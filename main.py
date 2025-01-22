from flask import Flask, request, render_template

import os
from random import randint

import torch
import torch.quantization as quant
from transformers import AutoTokenizer, AutoModelForCausalLM
from diffusers import StableDiffusionPipeline, DDIMScheduler

# Load model with optimizations
image_generator = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype = torch.float32
)

# For text generation (e.g., GPT-2 or GPT-3-like models)
text_model_name = "gpt2"
text_tokenizer = AutoTokenizer.from_pretrained(text_model_name)
text_tokenizer.pad_token = text_tokenizer.eos_token
text_model = AutoModelForCausalLM.from_pretrained(text_model_name)

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("main.html")

@app.route("/generate-image", methods=["GET"])
def generate_index():
    return render_template("generate-image.html")

@app.route("/generate-image", methods=["POST"])
def generate():
    prompt = request.form["prompt"]
    inference_steps = request.form["inference_steps"]
    try:
        image = image_generator(prompt=prompt, num_inference_steps=int(inference_steps)).images[0] # Generate image

        output_path = f"static/generated/{f"generation{randint(1,9999999999)}"}.png"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        image.save(output_path)

        return render_template(
            "generate-image.html", 
            prompt=prompt, 
            url=output_path,
        )
    except Exception as e:
        return render_template(
            "generate-image.html", 
            prompt=prompt, 
            error=str(e),
        )

@app.route("/finish-sentence", methods=["GET"])
def finish_index():
    return render_template("finish-sentence.html")

@app.route("/finish-sentence", methods=['POST'])
def finish():
    current_page = "/finish-sentence"  
    data = request.form
    prompt = data['prompt']
    temperature = float(data['temperature'])/100

    # Generate output, continuing from the prompt
    inputs = text_tokenizer(
        prompt, 
        padding=True,
        truncation=True,
        return_tensors="pt",
        return_attention_mask=True
    )


    output_ids = text_model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=50,
        num_return_sequences=1,
        temperature=temperature,
        top_k=50,
        top_p=0.9,
        do_sample=True
    )

    # Decode only the continuation (exclude the prompt itself)
    finished_sentence = text_tokenizer.decode(output_ids[0], skip_special_tokens=True)

    dot = finished_sentence[len(prompt):].index(".")
    finished_sentence = f"{finished_sentence[len(prompt):][:dot]}."

    return render_template("finish-sentence.html", prompt=prompt, finished=finished_sentence, current_page=current_page)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)