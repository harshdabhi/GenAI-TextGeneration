from fastapi import FastAPI
from transformers import pipeline


app = FastAPI()

pipe = pipeline("text2text-generation", model="google/flan-t5-small")


@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.get("/generate")
def generate(text: str):
    return pipe(text)