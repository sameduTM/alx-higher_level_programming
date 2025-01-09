#!/usr/bin/env node
const request = require('request');
const url = process.argv[2];
const characterId = 'https://swapi-api.alx-tools.com/api/people/18/';
let count = 0;

request(url, (err, response, data) => {
  if (err) { console.error(err); }
  const films = JSON.parse(data).results;
  films.forEach((film) => {
    const characters = film.characters;
    characters.forEach((character) => {
      if (characterId === character) {
        count++;
      }
    });
  });
  console.log(count);
});
