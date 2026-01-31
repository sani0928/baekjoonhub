const filePath = process.platform === "linux" ? '/dev/stdin' : '1427.txt'
const input = require('fs').readFileSync(filePath, 'utf8').trim().split('');
const ans = input.map(Number).sort((a, b) => b - a).join('');
console.log(ans);