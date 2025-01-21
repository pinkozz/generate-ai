## Generate AI
This website showcases the power of generative AI for creating images and completing sentences based on user input. It features a simple, user-friendly design, making advanced AI accessible for creative and practical use. The platform highlights the potential of AI in transforming ideas into engaging visual and textual content.

https://github.com/user-attachments/assets/31ab52d9-b55e-4521-8aae-ab9b4ae0458a

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

Download Pretrained Models: Run the following commands to pre-download the models used by the app:
```
from transformers import AutoTokenizer, AutoModelForCausalLM
from diffusers import StableDiffusionPipeline

# For text generation
tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")

# For image generation
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")

```

Run the app
```
python3 main.py
```

# Usage
Once the app is up and runnning, you can use it on http://localhost:3000. You will get access to its features, like image generation.
