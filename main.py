from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def read_root():
    return {"hi from my side"}


@app.get("/hy")
def read_item():
    return {"message":"heyya"}