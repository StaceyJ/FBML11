import transformers
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from transformers import pipeline

app = FastAPI()

# Initialize the pipeline
pipeline = transformers.pipeline("translation_en_to_fr", model="t5-small”, max_length=512)

class TextToTranslate(BaseModel):
    input_text: str

class TextsToTranslate(BaseModel):
    input_texts: List[str]

@app.get("/")
def index():
    return {"message": "Hello World"}

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.post("/echo") 
def echo(text_to_translate: TextToTranslate):
    return {"message": text_to_translate.input_text}
    
@app.post("/translate")
def translate_text(text_to_translate: TextToTranslate):
    # Use the pipeline to translate the text
    translated_text = pipeline(text_to_translate.input_text, max_length=4096)[0]['translation_text']
    return {"translated_text": translated_text}

@app.post("/translates")
def translate_text(texts_to_translate: TextsToTranslate):
    translated_texts = []
    for text in texts_to_translate.input_texts:
        translated_text = pipeline(text, max_length=4096)[0]['translation_text']
        translated_texts.append(translated_text)
    return {"translated_texts": translated_texts}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
