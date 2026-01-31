const filePath = process.platform === "linux" ? '/dev/stdin' : '1283.txt'
const fs = require('fs')
const input = fs.readFileSync(filePath, 'utf8').trim().split('\n');
const n = parseInt(input[0])
let ans = [];
let selected = new Set();

for (let i = 1; i <= n; i++) {
    const words = input[i].split(' ');
    let res = input[i].trim();
    let end = false;
    
    // 각 단어의 첫번째 알파벳만 탐색
    for (let j = 0; j < words.length; j ++) {
        const str = words[j][0].toUpperCase();
        if (!selected.has(str)) {
            selected.add(str);
            words[j] = '[' + words[j][0] + ']' + words[j].slice(1);
            res = words.join(' ');
            end = true;
            break;
        }
    };
    // 모든 알파벳 탐색
    if (!end) {
        const chars = input[i].trim().split('');
        for (let k = 0; k < chars.length; k++) {
            if (chars[k] === ' ') {
                continue;
            }
            const str = chars[k].toUpperCase();
            if (!selected.has(str)) {
                selected.add(str);
                chars[k] = '[' + chars[k] + ']';
                res = chars.join('');
                break;
            }

        }
    };
    ans.push(res);
};

ans.forEach(element => {
    console.log(element)
});