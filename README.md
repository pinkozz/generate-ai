## Generate AI
Generative AI web app based on OpenAI's GPT and DALL-E models. Written on Python Flask.

https://github.com/pinkozz/generate-ai/assets/136079534/73ff1926-7a4a-4535-b17f-84325a0064d1

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
