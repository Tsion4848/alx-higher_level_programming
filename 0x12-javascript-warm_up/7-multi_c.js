#!/usr/bin/node
let x = process.argv[2];
if (x && isNaN(x) === false) {
	for (let j = 0; j < x; j++) {
		console.log('C id fun')
	}
} else {
	console.log('Missing number of occurrences');
}
