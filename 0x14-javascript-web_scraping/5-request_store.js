#!/usr/bin/env node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filepath = process.argv[3];

request(url, 'utf-8', (err, response, body) => {
  if (err) { console.error(err); }
  fs.writeFile(filepath, body, 'utf-8', (err) => {
    if (err) { console.error(err); }
  });
});
