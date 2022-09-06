#!/usr/bin/node
function factorial (x) {
	if (isNaN(n) === true || n ===0) {
		return (1);
	}
	return (n * factorial(n - 1));
}
console.log(factorial(parseInt(process.argv[2],10)));
