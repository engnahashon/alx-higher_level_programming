#!/usr/bin/node
//Script that writes to a file
const fs = require('fs');

const filename = process.argv[2];
const input = process.argv[3];

fs.writeFile(filename, input, 'utf-8', (err) => {
	if (err) throw err;
})
