#!/usr/bin/env node
const i = process.argv[2];

console.log(i);

const fs = require('node:fs');

const content = i;

fs.writeFileSync('test.txt', content);

const data = fs.readFileSync('test.txt', { encoding: 'utf8', flag: 'r' });

console.log(data);
