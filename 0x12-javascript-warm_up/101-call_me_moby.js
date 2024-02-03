#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  if (x < 0) {
    x = 0;
  }
  while (x !== 0) {
    theFunction();
    x--;
  }
};
