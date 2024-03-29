#!/usr/bin/node
let logno = 0;
exports.logMe = function (item) {
  logno++;
  console.log(`${logno - 1}: ${item}`);
};
