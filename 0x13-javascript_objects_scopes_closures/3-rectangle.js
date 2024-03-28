#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w === undefined || h === undefined || w <= 0 || h <= 0) {
      return this;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let x = 1; x <= this.height; x++) {
      let rect = '';
      for (let y = 1; y <= this.width; y++) {
        rect += 'X';
      }
      console.log(rect);
    }
  }
}
module.exports = Rectangle;
