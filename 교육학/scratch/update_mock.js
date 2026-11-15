const fs = require('fs');
let code = fs.readFileSync('g:\\내 드라이브\\ANTI GRAVITY\\시험준비(패턴)\\교육학\\scratch\\test_new_features.js', 'utf8');

code = code.replace("querySelector: function() { return null; },", `querySelector: function() { return null; },
  createElement: function(tag) {
    return {
      style: {},
      innerText: '',
      className: '',
      remove: function() {}
    };
  },`);

fs.writeFileSync('g:\\내 드라이브\\ANTI GRAVITY\\시험준비(패턴)\\교육학\\scratch\\test_new_features.js', code, 'utf8');
