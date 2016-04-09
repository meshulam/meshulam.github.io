---
layout: post
title: Amusing myself with basic Javascript
date: '2013-01-26 18:25:34'
---


<div class="wp-caption aligncenter" id="attachment_932" style="width: 560px">[![Just look at that URL. Madness!](http://res.cloudinary.com/meshulam/image/upload/h_149,w_550/v1437619278/Screen-Shot-2013-01-25-at-11.47.36-PM1_btmwma.png)](http://res.cloudinary.com/meshulam/image/upload/v1437619278/Screen-Shot-2013-01-25-at-11.47.36-PM1_btmwma.png)Just look at that URL. Madness!

</div>Call me crazy, but ever since I noticed the random 32-letter ID's for apps in Google Chrome Web Store URLs (see above), I can't help but imagine pronouncing them in my head. The thought of someone actually trying to read off the nonsensical URL is almost unbearably hilarious to me for some reason. It's just one of those weird things I do to keep myself entertained.

So today I decided to take it one step further. I made a bookmarklet that uses Google Translate's text-to-speech engine to get a real robotic pronunciation of the letters in a URL. Naturally it uses the Italian robot voice because it's the funniest one I found. Want to hear the results?

1. Drag the following link to your bookmarks bar. [URL Pronouncer](javascript:(function(){ var s=location.href.replace(/[^A-Za-z]/g,'');var url='http://translate.google.com/translate_tts?ie=UTF-8&tl=it&q='+s; console.log(url); var a=document.createElement('audio');a.setAttribute('src',url);a.play();}()))
2. Go to a page on the Chrome store, like [this one](https://chrome.google.com/webstore/detail/google-maps/lneaknkopdijkpnocmklfnjbeapigfbh?utm_source=chrome-ntp-icon).
3. Click the bookmark you just added.

I've tested this on Chrome and Safari and it might not work on Firefox.

It sometimes works on other websites but not all the time, probably because of some restrictions on Google's side. If you know what the problem might be, let me know.

This useless little project is also the [first thing I've uploaded to GitHub](https://gist.github.com/4643405).


