const fs = require('fs');
const top55 = JSON.parse(fs.readFileSync('교육학/scratch/top55_extracted.json', 'utf8'));

top55.slice(0, 37).forEach((item, idx) => {
  const isPed = item.type === 'pedagogy';
  const code = (isPed ? 'P' : 'C') + String(idx + 1).padStart(2, '0');
  let cleanAns = item.clean_ans || item.answer || '';
  cleanAns = cleanAns.replace(/<[^>]*>/g, '').trim();

  console.log('[' + code + '] [' + item.id + ']');
  console.log('  Q:', item.question);
  console.log('  KW:', item.keyword);
  console.log('  A:', cleanAns);
  console.log('----------------------------------------------------');
});
