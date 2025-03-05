function clock() {
    const newDate = new Date();
    let hours = newDate.getHours();
    let minutes = newDate.getMinutes();
    let seconds = newDate.getSeconds();
    let amPm = hours >= 12 ? "PM" : "AM";
    
    hours = hours % 12;
    hours = hours ? hours : 12; // the hour '0' should be '12'
    minutes = minutes < 10 ? '0' + minutes : minutes;
    seconds = seconds < 10 ? '0' + seconds : seconds;

    document.getElementById("hrs").innerHTML = hours;
    document.getElementById("min").innerHTML = minutes;
    document.getElementById("sec").innerHTML = seconds;
    document.getElementById("status").innerHTML = amPm;
}

setInterval(clock, 1000);
clock();
