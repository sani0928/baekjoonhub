const filePath = process.platform === "linux" ? '/dev/stdin' : '1343.txt';
const board = require('fs').readFileSync(filePath, 'utf8').trim().split('').concat(['.']);

let s = 0;
let success = true;

for (let i = 0; i < board.length; i++) {
    if (s == 4) {
        for (let j = i - 4; j < i; j++) {
            board[j] = 'A'
        };
        s = 0
    };
    if (board[i] == 'X') {
        s += 1
    } else {
        if (s == 4) {
            for (let j = i - 4; j < i; j++) {
                board[j] = 'A'
            }
        } else if (s == 2) {
            for (let j = i - 2; j < i; j++) {
                board[j] = 'B'
            }
        } else if (s == 1 || s == 3) {
            success = false;
            break;
        }
        s = 0
    };
};

if (success) {
    console.log(board.slice(0, -1).join(''))
} else {
    console.log(-1)
};