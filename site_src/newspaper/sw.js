var __wpo = {"assets":{"main":["/newspaper/60fffb02ec09f5bae95e6454b4750a2b.png","/newspaper/bundle.js","/newspaper/style.css","/newspaper/bundle.js.map","/newspaper/style.css.map","/newspaper/","/newspaper/manifest.json","/newspaper/favicon.ico"],"additional":[],"optional":[]},"externals":[],"hashesMap":{"a9c2edb258b2e6acf43e7eb97f09008784f3f67d":"/newspaper/60fffb02ec09f5bae95e6454b4750a2b.png","3174790fdc19fc1a15bec443507071c9ae27e0f9":"/newspaper/bundle.js","941e19ac183d5d6acdd3a2ca9e8bf004e59e1f1f":"/newspaper/style.css","87c0b7774037ce9ea1cc038f083a857572c716e4":"/newspaper/bundle.js.map","7cc595a5f512c0501ef0288229c0dedeb383f8cd":"/newspaper/style.css.map","17f50d6dd3ef17ebe1d446e749691ea76cee863d":"/newspaper/","7e90a6f89be1ae00a6f5fec87d8eb09f3497a3f9":"/newspaper/manifest.json","5bc4a5adc67e3675fb9ff243dd9d8b095a18976e":"/newspaper/favicon.ico"},"strategy":"changed","responseStrategy":"cache-first","version":"3/23/2017, 5:50:58 PM","name":"webpack-offline","pluginVersion":"4.6.2","relativePaths":false};

(function(n){function e(r){if(t[r])return t[r].exports;var o=t[r]={exports:{},id:r,loaded:!1};return n[r].call(o.exports,o,o.exports,e),o.loaded=!0,o.exports}var t={};return e.m=n,e.c=t,e.p="/newspaper/",e(0)})([function(n,e,t){"use strict";function r(n,e){function t(){if(!L.additional.length)return Promise.resolve();var n=void 0;return n="changed"===y?u("additional"):r("additional"),n.catch(function(n){console.error("[SW]:","Cache section `additional` failed to load")})}function r(e){var t=L[e];return caches.open(E).then(function(e){return g(e,t,{bust:n.version,request:n.prefetchRequest})}).then(function(){s("Cached assets: "+e,t)}).catch(function(n){throw console.error(n),n})}function u(e){return l().then(function(t){if(!t)return r(e);var o=t[0],i=t[1],a=t[2],c=a.hashmap,u=a.version;if(!a.hashmap||u===n.version)return r(e);var f=Object.keys(c).map(function(n){return c[n]}),l=i.map(function(n){var e=new URL(n.url);return e.search="",e.toString()}),h=L[e],d=[],v=h.filter(function(n){return l.indexOf(n)===-1||f.indexOf(n)===-1});Object.keys(R).forEach(function(n){var e=R[n];if(h.indexOf(e)!==-1&&v.indexOf(e)===-1&&d.indexOf(e)===-1){var t=c[n];t&&l.indexOf(t)!==-1?d.push([t,e]):v.push(e)}}),s("Changed assets: "+e,v),s("Moved assets: "+e,d);var p=Promise.all(d.map(function(n){return o.match(n[0]).then(function(e){return[n[1],e]})}));return caches.open(E).then(function(e){var t=p.then(function(n){return Promise.all(n.map(function(n){return e.put(n[0],n[1])}))});return Promise.all([t,g(e,v,{bust:n.version,request:n.prefetchRequest})])})})}function f(){return caches.keys().then(function(n){var e=n.map(function(n){if(0===n.indexOf(W)&&0!==n.indexOf(E))return console.log("[SW]:","Delete cache:",n),caches.delete(n)});return Promise.all(e)})}function l(){return caches.keys().then(function(n){for(var e=n.length,t=void 0;e--&&(t=n[e],0!==t.indexOf(W)););if(t){var r=void 0;return caches.open(t).then(function(n){return r=n,n.match(new URL(P,location).toString())}).then(function(n){if(n)return Promise.all([r,r.keys(),n.json()])})}})}function h(){return caches.open(E).then(function(e){var t=new Response(JSON.stringify({version:n.version,hashmap:R}));return e.put(new URL(P,location).toString(),t)})}function d(n,e,t){return o(t,E).then(function(r){if(r)return r;var o=fetch(n.request).then(function(n){return n.ok?(t===e&&function(){var t=n.clone();caches.open(E).then(function(n){return n.put(e,t)}).then(function(){console.log("[SW]:","Cache asset: "+e)})}(),n):n});return o})}function v(n,e,t){return fetch(n.request).then(function(n){if(n.ok)return n;throw new Error("response is not ok")}).catch(function(){return o(t,E)})}function p(n){return n.catch(function(){}).then(function(n){return n&&n.ok?n:o(_,E)})}function m(){Object.keys(L).forEach(function(n){L[n]=L[n].map(function(n){var e=new URL(n,location);return U.indexOf(n)===-1?e.search="":e.hash="",e.toString()})}),Object.keys(S).forEach(function(n){S[n]=S[n].map(function(n){var e=new URL(n,location);return U.indexOf(n)===-1?e.search="":e.hash="",e.toString()})}),R=Object.keys(R).reduce(function(n,e){var t=new URL(R[e],location);return t.search="",n[e]=t.toString(),n},{}),U=U.map(function(n){var e=new URL(n,location);return e.hash="",e.toString()})}function g(n,e,t){var r=t.allowLoaders!==!1,o=t&&t.bust,a=t.request||{credentials:"omit",mode:"cors"};return Promise.all(e.map(function(n){return o&&(n=i(n,o)),fetch(n,a)})).then(function(o){if(o.some(function(n){return!n.ok}))return Promise.reject(new Error("Wrong response status"));var i=[],a=o.map(function(t,o){return r&&i.push(x(e[o],t)),n.put(e[o],t)});return i.length?function(){var r=c(t);r.allowLoaders=!1;var o=a;a=Promise.all(i).then(function(t){var i=[].concat.apply([],t);return e.length&&(o=o.concat(g(n,i,r))),Promise.all(o)})}():a=Promise.all(a),a})}function x(n,e){var t=Object.keys(S).map(function(t){var r=S[t];if(r.indexOf(n)!==-1&&w[t])return w[t](e.clone())}).filter(function(n){return!!n});return Promise.all(t).then(function(n){return[].concat.apply([],n)})}function O(n){var e=n.url,t=new URL(e),r=void 0;r="navigate"===n.mode?"navigate":t.origin===location.origin?"same-origin":"cross-origin";for(var o=0;o<k.length;o++){var i=k[o];if(i&&(!i.requestTypes||i.requestTypes.indexOf(r)!==-1)){var a=void 0;if(a="function"==typeof i.match?i.match(t,n):e.replace(i.match,i.to),a&&a!==e)return a}}}var w=e.loaders,k=e.cacheMaps,y=n.strategy,q=n.responseStrategy,L=n.assets,S=n.loaders||{},R=n.hashesMap,U=n.externals,W=n.name,b=n.version,E=W+":"+b,P="__offline_webpack__data";m();var j=[].concat(L.main,L.additional,L.optional),_=n.navigateFallbackURL;self.addEventListener("install",function(n){console.log("[SW]:","Install event");var e=void 0;e="changed"===y?u("main"):r("main"),n.waitUntil(e)}),self.addEventListener("activate",function(n){console.log("[SW]:","Activate event");var e=t();e=e.then(h),e=e.then(f),e=e.then(function(){if(self.clients&&self.clients.claim)return self.clients.claim()}),n.waitUntil(e)}),self.addEventListener("fetch",function(n){var e=n.request.url,t=new URL(e),r=void 0;U.indexOf(e)!==-1?r=e:(t.search="",r=t.toString());var o="GET"===n.request.method,i=j.indexOf(r)!==-1,c=r;if(!i){var s=O(n.request);s&&(c=s,i=!0)}if(!i&&o&&_&&a(n.request))return void n.respondWith(p(fetch(n.request)));if(!i||!o)return void(t.origin!==location.origin&&navigator.userAgent.indexOf("Firefox/44.")!==-1&&n.respondWith(fetch(n.request)));var u=void 0;u="network-first"===q?v(n,r,c):d(n,r,c),_&&a(n.request)&&(u=p(u)),n.respondWith(u)}),self.addEventListener("message",function(n){var e=n.data;if(e)switch(e.action){case"skipWaiting":self.skipWaiting&&self.skipWaiting()}})}function o(n,e){return caches.match(n,{cacheName:e}).catch(function(){})}function i(n,e){var t=n.indexOf("?")!==-1;return n+(t?"&":"?")+"__uncache="+encodeURIComponent(e)}function a(n){return"navigate"===n.mode||n.headers.get("Upgrade-Insecure-Requests")||(n.headers.get("Accept")||"").indexOf("text/html")!==-1}function c(n){return Object.keys(n).reduce(function(e,t){return e[t]=n[t],e},{})}function s(n,e){console.groupCollapsed("[SW]:",n),e.forEach(function(n){console.log("Asset:",n)}),console.groupEnd()}r(__wpo,{loaders:{},cacheMaps:[{match:/.*/,to:"/newspaper/",requestTypes:["navigate"]}]}),n.exports=t(1)},function(n,e){}]);