#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
const comTasks = [];
const users = [];

request(url, (err, response, data) => {
  if (err) { console.error(err); }
  const todos = JSON.parse(data);
  todos.forEach((todo) => {
    if (todo.completed === true) {
      comTasks.push(todo);
    }
  });
  comTasks.forEach((task) => {
    users.push(task.userId);
  });
  function getNumOfTimes (arrayOfNums) {
    const found = {};
    for (let i = 0; i < arrayOfNums.length; i++) {
      const keys = arrayOfNums[i].toString();
      found[keys] = ++found[arrayOfNums[i]] || 1;
    }

    return found;
  }

  console.log(getNumOfTimes(users));
});
