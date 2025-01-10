#!/usr/bin/node
const request = require('request');

function fetchUrl (url) {
  return new Promise((resolve, reject) => {
    request(url, { json: true }, (err, res, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(body);
      }
    });
  });
}

async function fetchCharacters (characters) {
  for (const url of characters) {
    try {
      const character = await fetchUrl(url);
      console.log(character.name);
    } catch (error) {
      console.error('Failed to fetch character:', error);
    }
  }
}

if (process.argv.length <= 2) {
  console.log('Please provide a movie ID as an argument.');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

fetchUrl(url)
  .then(film => {
    if (film && film.characters) {
      fetchCharacters(film.characters);
    } else {
      console.log('No characters found for this movie.');
    }
  })
  .catch(error => {
    console.error('Failed to fetch film:', error);
  });
