const filePath = process.platform === "linux" ? '/dev/stdin' : '2512.txt'
const input = require('fs').readFileSync(filePath, 'utf8').trim().split('\n');
N = parseInt(input[0]);
states = input[1].split(' ').map(Number);
M = parseInt(input[2]);

let mn = 0;
let mx = Math.max(...states);
while (mn <= mx) {
    const mid = Math.floor((mn + mx) / 2);
    let total = 0;
    states.forEach(state => {
        total += Math.min(state, mid)
    });

    if (total <= M) {
        mn = mid + 1
    } else {
        mx = mid - 1
    };
};

console.log(mx)