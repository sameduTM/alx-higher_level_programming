#!/usr/bin/node
const checkArgs = () => {
    const firstArg = process.argv[2];
    val = parseInt(firstArg);

    if (isNaN(val)) {
        console.log('Not a number');
    } else {
        console.log(val);
    }
};

checkArgs();