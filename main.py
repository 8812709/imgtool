from fastapi import FastAPI, UploadFile, File,Form
from PIL import Image
from fastapi.responses import JSONResponse
app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)
@app.post("/resize")
async def resize_image(passportphoto:UploadFile=File(),width:int=Form(),height:int=Form(),targetsize:int=Form()):
    details={"message":"The resized image has been saved in the imgtool folder of this PC by a new name as newimage1.png"}
    img = Image.open(passportphoto.file) #Open the image using syntax "open" which fetch the image data through the uploaded file
    resized_image = img.resize((int(width),int(height))) #Resize the image using the syntax "resize"
    resized_image.save("newimage1.png")  #saves the image in my pc in imgtool folder
    quality=95
    targetsize=targetsize*1024 #converting it in bytes(since on the frontend it was mentioned kb)
    actualsize=os.path.getsize("newimage1.png")#the size of the image for comparision
    while True:
        if targetsize<actualsize and quality>1: #will compare the size of the image and desired size and will give the most appropriate result
            quality=quality-3
            resized_image.save("newimage1.png",optimize=True,quality=quality)
            actualsize=os.path.getsize("newimage1.png")
        else:
            break
    return JSONResponse(content=details)  #returns the details which student has given and delivers a message alongwith
@app.post("/aspectratio")
async def ratio_resize(passportphoto:UploadFile=File(),width:int=Form(),height:int=Form(),targetsize:int=Form()):
    details={"message":"The resized image has been saved in the imgtool folder of this PC by a new name as newimage1.png"}
    img2 = Image.open(passportphoto.file) #Open the image using syntax "open" which fetch the image data through the uploaded file
    img2.thumbnail((int(width),int(height))) #Resize the image to 300*300 ratio using the syntax "resize"
    img2.save("newimage1.png") #saves the image in my pc in imgtool folder
    quality=95
    targetsize=targetsize*1024
    actualsize=os.path.getsize("newimage1.png")
    while True:
        if targetsize<actualsize and quality>1:
            quality=quality-5
            img2.save("newimage1.png",optimize=True,quality=quality)
            actualsize=os.path.getsize("newimage1.png")
        else:
            break
    return JSONResponse(content=details)  #returns a message
