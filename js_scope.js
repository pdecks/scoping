var someNumber = 10;

function someFunction(){
    someNumber += 1;
    console.log(someNumber);
    var otherNumber = 20;

}

function anotherFunction(){
    otherNumber += 1;
    console.log(otherNumber);
}

// before running someFunction
console.log('Initial value of someNumber, global:');
console.log(someNumber);

console.log('Value of someNumber, after running someFunction:');
someFunction();

console.log('Calling otherNumber inside function: ... not available');
anotherFunction();

console.log('Trying to call otherNumber outside of function scope: ... not available');
console.log(otherNumber);