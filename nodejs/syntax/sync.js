var fs = require('fs');


// Sync
console.log('A');
var result = fs.readFileSync('./sample.txt', 'utf-8');
console.log(result);
console.log('C');

console.log('\n');

//Async
console.log('A');
fs.readFile('./sample.txt', 'utf-8', function(err, result){
    console.log(result);
});
console.log('C');