from flask import Flask, request, render_template

import os
from random import randint

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from diffusers import StableDiffusionPipeline

image_generator = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
image_generator = image_generator.to("cuda" if torch.cuda.is_available() else "cpu")

# For text generation (e.g., GPT-2 or GPT-3-like models)
text_model_name = "gpt2"
text_tokenizer = AutoTokenizer.from_pretrained(text_model_name)
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
    try:
        image = image_generator(prompt=prompt).images[0] # Generate image

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

    # Generate text completion
    input_ids = text_tokenizer.encode(prompt, return_tensors="pt")

    # Generate output, continuing from the prompt
    output = text_model.generate(
        input_ids, 
        max_length=len(input_ids[0]) + 50,  # Extend the prompt by up to 50 tokens
        num_return_sequences=1,
        do_sample=True,
    )

    # Decode only the continuation (exclude the prompt itself)
    finished_sentence = text_tokenizer.decode(
        output[0][len(input_ids[0]):], skip_special_tokens=True
    )

    return render_template("finish-sentence.html", prompt=prompt, finished=finished_sentence, current_page=current_page)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
