#!/usr/bin/node
let logno = 0;
exports.logMe = function (item) {
  logno++;
  console.log('${count - 1}: ${item}');
};
