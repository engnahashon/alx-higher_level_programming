#!/usr/bin/node

const num = process.argv[2];
if (isNaN(num) || undefined) {
  console.log('Missing size');} else {
	  let x = 0;
	  while (x < num) {
	  let y = 0;
	  let row = ''
	  while (y < num) {
		  row += 'X'
		  y++;
	  }
	  console.log(row);
	  x++;
  }
  }
