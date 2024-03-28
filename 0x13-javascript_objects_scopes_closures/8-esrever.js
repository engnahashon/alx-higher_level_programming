#!/usr/bin/node
exports.esrever = function (list) {
  const hold = [];

  for (let i = list.length - 1; i >= 0; i--) {
    hold.push(list[i]);
  }
  return hold;
};
