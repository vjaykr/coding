function myFun() {
    const name= document.forms["myForm"].nm.value;
    const pass=document.forms["myForm"].pass.value;
    
    if (name == ""){
        document.getElementById("result").innerText="Please enter your name";
    }
    else if (pass == ""){
        document.getElementById("result").innerText="Please enter your password";
    }
    else{
        document.getElementById("result").innerText=`My Name is ${name} and my password is ${pass}`;
    }


}