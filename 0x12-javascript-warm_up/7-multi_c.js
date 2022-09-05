#!/usr/bin/node
const x = process.argv[2];
if (x && isNaN(x) === false) {
	for (let j = 0; j < x; j++) {
		console.log('C is fun');
	}
} else {
	console.log('Missing number of occurrences');
}
