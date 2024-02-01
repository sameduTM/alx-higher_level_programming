#!/usr/bin/node
const checkArgs = () => {
  numArgs = process.argv.length - 2;

  if (process.argv[2] === undefined) {
    console.log('No argument');
  } else {
    console.log(process.argv[2]);
  }
};

checkArgs();
