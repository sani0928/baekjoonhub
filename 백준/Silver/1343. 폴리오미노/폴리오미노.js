const filePath = process.platform === "linux" ? '/dev/stdin' : '1343.txt';
let board = require('fs').readFileSync(filePath, 'utf8').toString().trim();

board = board.replaceAll('XXXX', 'AAAA').replaceAll('XX', 'BB');
if (board.includes('X')) {
    console.log(-1)
} else {
    console.log(board)    
};