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

  rotate () {
    const hold = this.height;
    this.height = this.width;
    this.width = hold;
  }

  double () {
    this.height = 2 * this.height;
    this.width = 2 * this.width;
  }
}
module.exports = Rectangle;
