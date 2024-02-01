#!/usr/bin/node
const numArgs = process.argv.length - 2;

if (numArgs === 0) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('C is fun');
  }
}
