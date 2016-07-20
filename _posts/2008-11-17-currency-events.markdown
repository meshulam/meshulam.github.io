---
title: Currency events
date: '2008-11-17 15:58:06'
---


In December, I will be going to Israel for ten days. I recently thought to take a look at the exchange rate to see if the dollar has gotten any stronger since the summer, when some of my friends were busy getting poor in Europe:

{% include _image.html img="2008-11-17-exchangerate_pxrkgw.png" title="exchangerate"  %}
Not too bad. It's not quite where it was two years ago, but it looks like the summer really was the worst of it. Also, it seems like it's been pretty volatile lately, what with the global financial crisis and all. So naturally, that got me to thinking: Would it be a worthwhile gamble to invest in foreign currency, speculating on the dollar drastically losing value?

I know it's possible to invest in currency from the comfort of your own country, but just for fun I wondered what the odds would be of profiting during my trip abroad. Simply put, if I buy Shekels the day I get to Israel, and sell them the day I leave, what would be my expected return?

I got the past two years of USD-to-ILS exchange rate data from [Oanda.com,](http://www.oanda.com/convert/fxhistory) which has a very nice interface for historical currency data. I assumed a 2% premium when exchanging currency, approximately what your credit card company charges. I brought the data into Matlab and made a pretty picture:

{% include _image.html img="2008-11-17-matlabgraph1_hfzhdz.png" title="matlabgraph1"  %}
As expected, it is highly likely that I would lose money because of the 4% in exchange fees (two transactions: USD-to-ILS and back). Sure enough, the red dotted line indicating the average return is pretty close to 0.96. But there have been a few peaks over 1, indicating a net profit. All of these have occurred in the last year when the economy has been going crazy. In the past two years, there were twenty instances where it was profitable to hold Shekels for ten consecutive days. This translates to about a 3% win rate, which is not very encouraging. Furthermore, the highest-ever return was 1.023, netting just above two cents per dollar invested.

The bottom line is that it may make sense to make long term investments in foreign currency (or stock) as a hedge against the U.S. economy, but the exchange premiums make it pointless to try beating the market on a shorter scale.


