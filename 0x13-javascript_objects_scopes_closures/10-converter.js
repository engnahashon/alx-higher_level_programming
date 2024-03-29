#!/usr/bin/node
exports.converter = function (base) {
  return function convertToBase10 (number) {
    return number < base ? String(number) : convertToBase10(Math.floor(number / base)) + String(number % base);
  };
};
