import ebuddy

from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Question(BaseModel):
    question : str
    
@app.post("/question")
def ask_question_to_ebuddy(question: Question):
        
    return ebuddy.ask_ebuddy(question.question)

