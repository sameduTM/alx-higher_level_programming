#!/usr/bin/env node
const file1 = process.argv[2];
const file2 = process.argv[3];

const fs = require('node:fs');

const fl1 = fs.readFileSync('fileA', { encoding: 'utf8', flag: 'r' });
const fl2 = fs.readFileSync('fileB', { encoding: 'utf8', flag: 'r' });

fs.appendFileSync('fileC', fl1 + fl2);
