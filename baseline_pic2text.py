import requests
import torch
from PIL import Image
from transformers import BlipProcessor, BlipForQuestionAnswering

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"running on {device}...")

processor = BlipProcessor.from_pretrained("Salesforce/blip-vqa-base")
model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base")

def describe_img(input_image):
    '''print (input_image)'''
    

    '''img_url = 'https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg' 
    raw_image = Image.open(requests.get(img_url, stream=True).raw).convert('RGB')'''

    question = "describe this image"
    inputs = processor(input_image, question, return_tensors="pt")

    out = model.generate(**inputs)
    generated_text = processor.decode(out[0], skip_special_tokens=True)
    print(generated_text)
    return generated_text
