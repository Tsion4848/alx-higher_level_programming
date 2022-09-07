#!/usr/bin/node
exports.esrever = function (list) {
  let temp = 0;
  for (let i = 0; i < list.length; i++) {
    let r = list.length - 1 - i;
    if (i < r) {
      temp = list[i];
      list[i] = list[r];
      list[r] = temp;
    }
  }
  return list;
};
