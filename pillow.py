from PIL import Image
img=Image.open("genshin.png") #img is an object created which opens the image named genshin.png
img.show() #it shows the image in the display
print(img.height,img.width)
print(img.size)
print(img.format)
resize_1=(300,300)#the size i want in my new image
img.thumbnail(resize_1) #using thumbnail syntax to resize my orginal image,but it maintains the aspect ratio of the image
img.save("genshin_new.png") #using save sytax to save my new image as the follwing name in the same folder
img.resize(resize_1)#using syntax resize which doesnt maintains the aspect ratio
img.save("new_image.png")
new_img=Image.open("new_image.png")
print(new_img.size)