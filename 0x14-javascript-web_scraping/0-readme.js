#!/usr/bin/node
//Script that read contents of a file
const fs = require('fs');

const filename = process.argv[2];
fs.readFile(filename, 'utf-8', (err, data) => {
	if (err) throw err;
		console.log(data.toString());
})
