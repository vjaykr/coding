function myFun() {
    const name = document.forms['myForm']['nm'].value;
    const city = document.forms['myForm']['city'].value;
    document.getElementById('result').innerText = `My Name is ${name} and I belong to ${city}`;
}
