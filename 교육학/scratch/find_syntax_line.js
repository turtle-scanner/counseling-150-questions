const fs = require('fs');

const code = fs.readFileSync('scratch/extracted_script_2.js', 'utf8');
const lines = code.split('\n');

console.log(`Total lines: ${lines.length}`);

// Let's test chunks or parse with vm
const vm = require('vm');
try {
  new vm.Script(code);
  console.log('Script parsed successfully!');
} catch (err) {
  console.error('Detailed Error:');
  console.error(err.message);
  console.error(err.stack);
}
