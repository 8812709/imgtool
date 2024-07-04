let hvalue;
let wvalue;
let imagedata;
console.log("getting element id");
let helement=document.getElementById("hei");
let welement=document.getElementById("wid");

function setdata(event) //to save the value of width and height somewhere in js
{
    event.preventDefault();
    hvalue=helement.value; //height value set 
    wvalue=welement.value;//width value set
    console.log("Width and Height are set as:",wvalue,hvalue);
}
helement.addEventListener('change',setdata); //sets the value of height and width when value changes inside the input box
welement.addEventListener('change',setdata); 


//image setting in js
let imgelement=document.getElementById("inputimage");
//geting image element
function settingimage(event) 
{
    event.preventDefault();
    imagedata=imgelement.files[0]; //setting image data(not element) in the imagedata variable
    if(imagedata!=null)
        {
            console.log("image is uploaded");
            uploadbutton.textContent="Uploaded"; //will change text content to uploaded if file selected
        }
    else{
        uploadbutton.textContent="Upload"; //will change it to upload if not slected
        console.log("image is not selested yet");
        alert("please upload the image");
    }
}
let uploadbutton=document.getElementById("uploadbut");
uploadbutton.addEventListener('click',settingimage);//on clicking upload it will upload the image in my js 

//selecting endpoint URL here
let url="http://127.0.0.1:8000/resize"; //normal resize declared the url by default
let imgsrc; //name of the image where it is saved after the execution of api
function selecturl()
{
    if(checkbox.checked)
        {
            url="http://127.0.0.1:8000/aspectratio"; //will change the endpoint to apectratioif i checked the box
            imgsrc="newimage2.png";
            console.log("endpoint of aspect/ratio is selected as url");
            
        }
    else{
            url="http://127.0.0.1:8000/resize";
            imgsrc="newimage1.png";
            console.log("endpoint of resize is selected");
    }
}
let checkbox=document.getElementById("checkbox");
checkbox.addEventListener("change",selecturl);

async function postdata()
{
    const formData = new FormData();
    formData.append('passportphoto', imagedata);
    formData.append('width', wvalue);
    formData.append('height', hvalue);
    const response=await fetch(url,{
        method:'POST', //post upload method
        body:formData
    });
    let readable=await response.json(); //using json to convert the response from api to readable format 
    console.log(readable); 
}
resizebutton=document.getElementById("resizebut");
resizebutton.addEventListener('click',postdata);

// //download button
// let downloadbutton=document.getElementById("downloadbut"); 
// function downloadimage()
// {
//     let newfilename="downloaded.png";
//     let img=document.createElement("a");
//     img.getAttribute(image)
    
// }
// downloadbutton.addEventListener("click",downloadimage);
