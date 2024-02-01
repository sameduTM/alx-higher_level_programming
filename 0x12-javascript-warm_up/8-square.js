#!/usr/bin/node
const sz = parseInt(process.argv[2]);
let str = '';

if (isNaN(sz)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < sz; i++) {
    str = 'X';
    for (let j = 1; j < sz; j++) {
      str += 'X';
    }
    console.log(str);
  }
}
