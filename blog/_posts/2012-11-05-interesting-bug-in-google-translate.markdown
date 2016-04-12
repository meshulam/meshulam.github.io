---
layout: post
title: Interesting bug in Google Translate
date: '2012-11-05 21:04:50'
---


Since moving to Sweden, I've been using Google Translate quite a bit. I recently noticed a weird glitch where it would "translate" currencies, but only occasionally. Seems it has to do with the formatting of the amount:

[Looks ok:](http://translate.google.com/?hl=en&sl=sv&tl=en&vi=c#sv/en/1250%20SEK)
{% include _image.html img="2012-11-05-Screen-Shot-2012-11-05-at-9.57.57-PM_qb88wx.png" title="Screen Shot 2012-11-05 at 9.57.57 PM"  %}

[Wrong:](http://translate.google.com/?hl=en&sl=sv&tl=en&vi=c#sv/en/1%2C250.00%20SEK)
{% include _image.html img="2012-11-05-Screen-Shot-2012-11-05-at-9.56.57-PM_ayrnoo.png" title="Screen Shot 2012-11-05 at 9.56.57 PM"  %}

[Differently wrong:](http://translate.google.com/?hl=en&sl=sv&tl=en&vi=c#sv/en/1250.0%20SEK)
{% include _image.html img="2012-11-05-Screen-Shot-2012-11-05-at-9.55.54-PM_ay8ddj.png" lightbox_img="2012-11-05-Screen-Shot-2012-11-05-at-9.55.54-PM_ay8ddj.png" title="Screen Shot 2012-11-05 at 9.55.54 PM"  %}

[And again:](http://translate.google.com/?hl=en&sl=sv&tl=en&vi=c#sv/en/1%2C250.0%20SEK)
{% include _image.html img="2012-11-05-Screen-Shot-2012-11-05-at-10.00.20-PM_o5lpow.png" title="Screen Shot 2012-11-05 at 10.00.20 PM"  %}

[And my favorite:](http://translate.google.com/?hl=en&sl=sv&tl=en&vi=c#sv/en/1250.%20SEK)
{% include _image.html img="2012-11-05-Screen-Shot-2012-11-05-at-10.01.18-PM_e845st.png" title="Screen Shot 2012-11-05 at 10.01.18 PM"  %}

Made me do a double take when I was on a translated website that showed an outrageous price in USD.

 


