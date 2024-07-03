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
    wvalue=welement.value; //width value set
    console.log("Width and Height are set as:",wvalue,hvalue);
}
helement.addEventListener('change',setdata); //sets the value of height and width when value changes inside the input box
helement.addEventListener('change',setdata); 


//image setting in js
let imgelement=document.getElementById("inputimage");
//geting image element
function settingimage(event) 
{
    event.preventDefault();
    imagedata=imgelement.files[0]; //setting image data(not element) in the imagedata variable
    console.log("image is uploaded");
    if(imagedata!=null)
        {
            uploadbutton.textContent="Uploaded"; //will change text content to uploaded if file selected
        }
    else{
        uploadbutton.textContent="Upload"; //will change it to upload if not slected
    }
}
let uploadbutton=document.getElementById("uploadbut");
uploadbutton.addEventListener('click',settingimage);//on clicking upload it will upload the image in my js 



//fetching api now using download button
//declared the endpoints of resizing here
const resizeurl="http://127.0.0.1:8000/resize";
const aspectRatioUrl="http://127.0.0.1:8000/aspectratio";

// if checckbox is clicked then maintaining aspect ratio endpoint
let checkbox=document.getElementById("checkbox");
if(checkbox.checked)
    {
        async function postdata1(event)
        {
        event.preventDefault();
        const formData = new FormData();
        formData.append('passportphoto', imagedata);
        formData.append('width', wvalue);
        formData.append('height', hvalue);
        const response=await fetch(aspectRatioUrl,{ //telling to fetch response from 
            method:'POST', //post upload method
            body:formData
        });
        let readable=await response.json(); //using json to convert the response from api to readable format 
        console.log(readable); 
    }
        resizebutton=document.getElementById("resizebut");
        resizebutton.addEventListener('click',postdata1);
    }
else //it will go for custom resizng endpoint and will return custom image here
{
    async function postdata2(event)
    {
        event.preventDefault();
        const formData = new FormData();
        formData.append('passportphoto', imagedata);
        formData.append('width', wvalue);
        formData.append('height', hvalue);
        const response=await fetch(resizeurl,{
            method:'POST', //post upload method
            body:formData
        });
        let readable=await response.json(); //using json to convert the response from api to readable format 
        console.log(readable); 
    }
    resizebutton=document.getElementById("resizebut");
    resizebutton.addEventListener('click',postdata2);
}
