#!/usr/bin/node
const x = process.argv[2];
let z = 'x';
if (x && isNaN(x) === false) {
	for (let i = 0; i < x ; i++) {
		console.log(z.repeat(x));
	}
} else {
	console.log('Missing size');
}
