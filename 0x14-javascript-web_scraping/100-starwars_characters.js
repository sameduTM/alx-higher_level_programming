#!/usr/bin/env node
const movieID = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieID + '/';
const request = require('request');

request(url, (err, response, data) => {
  if (err) { console.error(err); }
  const characters = JSON.parse(data).characters;
  characters.forEach((character) => {
    const apiURL = String(character);
    request(apiURL, (err, response, data) => {
      if (err) { console.error(err); }
      console.log(JSON.parse(data).name);
    });
  });
});
