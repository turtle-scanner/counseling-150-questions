# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='backslashreplace')
html = open(r'C:\Users\LENOVO\Desktop\sam3_update.html', 'r', encoding='utf-8', errors='ignore').read()
pos = html.rfind('</script>')
after = html[pos:]
print('Length after </script>:', len(after))
modals_after = re.findall(r'<div[^>]*id=["\']([^"\']+)["\']', after)
print('Modals/divs with id after </script>:', modals_after[:30])
