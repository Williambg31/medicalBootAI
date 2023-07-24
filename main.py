from typing import Union
from fastapi import FastAPI
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.vectorstores import Chroma
from pydantic import BaseModel
from apiKEY import OPENAI_API_KEY
import os

os.environ["OPENAI_API_KEY"]=OPENAI_API_KEY
loader=PyPDFLoader('./Docs/UrgenciasGuia.pdf')
index=VectorstoreIndexCreator().from_loaders([loader])

app=FastAPI()

class Item(BaseModel):
    query:str

@app.get('/')
def read_root():
    return {"Hola": "Mundo"}
@app.post('/')
def answer_query(item:Item):
    try:    
        response=index.query(item.query)
        return response
    except:
        return {"Mensaje":"Ocurrió algún Error!"}
