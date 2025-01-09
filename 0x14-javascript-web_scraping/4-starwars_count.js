#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const characterId = 18;
let count = 0;

request(url, (err, response, data) => {
  if (err) { console.error(err); }
  const films = JSON.parse(data).results;
  films.forEach((film) => {
    const characters = film.characters;
    characters.forEach((character) => {
      if (character.includes(characterId)) {
        count++;
      }
    });
  });
  console.log(count);
});
