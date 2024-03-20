## Generate AI
Generative AI web app based on OpenAI's GPT and DALL-E models. Written on Python Flask.
![Screenshot from 2024-03-15 15-07-29](https://github.com/pinkozz/generate-ai/assets/136079534/c7938cfe-8cf9-4704-8a38-7bc0a1ca7200)
![Screenshot from 2024-03-15 15-07-20](https://github.com/pinkozz/generate-ai/assets/136079534/05ead335-2919-41a8-9c81-b5179418dcd9)

!! Before starting the app on your machine, ensure you have Python3 installed !!

# Set up
Clone the repository
```
git clone https://github.com/pinkozz/generate-ai
```

Navigate to project folder
```
cd generate-ai
```

Install requirements
```
pip3 install -r requirements.txt
```

Create API key on OpenAI's website and paste it instead of "API_KEY" in main.py:
```
client = OpenAI(api_key="API_KEY")
```

Run the app
```
python3 main.py
```

# Usage
Once the app is up and runnning, you can use it on http://localhost:3000. You will get access to its features, like image generation.
