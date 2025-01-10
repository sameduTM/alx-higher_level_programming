#!/usr/bin/env node
const request = require('request');

const array = ['1', '2', '3', '4', '5'];
const results = new Array(array.length); // Initialize results array to hold responses

array.forEach((item, index) => {
  const url = `https://swapi-api.alx-tools.com/api/films/${item}`;
  request(url, (err, response, data) => {
    if (err) {
      console.error('Error fetching data:', err);
      return;
    }
    // Store the film title in the corresponding index
    results[index] = JSON.parse(data).title;

    // Check if all entries in the results array are filled
    if (results.filter(title => title).length === array.length) {
      // All requests have completed, print results in order
      results.forEach(title => console.log(title));
    }
  });
});
