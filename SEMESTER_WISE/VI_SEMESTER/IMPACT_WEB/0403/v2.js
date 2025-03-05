function myFun() {
    var username = document.myForm.username.value;
    var password = document.myForm.password.value;
    var result = document.getElementById("result");

    
    if (username.length < 5) {
        result.textContent = "Username must be at least 5 characters long.";
        
        return false; // Prevent form submission
    }

    
    if (password.length < 6) {
        result.textContent = "Password must be at least 6 characters long.";
    
        return false; // Prevent form submission
    }

   
    result.textContent = "Login successful!";
   

   
}
