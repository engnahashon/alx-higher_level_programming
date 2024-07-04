#!/usr/bin/node
//Script that displays status of code of a GET request
const request = require('request');

const url = process.argv[2];
request.get(url, (error, response, body) => {
		if (error) throw error;
		else {
			console.log('code: ${response.statusCode}');
			}
})
