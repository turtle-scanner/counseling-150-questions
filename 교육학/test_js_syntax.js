const fs = require('fs');
const path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/index.html';

const html = fs.readFileSync(path, 'utf8');

// Extract script tag content
const scriptMatch = html.match(/<script>([\s\S]*?)<\/script>/);
if (!scriptMatch) {
  console.error('No script tag found!');
  process.exit(1);
}

const jsCode = scriptMatch[1];
console.log('Extracted JS code length:', jsCode.length);

try {
  // Test parsing via Function constructor or vm
  const vm = require('vm');
  const script = new vm.Script(jsCode);
  console.log('✅ JS Syntax check passed with 0 errors!');
} catch (err) {
  console.error('❌ JS Syntax error:', err);
  process.exit(1);
}
