const filePath = process.platform === "linux" ? '/dev/stdin' : '8958.txt'
const input = require('fs').readFileSync(filePath, 'utf8').trim().split('\n');
const t = Number(input[0]);

for (let i = 1; i <= t; i++) {
    const arr = input[i].trim()
    let score = 0
    let serial = 0 
    for (str of arr) {
        if (str == 'O') {
           serial++;
           score += serial; 
        } else {
            serial = 0;
        }
    }
    console.log(score)
}