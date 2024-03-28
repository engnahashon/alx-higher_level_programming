#!/usr/bin/node
const newSquare = require('./5-square');

class Square extends newSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let x = 1; x <= this.width; x++) {
        let rect = '';
        for (let y = 1; y <= this.height; y++) {
          rect += c;
        }
        console.log(rect);
      }
    }
  }
}
module.exports = Square;
