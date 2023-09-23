from PIL import Image
from transformers import pipeline

vqa_pipeline = pipeline("visual-question-answering")

image =  Image.open("/home/victorknox/Viz/images/pandabutt.jpeg")
question = "what is going on in this picture? what is the animal doing?"

print(vqa_pipeline(image, question, top_k=1))

#[{'score': 0.9998154044151306, 'answer': 'yes'}]
