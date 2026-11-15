const fs = require('fs');
const vm = require('vm');

let bm = fs.readFileSync('build_master.js', 'utf8');

// Replace the validation block in build_master.js so it catches and prints the exact line with error
const oldValidation = `// 4. Validate script syntax
const scriptMatch = htmlTemplate.match(/<script>([\\s\\S]*?)<\\/script>/);
if (scriptMatch) {
  try {
    new Function(scriptMatch[1]);
    console.log('✅ JAVASCRIPT SYNTAX VALIDATED PERFECTLY! Zero errors!');
  } catch (err) {
    console.error('❌ JS Syntax Error detected:', err);
    process.exit(1);
  }
}`;

const newValidation = `// 4. Validate script syntax
const scriptMatch = htmlTemplate.match(/<script>([\\s\\S]*?)<\\/script>/);
if (scriptMatch) {
  try {
    new vm.Script(scriptMatch[1]);
    console.log('✅ JAVASCRIPT SYNTAX VALIDATED PERFECTLY! Zero errors!');
  } catch (err) {
    console.error('❌ JS Syntax Error detected:', err);
    process.exit(1);
  }
}`;

if (bm.includes(oldValidation)) {
  bm = bm.replace(oldValidation, newValidation);
  fs.writeFileSync('build_master.js', bm, 'utf8');
  console.log('Updated validation to vm.Script');
} else {
  console.log('oldValidation block not found');
}
