function myFun(){
    // alert("Hello World!");
   const name= document.forms["myForm"].nm.value;
   const city=document.forms["myForm"].city.value;
   alert(name)

   document.getElementById("result").innerText=`My Nmae is ${name} and I belongs to ${city}`;
    

}