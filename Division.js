Half = function (value){
    return value/2;
}

Quarter = function (value){
    return value/4;
}

Divide = function (value, divisor){
    if(divisor ==0){
        throw new Error("Divisor cannot be zero");
    }
    return value / divisor;
}

