import torch
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipe = pipe.to(("cuda" if torch.cuda.is_available() else "cpu"))

prompt = "a photo of an astronaut riding a horse on mars"
image = pipe(prompt).images[0]