import uvicorn 
import pickle
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import warnings 
warnings.filterwarnings("ignore")

path="task1.ipynb"
load_model=pickle.load(open("model.pkl","rb"))


app=FastAPI()

@app.get("/")
def intro():
    return {"getting stronger day by day"}

def get_input(input):
    prediction=load_model.predict([[input]])
    result=prediction.tolist()
    print(result)
    return result

@app.get("/prediction")
def predict(input:int):
    pred=get_input(input)
    return{"result":pred[0]} #  