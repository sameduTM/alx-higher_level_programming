#!/usr/bin/node

const { dict } = require('./101-data.js');

const sorted = {};

for (const key in dict) {
  if (Object.prototype.hasOwnProperty.call(dict, key)) {
    const value = dict[key];
    if (!Object.prototype.hasOwnProperty.call(sorted, value)) {
      sorted[value] = [];
    }
    sorted[value].push(key);
  }
}

console.log(sorted);
