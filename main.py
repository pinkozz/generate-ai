from flask import Flask, request, render_template, redirect
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key="API_KEY")

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/generate", methods=['POST'])
def generate():
    data = request.form
    prompt = data['prompt']

    response = client.images.generate(
        model="dall-e-2",
        prompt=prompt,
        size="256x256",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url
    return render_template("index.html", url=image_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)