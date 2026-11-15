// -*- coding: utf-8 -*-
const fs = require('fs');

const html = fs.readFileSync('C:\\Users\\LENOVO\\Desktop\\삼국지_황제의결단_웹게임.html', 'utf8');

// Extract all <script> contents
const regex = /<script\b[^>]*>([\s\S]*?)<\/script>/gi;
let match;
let count = 0;

while ((match = regex.exec(html)) !== null) {
  count++;
  const scriptContent = match[1];
  const filename = `scratch/extracted_script_${count}.js`;
  fs.writeFileSync(filename, scriptContent, 'utf8');
  console.log(`Saved ${filename} (length: ${scriptContent.length})`);
  
  // Syntax check with node
  try {
    new Function(scriptContent);
    console.log(`Script ${count}: Syntax OK!`);
  } catch (err) {
    console.error(`Script ${count}: SYNTAX ERROR!`, err.message);
    console.error(err.stack);
  }
}
