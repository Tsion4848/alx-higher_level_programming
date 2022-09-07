#!/usr/bin/node

let old = require('./101-data.js').dict;
let newDic = {};
Object.keys(old).forEach(function (key) {
  if (newDic[old[key]] === undefined) {
    new[old[key]] = [];
  }
  newDic[old[key]].push(key);
});
console.log(newDic);
