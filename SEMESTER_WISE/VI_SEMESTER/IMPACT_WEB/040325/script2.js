// const newDate=new Date();
// console.log(newDate);
// var hours=newDate.getHours();
// var minutes=newDate.getMinutes();
// var seconds=newDate.getSeconds();       


//digital clock

function clock(){
    const newDate=new Date();
    setTimeout(()=>{

    
    document.getElementById('hours').innerHTML=newDate.getHours();
    document.getElementById('minutes').innerHTML=newDate.getMinutes();
    document.getElementById('seconds').innerHTML=newDate.getSeconds();
    clock();
    },1000)
}

clock()