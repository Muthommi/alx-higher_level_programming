#!/usr/bin/node

const arg1 = process.argv[2];
const arg2 = process.argv[3];

const num1 = parseInt(arg1);
const num2 = parseInt(arg2);

function add (a, b) {
  return a + b;
}

if (isNaN(num1) || isNaN(num2)) {
  console.log('NaN');
} else {
  console.log(add(num1, num2));
}
