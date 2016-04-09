---
layout: post
title: Interesting bug in Google Translate
date: '2012-11-05 21:04:50'
---


Since moving to Sweden, I've been using Google Translate quite a bit. I recently noticed a weird glitch where it would "translate" currencies, but only occasionally. Seems it has to do with the formatting of the amount:

[Looks ok:](http://translate.google.com/?hl=en&sl=sv&tl=en&vi=c#sv/en/1250%20SEK)

[![](http://res.cloudinary.com/meshulam/image/upload/v1437619326/Screen-Shot-2012-11-05-at-9.57.57-PM_qb88wx.png "Screen Shot 2012-11-05 at 9.57.57 PM")](http://res.cloudinary.com/meshulam/image/upload/v1437619326/Screen-Shot-2012-11-05-at-9.57.57-PM_qb88wx.png) [  
](http://blog.meshul.am/blog/wp-content/uploads/2012/11/Screen-Shot-2012-11-05-at-9.51.50-PM.png)

[Wrong:](http://translate.google.com/?hl=en&sl=sv&tl=en&vi=c#sv/en/1%2C250.00%20SEK)

[![](http://res.cloudinary.com/meshulam/image/upload/v1437619326/Screen-Shot-2012-11-05-at-9.56.57-PM_ayrnoo.png "Screen Shot 2012-11-05 at 9.56.57 PM")](http://res.cloudinary.com/meshulam/image/upload/v1437619326/Screen-Shot-2012-11-05-at-9.56.57-PM_ayrnoo.png)

[Differently wrong:](http://translate.google.com/?hl=en&sl=sv&tl=en&vi=c#sv/en/1250.0%20SEK)

[![](http://res.cloudinary.com/meshulam/image/upload/h_146,w_550/v1437619327/Screen-Shot-2012-11-05-at-9.55.54-PM_ay8ddj.png "Screen Shot 2012-11-05 at 9.55.54 PM")](http://res.cloudinary.com/meshulam/image/upload/v1437619327/Screen-Shot-2012-11-05-at-9.55.54-PM_ay8ddj.png)

[And again:](http://translate.google.com/?hl=en&sl=sv&tl=en&vi=c#sv/en/1%2C250.0%20SEK)

[![](http://res.cloudinary.com/meshulam/image/upload/v1437619325/Screen-Shot-2012-11-05-at-10.00.20-PM_o5lpow.png "Screen Shot 2012-11-05 at 10.00.20 PM")](http://res.cloudinary.com/meshulam/image/upload/v1437619325/Screen-Shot-2012-11-05-at-10.00.20-PM_o5lpow.png)

[And my favorite:](http://translate.google.com/?hl=en&sl=sv&tl=en&vi=c#sv/en/1250.%20SEK)

[![](http://res.cloudinary.com/meshulam/image/upload/v1437619325/Screen-Shot-2012-11-05-at-10.01.18-PM_e845st.png "Screen Shot 2012-11-05 at 10.01.18 PM")](http://res.cloudinary.com/meshulam/image/upload/v1437619325/Screen-Shot-2012-11-05-at-10.01.18-PM_e845st.png)

Made me do a double take when I was on a translated website that showed an outrageous price in USD.

 


