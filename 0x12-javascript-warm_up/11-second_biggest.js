#!/usr/bin/node

const list = process.argv.slice(2);
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  console.log(list.sort((a, b) => b - a)[1]);
}
