#!/usr/bin/node
let list = require('./100-data').list;

console.log(list);
const m = list.map((x, index) => x * index);
console.log(m);
