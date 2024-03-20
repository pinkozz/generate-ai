from flask import Flask, request, render_template
from openai import OpenAI
from time import gmtime, strftime

app = Flask(__name__)
client = OpenAI(api_key="API_KEY")

year = strftime("%Y", gmtime())
current_page = "/"

# Home page
@app.route("/", methods=['GET'])
def index():
    current_page = "/"
    return render_template("main.html", year=year, current_page=current_page)

# Generate image page
@app.route("/generate-image", methods=['GET'])
def generate_index():
    current_page = "/generate-image"    
    return render_template("generate-image.html", year=year, current_page=current_page)

@app.route("/generate-image", methods=['POST'])
def generate():
    current_page = "/generate-image"
    data = request.form
    prompt = data['prompt']

    response = client.images.generate(
        model="dall-e-2",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url
    return render_template("generate-image.html", prompt=prompt, year=year, url=image_url, current_page=current_page)

# Finish sentence page
@app.route("/finish-sentence", methods=['GET'])
def finish_index():
    current_page = "/finish-sentence"
    return render_template("finish-sentence.html", year=year, current_page=current_page)

@app.route("/finish-sentence", methods=['POST'])
def finish():
    current_page = "/finish-sentence"  
    data = request.form
    prompt = data['prompt']

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that helps finish the sentence. Take a role of a creative and interesting writer while being laconic."},
            {"role": "user", "content": prompt},
        ],
    )

    finished_sentence = response.choices[0].message.content
    return render_template("finish-sentence.html", prompt=prompt, year=year, finished=finished_sentence, current_page=current_page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)