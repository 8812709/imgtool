from fastapi import FastAPI, UploadFile, File
from PIL import Image

app = FastAPI()


@app.get("/details") #have to put my name and roll no as required parameters else it will show error 
def info(name:str,roll_no:int):
    name={"name":name,"roll no":roll_no}
    return(name)

@app.post("/resize")
async def resize_image(name:str,roll_no:int,passportphoto:UploadFile=File()):
    details={"name":name,"roll_no":roll_no,"message":"The resized image has been saved in the imgtool folder of this PC by a new name as newimage1.png"}
    img = Image.open(passportphoto.file) # Open the image using syntax "open" which fetch the image data through the uploaded file
    resized_image = img.resize((300,300)) # Resize the image to 300*300 ratio using the syntax "resize"
    resized_image.save("newimage1.png")  #saves the image in my pc in imgtool folder
    return(details)  #returns the details which student has given and delivers a message alongwith
    