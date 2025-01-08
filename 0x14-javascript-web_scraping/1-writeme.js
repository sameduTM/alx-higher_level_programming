#!/usr/bin/node
const filepath = process.argv[2];
const fs = require('fs');
const stringtoWrite = process.argv[3];
fs.writeFile(filepath, stringtoWrite, 'utf-8', (err) => {
  if (err) { console.error(err); }
});
