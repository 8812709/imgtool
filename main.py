from typing import Union #this module helps in setting default values 
from fastapi import FastAPI, Query 
from enum import Enum
app = FastAPI()

class options(str, Enum):
    option1 = "alexnet"
    option2 = "resnet"
    option3 = "lenet"


@app.get("/hello")#path 
def read_root():
    return {"hi from my side"}#the result it will show at the server


@app.get("/hy") #it will do the same as above
def read_item():
    return {"message":"heyya"}



@app.get("/query/{items}") #server query where a path parameter is set as item which will run the func and return the item itself which is stored in a varibale 
def func(items):
    name={"path variabl":items}
    return(name)

@app.get("/details") #have to put my name and roll no as required parameters else it will show error 
def info(name:str,roll_no:int):
    name={"name":name,"roll no":roll_no}
    return(name)
@app.get("/details2") #have to put my name and roll no(optional)or it will show the default value as null) as required parameters else it wont load the server
def info(name:str,roll_no:Union[str,None]=Query(default=None,min_length=3,max_length=3)):#the min length and max length works on strings and not on integer so changed the type,the query helps in fixing the max and min length of the stringg which is 3 here.
    name={"name":name,"roll no":roll_no}#storing the name and roll no in a variable
    return(name) #reurning the variable

@app.get("/models/{items}") 
async def getmodel(items: options): #predefining the parameters in the class options
    return(items)
