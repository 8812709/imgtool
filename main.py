from fastapi import FastAPI, UploadFile, File,HTTPException
from PIL import Image,UnidentifiedImageError
app = FastAPI()
@app.post("/resize")
async def resize_image(passportphoto:UploadFile=File(),width:int=300,height:int=300):
    details={"message":"The resized image has been saved in the imgtool folder of this PC by a new name as newimage1.png"}
    try:
        img = Image.open(passportphoto.file) #Open the image using syntax "open" which fetch the image data through the uploaded file
    except UnidentifiedImageError:
        raise HTTPException(status_code=401,detail="please upload a vaild image")
    if (width<1 or height<1):
        raise HTTPException(status_code=400,detail="please enter the valid width and height for image resizing i.e. greater than 1")
    resized_image = img.resize((int(width),int(height))) #Resize the image to 300*300 ratio using the syntax "resize"
    resized_image.save("newimage1.png")  #saves the image in my pc in imgtool folder
    return(details)  #returns the details which student has given and delivers a message alongwith
@app.post("/compression") #creates a endpoint named as compression
async def compress_image(quality: int = 20, uploadphoto: UploadFile = File()): #declareed a function compress image with two paramters quality and uploadphoto
    try:
        compimage = Image.open(uploadphoto.file) #a vaiable comp image which will open the image whatever i have uploaded in the UI
    except UnidentifiedImageError:
        raise HTTPException(status_code=400, detail="Please upload a valid image")
    if(quality<1 or quality>95):
        raise HTTPException(status_code=400,detail="invalid value of quality selected please select between 1 and 95")
    
    compimage.save("newcompimage1.png", optimize=True, quality=quality) #it will save the image in the same directory where my python file is present with the quality of image i have choosen
    details = {"message": "The compressed file has been saved to the imgfolder with name newimage2.png"}
    return details #it will return the details i have included in the details i.e. a message
@app.post("/aspectratio")
async def ratio_resize(passportphoto:UploadFile=File(),width:int=300,height:int=300):
    details={"message":"The resized image has been saved in the imgtool folder of this PC by a new name as newimage1.png"}
    try:
        img2 = Image.open(passportphoto.file) #Open the image using syntax "open" which fetch the image data through the uploaded file
    except UnidentifiedImageError:
        raise HTTPException(status_code=401,detail="please upload a vaild image")
    if (width<1 or height<1):
        raise HTTPException(status_code=400,detail="please enter the valid width and height for image resizing i.e. greater than 1")
    resized_img= img2.thumbnail((int(width),int(height))) #Resize the image to 300*300 ratio using the syntax "resize"
    img2.save("newimage2.png") #saves the image in my pc in imgtool folder
    return(details)  #returns a message 