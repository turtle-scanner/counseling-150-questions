const fs = require('fs');

const code = fs.readFileSync('scratch/extracted_script_2.js', 'utf8');
const lines = code.split('\n');

for (let i = 1930; i <= 1955; i++) {
  console.log(`${i}: ${lines[i - 1]}`);
}
