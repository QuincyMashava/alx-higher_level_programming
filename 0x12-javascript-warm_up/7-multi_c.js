#!/usr/bin/node

const numArg = parseInt(process.argv[2], 10);

if (isNaN(numArg)){
    console.log("Missing number of occurrences");
}else {
    for ( let count = numArg; numArg > 0; count -= 1){
	console.log("C is fun");
}
}
