#!/usr/bin/node
let myFuncCalls = 0;
exports.logMe = function (item) {
  console.log(myFuncCalls + ':', item);
  myFuncCalls++;
};
