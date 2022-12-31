from fastapi import FastAPI
from pydantic import BaseModel

pipeline = /Users/staceyjohnson/PycharmProjects/MLE11/FBML11/assignments/week-03-huggingface-fastapi/fast_api_tutorial/app/model

app = FastAPI()

class TextToTranslate(BaseModel):
    input_text: str

class  

@app.get("/")
def index():
    return {"message": "Hello World"}

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.post("/echo")
def echo(text_to_translate: TextToTranslate):
    return {"message": text_to_translate.input_text}

@app.post("/trans")
def trans()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)



