var division = require('./Division.js');
var multiplication = require('./Multiplication.js');

//var valueData = [ 8, 3, 0.52, 0.72, 0, 95, 0.5, 16, 6, 0.26, 331, 123.1, 0 ];

testExample = function (valueData){
    for(var value of valueData){

    if (value ==0){
         console.log("Skipping over value 0\n");
         continue;
    }
    try
    {
        console.log(value + " squared is " + Square(value) + "\n")
        console.log(value + " cubed is " + Cube(value) + "\n")
        console.log(value + " multiplied by 3 is " + Multiply(value,3) + "\n")
        console.log(value + " halved is " + Half(value) + "\n")
        console.log(value + " quartered is " + Quarter(value) + "\n")
        console.log(value + " diveded by zero is " + Divide(value,0) + "\n")

    }
    catch(err)
    {
        console.log(err.message+"\n");
    }
}
}