#!/usr/bin/node

const arg1 = process.argv[2] || 'undefined';
const arg2 = process.argv[3] || 'undefined';

const output = `${arg1} is ${arg2}`;
console.log(output);
