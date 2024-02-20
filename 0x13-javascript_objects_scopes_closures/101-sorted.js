#!/usr/bin/node

const { dict } = require('./101-data.js');

const sorted = {};

for (const key in dict) {
  if (dict.hasOwnProperty(key)) {
    const value = dict[key];
    if (!sorted.hasOwnProperty(value)) {
      sorted[value] = [];
    }
    sorted[value].push(key);
  }
}

console.log(sorted);
