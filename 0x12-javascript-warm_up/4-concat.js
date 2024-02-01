#!/usr/bin/node
const checkArgs = () => {
  const i = process.argv[2];
  const j = process.argv[3];

  console.log(i + ' is ' + j);
};

checkArgs();
