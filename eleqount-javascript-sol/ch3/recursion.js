const isEven = function(n) {
    if (n == 0)
        return true;
    if (n == 1)
        return false;
    return isEven(n-2);
}

console.log(isEven(9));
console.log(isEven(1));
console.log(isEven(0));
console.log(isEven(6));
