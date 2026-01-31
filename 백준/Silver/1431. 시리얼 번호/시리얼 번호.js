function sumOnlyNums(str) {
    let total_sum = 0;
    for (let char of str) {
        if (char > '0' && char <= '9') {
            total_sum += parseInt(char);
        }
    }
    return total_sum
}

const filePath = process.platform === "linux" ? '/dev/stdin' : '1431.txt'
const input = require('fs').readFileSync(filePath, 'utf8').trim().split('\n');
const n = parseInt(input[0]);

info = [];
for (let i = 1; i <= n; i++) {
    info.push([input[i].length, sumOnlyNums(input[i]), input[i]]);
}
info.sort((a, b) => {
    if (a[0] !== b[0]) return a[0] - b[0];
    if (a[1] !== b[1]) return a[1] - b[1];
    return a[2].localeCompare(b[2]);
});

for (ans of info) {
    console.log(ans[2])
};