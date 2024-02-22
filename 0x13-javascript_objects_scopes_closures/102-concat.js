#!/usr/bin/node
const file1 = process.argv[2];
const file2 = process.argv[3];
const file3 = process.argv[4];

const fs = require('node:fs');

const fl1 = fs.readFileSync(file1, { encoding: 'utf8', flag: 'r' });
const fl2 = fs.readFileSync(file2, { encoding: 'utf8', flag: 'r' });

fs.appendFileSync(file3, fl1 + fl2);
