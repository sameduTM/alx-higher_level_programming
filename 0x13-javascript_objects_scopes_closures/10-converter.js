#!/usr/bin/node
exports.converter = function (base) {
  function myConverter (number, base) {
    const dgts = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ';

    if (number < base) {
      return dgts[number];
    } else {
      const rem = number % base;
      const qt = (number - rem) / base;
      return myConverter(qt, base) + dgts[rem];
    }
  }

  return function (number) {
    return myConverter(number, base);
  };
};
