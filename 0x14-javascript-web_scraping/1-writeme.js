#!/usr/bin/env node
filepath = process.argv[2];
const fs = require('fs');
string_to_write = process.argv[3];
fs.writeFile(filepath, 'utf-8', string_to_write, (err) => {
    if (err)
        console.error(err);
});