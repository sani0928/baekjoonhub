const filePath = process.platform === "linux" ? '/dev/stdin' : '2752.txt';
const fs = require('fs');
let input = fs.readFileSync(filePath, 'utf8').trim().split(' ').map(Number);
input.sort((a, b) => a - b);
console.log(input.join(' '));