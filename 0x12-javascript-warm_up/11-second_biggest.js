#!/usr/bin/node
let max, num, second;
if (process.argv.length <= 3) {
	console.log(0);
} else {
	for (let i = 2 ; i < process.argv.length ; i++) {
		num = parseInt(process.argv[i], 10);
		if (i === 2) {
			max = num;
		}
		if (num > max) {
			second = max;
			max = num;}
		else {
			second = num;
		}
	}
	console.log(second);
}
