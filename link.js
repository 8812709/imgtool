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
let imgelement=document.getElementById("inputimage");//geting image element
function settingimage() 
{
    imagedata=imgelement.files[0]; //setting image data(not element) in the imagedata variable
    if(imagedata!=null)
        {
            console.log("image is uploaded");
            uploadbutton.textContent="Uploaded"; //will change text content to uploaded if file selected
        }
    else{
        uploadbutton.textContent="Upload"; //will change it to upload if not slected
        console.log("image is not selested yet");
        alert("please select the image");
    }
}
let uploadbutton=document.getElementById("uploadbut");
//compression part setting the target size
let targetsize;
function setTargetSize()
{
    if(targetelement.value!=null)
    {
        targetsize=targetelement.value;
        console.log("the target size has been set to",targetsize);
    }
    else
    {
        alert("please set the estimated target size");
    }
    
}
let targetelement=document.getElementById("size");
targetelement.addEventListener('change',setTargetSize);
//selecting endpoint URL here
let url="http://127.0.0.1:8000/resize"; //normal resize url as endpoint before even clicking the checkbox
function selecturl()
{
    if(checkbox.checked)
        {
            url="http://127.0.0.1:8000/aspectratio"; //will change the endpoint to apectratio if i check the box
            console.log("endpoint of aspect/ratio is selected as url");
            
        }
    else{
            url="http://127.0.0.1:8000/resize"; //resize endpoint is selected if i uncheck the box
            console.log("endpoint of resize is selected"); 
    }
}
let checkbox=document.getElementById("checkbox");
checkbox.addEventListener("change",selecturl);
//resize button and its function
resizebutton=document.getElementById("resizebut")
async function postdata()
{
    const formData = new FormData(); //will make a new form object to store the data that has been input
    formData.append('passportphoto', imagedata);
    formData.append('width', wvalue);
    formData.append('height', hvalue);
    formData.append('targetsize',targetsize);
    // formData.append('targetsize',targetsize);
    let response = await fetch(url, { //to fetch the response through post method to the api 
            method: 'POST', //post  method is selected 
            body: formData 
    })
    let readable=await response.json; //to convert the data i recieved to json format is readable
    return console.log(readable);
    
}
function downloadimg(event)
{
    
    let imagesource="newimage1.png"; //i have declared the image source here
    aelement.setAttribute('href', imagesource);
    console.log("file is been downloaded");
}
let aelement=document.getElementById("imghere");
aelement.addEventListener('click',downloadimg);