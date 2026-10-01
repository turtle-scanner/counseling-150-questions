import os
import json

base_dir = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook'

manifest = {
  "name": "2027 KICE 55제 암기장",
  "short_name": "KICE 55제",
  "start_url": "./kice_55_core_compressed.html",
  "display": "standalone",
  "background_color": "#161a23",
  "theme_color": "#161a23",
  "icons": [
    {
      "src": "images/go1.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "images/go1.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ]
}

with open(os.path.join(base_dir, 'manifest.json'), 'w', encoding='utf-8') as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)

sw_content = """
const CACHE_NAME = 'kice-55-v1';
const urlsToCache = [
  './kice_55_core_compressed.html',
  './manifest.json',
  './images/go1.png',
  './images/go2.jpg',
  './images/go3.png',
  './images/go4.jpg',
  './images/go5.jpg',
  './images/cheer3.jpg'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  );
});
"""

with open(os.path.join(base_dir, 'sw.js'), 'w', encoding='utf-8') as f:
    f.write(sw_content)

print("PWA files created.")
