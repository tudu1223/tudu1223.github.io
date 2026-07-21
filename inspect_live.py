import re
with open(r'D:\bloh\blog\tmp_live.html', 'r', encoding='utf-8') as f:
    h = f.read()
print('=== col-span-4 inner (length and preview) ===')
m = re.search(r'<div class="md:col-span-4[^>]*>(.*?)<div class="md:col-span-8', h, re.DOTALL)
if m:
    inner = re.sub(r'<svg.*?</svg>', '', m.group(1), flags=re.DOTALL)
    inner = re.sub(r'<[^>]+>', ' ', inner)
    inner = re.sub(r'\s+', ' ', inner).strip()
    print('len:', len(inner))
    print(inner)
else:
    print('no col-span-4 found')

print()
print('=== col-span-8 inner (length only) ===')
m = re.search(r'<div class="md:col-span-8[^>]*>(.*?)<!--', h, re.DOTALL)
if m:
    inner = re.sub(r'<svg.*?</svg>', '', m.group(1), flags=re.DOTALL)
    inner = re.sub(r'<[^>]+>', ' ', inner)
    inner = re.sub(r'\s+', ' ', inner).strip()
    print('len:', len(inner))
    print(inner[:300])
