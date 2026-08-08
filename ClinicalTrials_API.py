from fastapi import FastAPI
from ClinicalTrials_Project1 import get_studies, get_maximum_ages

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the Clinical Trials API"}

@app.get("/studies")
def studies(condition: str):
    data = get_studies(condition)
    return data

@app.get("/maximum-ages")
def maximum_ages(condition: str):
    data = get_studies(condition)
    ages = get_maximum_ages(data, condition)
    return ages