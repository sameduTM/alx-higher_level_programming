#!/usr/bin/node
const numArgs = process.argv.length - 2;

const secondL = () => {
  const arr = [];
  let i = 0;

  if (numArgs <= 1) {
    console.log(0);
  } else {
    while (i < numArgs) {
      arr.push(parseInt(process.argv[i + 2]));
      i++;
    }
    console.log(arr);
    for (let i = 0; i < arr.length - 1; i++) {
      for (let j = 0; j < arr.length - 1; j++) {
        if (arr[j] < arr[j + 1]) {
          const temp = arr[j];
          arr[j] = arr[j + 1];
          arr[j + 1] = temp;
        }
      }
    }
    console.log(arr[1]);
  }
};

secondL();
