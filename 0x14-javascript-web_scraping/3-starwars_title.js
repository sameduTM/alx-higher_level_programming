#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id + '/';
request(url, function (err, response, data) {
  if (err) { console.error(err); }
  console.log(JSON.parse(data).title);
});
