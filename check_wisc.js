const fs = require('fs');
const data = JSON.parse(fs.readFileSync('교육학/scratch/top55_extracted.json', 'utf8'));

data.forEach((item, idx) => {
  if (item.question.includes('K-WISC-V') || item.question.includes('웩슬러')) {
    console.log('Index:', idx, 'ID:', item.id, 'Code: C' + (idx + 1));
    console.log('Q:', item.question);
    console.log('KW:', item.keyword);
    console.log('A:', item.answer);
    console.log('-------------------------------------------');
  }
});
