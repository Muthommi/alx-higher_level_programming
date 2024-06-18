#!/usr/bin/node

const arg = process.argv[2];
const x = parseInt(arg);

if (isNaN(x) || x <= 0) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
