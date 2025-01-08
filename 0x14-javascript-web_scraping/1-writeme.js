#!/usr/bin/node
filepath = process.argv[2];
const fs = require('fs');
string_to_write = process.argv[3];
fs.writeFile(filepath, string_to_write,'utf-8', (err) => {
    if (err)
        console.error(err);
});