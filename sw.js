/* Bad Kreuznach City Walk — offline service worker
   Precaches EVERYTHING on install, serves cache-first,
   and answers HTTP Range requests from cache (required for
   audio playback on iOS Safari while offline). */

const CACHE_NAME = 'bad-kreuznach-walk-v3';

const ASSETS = [
  './',
  './index.html',
  './manifest.json',
  './assets/fonts/bricolage.woff2',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './icons/apple-touch-icon.png',
  './icons/icon-maskable-512.png',
  './assets/img/brueckenhaeuser.webp',
  './assets/img/kauzenburg.webp',
  './assets/img/kurpark.webp',
  './assets/img/nikolaus.webp',
  './assets/img/oranienpark.webp',
  './assets/img/paulus.webp',
  './assets/img/roemerhalle.webp',
  './assets/img/roseninsel.webp',
  './assets/img/salinen.webp',
  './assets/img/stift.webp',
  './assets/img/venedig.webp',
  './assets/audio/willkommen.mp3',
  './assets/audio/salinental.mp3',
  './assets/audio/roseninsel.mp3',
  './assets/audio/oranienpark.mp3',
  './assets/audio/kurpark.mp3',
  './assets/audio/pauluskirche.mp3',
  './assets/audio/brueckenhaeuser.mp3',
  './assets/audio/klein-venedig.mp3',
  './assets/audio/eiermarkt.mp3',
  './assets/audio/roemerhalle.mp3',
  './assets/audio/kauzenburg.mp3',
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      // cache:'reload' bypasses the browser HTTP cache, so a new SW version
      // always precaches the freshest files from the server
      .then(cache => cache.addAll(ASSETS.map(u => new Request(u, { cache: 'reload' }))))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys()
      .then(keys => Promise.all(
        keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k))
      ))
      .then(() => self.clients.claim())
  );
});

/* Page asks "how much is saved?" — reply with progress. */
self.addEventListener('message', event => {
  if (event.data && event.data.type === 'STATUS') {
    caches.open(CACHE_NAME)
      .then(cache => cache.keys())
      .then(keys => {
        event.ports[0].postMessage({ cached: keys.length, total: ASSETS.length });
      });
  }
});

/* Serve a partial (206) response from a fully cached body. */
async function rangeResponse(request, response) {
  const rangeHeader = request.headers.get('range');
  const match = /bytes=(\d+)-(\d*)/.exec(rangeHeader);
  if (!match) return response;
  const buffer = await response.arrayBuffer();
  const size = buffer.byteLength;
  const start = Number(match[1]);
  const end = match[2] ? Math.min(Number(match[2]), size - 1) : size - 1;
  return new Response(buffer.slice(start, end + 1), {
    status: 206,
    statusText: 'Partial Content',
    headers: {
      'Content-Type': response.headers.get('Content-Type') || 'application/octet-stream',
      'Content-Range': `bytes ${start}-${end}/${size}`,
      'Content-Length': String(end - start + 1),
      'Accept-Ranges': 'bytes',
    },
  });
}

self.addEventListener('fetch', event => {
  const request = event.request;
  if (request.method !== 'GET') return;

  event.respondWith((async () => {
    const cache = await caches.open(CACHE_NAME);
    // ignoreSearch: tolerate cache-busting query strings
    const cached = await cache.match(request, { ignoreSearch: true });
    if (cached) {
      if (request.headers.has('range')) return rangeResponse(request, cached);
      return cached;
    }
    try {
      return await fetch(request);
    } catch (err) {
      // offline navigation fallback
      if (request.mode === 'navigate') {
        const index = await cache.match('./index.html');
        if (index) return index;
      }
      throw err;
    }
  })());
});
