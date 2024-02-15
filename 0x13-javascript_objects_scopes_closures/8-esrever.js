#!/usr/bin/node
exports.esrever = function (list) {
  const arr = [];
  let r = list.length - 1;

  for (let i = 0; i < list.length; i++) {
    arr[i] = list[r];
    r--;
  }
  return arr;
};
