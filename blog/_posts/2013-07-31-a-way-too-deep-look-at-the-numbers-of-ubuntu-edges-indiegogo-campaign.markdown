---
layout: post
title: A way-too-deep look at Ubuntu Edge's Indiegogo numbers
date: '2013-07-31 16:07:58'
---


**TL;DR: Prospective Ubuntu Edge buyers are ridiculously sensitive to changes in pricing.**

If you follow tech news you've probably heard quite a bit about [Ubuntu's crowdfunding campaign](http://www.indiegogo.com/projects/ubuntu-edge--35), which is trying to raise $32 million to build a cutting-edge smartphone called the Ubuntu Edge. In the 9 days since the campaign began, there's been a lot of speculation on whether it will fall short of its all-or-nothing funding target. One site, [ubuntu-edge.info](http://ubuntu-edge.info/), shows the amount raised over time:

[![ubuntu1](http://res.cloudinary.com/meshulam/image/upload/h_317,w_550/v1437619278/ubuntu1_ioxjxm.png)](http://res.cloudinary.com/meshulam/image/upload/v1437619278/ubuntu1_ioxjxm.png)

Judging from the red on-target line, they aren't looking too good. But that's boring. Let's take a closer look at the rate of the funding so far:

[![ubuntu2](http://res.cloudinary.com/meshulam/image/upload/h_223,w_550/v1437619277/ubuntu2_rrw6nr.png)](http://res.cloudinary.com/meshulam/image/upload/v1437619277/ubuntu2_rrw6nr.png) The weird shape is at least partially due to Ubuntu's pricing scheme. They began the campaign with two price levels: a limited number of units for $600, and the rest being sold for $830. Then, after a few days, they introduced limited quantities available at lower price points: $625, $675, $725, $775, $780, etc. [See here](http://images.indiegogo.com/file_attachments/2991/files/20130724034144-IndieGogo_Perk-list_72.png) for the full distribution.

What struck me from looking at this graph is how clearly you can see the slope changing when a price level sold out. I speculated the story looked like this:

[![ubuntu3](http://res.cloudinary.com/meshulam/image/upload/h_223,w_550/v1437619277/ubuntu3_ld0ffy.png)](http://res.cloudinary.com/meshulam/image/upload/v1437619277/ubuntu3_ld0ffy.png)

Fortunately, we don't need to rely on our eyeballs when there's data involved; the dataset is available from the site above if you know where to look. I manually picked a single point around each of the kinks I observed and put them into Excel, since I'm not cool enough to use R for this kind of thing.

First I wanted to confirm that the funds raised in each time interval roughly equaled the corresponding price level*available quantity. It's not going to be exact since there are some other contribution levels (e.g. $20 just to support them, $10,000 if you are rich and like having Limited Edition things), but most of the money is coming from people just wanting to preorder a phone so this will get us in the ballpark.

[![ubuntu4](http://res.cloudinary.com/meshulam/image/upload/h_173,w_550/v1437619277/ubuntu4_hu5jru.png)](http://res.cloudinary.com/meshulam/image/upload/v1437619277/ubuntu4_hu5jru.png)

For each interval I drew on the graph above, I took the ending timestamp and cumulative amount raised (columns A and C) from ubuntu-edge.info. By subtracting each dollar amount from the previous row, I got the amount raised per interval (column D). Then I entered the cheapest price level at each time and the quantity available, assuming my hypothesis was correct. Note that we don't know how many suckers bought the $830 device before Ubuntu added lower price tiers, but they did state that the "hundreds" of them would get a refund for the difference.

For the rest of the time intervals, we can easily calculate the amount we expected to raise assuming all revenue came from the cheapest presale price level (column I). Then we can see the amount (column J) and percentage (column K) that this estimate differs from the actual amount. Our initial model is actually a really good fit; the first three intervals we have error %'s for are hovering at 5%. Without looking at the numbers, it feels about right that 5% of the revenue is coming from altruistic contributions.

Before going any further I want to point out that the math is actually a little fuzzier than it looks. There's nothing to stop someone from buying a more expensive phone when a cheaper level is still available, thus throwing off our Quantity column. Indeed we can see this is happening on the campaign site, since 34 phones have been bought for $830 even with the lower prices available. But we're just going for ballpark numbers here, and the ballpark looks about right.

Since intervals 1, 3, and 4 all have a deviation remarkably close to 5%, let's assume the same holds true for the time period when just the $830 phone was available. To get column K to result in a value of ~5%, there must have been about 740 suckers:

[![ubuntu5](http://res.cloudinary.com/meshulam/image/upload/h_170,w_550/v1437619277/ubuntu5_lsvhyt.png)](http://res.cloudinary.com/meshulam/image/upload/v1437619277/ubuntu5_lsvhyt.png)

 

But what's going on with our error during the $725 and $775 periods? We shoot up to 14% and then 25%. Did people suddenly start buying $10k phones? Did we miss the real points when the price levels sold out?

Actually, there's an explanation. When introducing the new price levels during the campaign, Ubuntu also added a "Double Edge" deal, where you can preorder two phones for $1400. Which works out to $700 apiece. Which just happens to be a worse deal than the $675 level but a better deal than the $725 level. So naturally, when the $675 phones sold out, the Double Edge started to get picked up. Let's keep calibrating our model to a 5% altruism rate and solve for the # of units sold as a double deal:

[![ubuntu6](http://res.cloudinary.com/meshulam/image/upload/h_153,w_550/v1437619276/ubuntu6_wcunit.png)](http://res.cloudinary.com/meshulam/image/upload/v1437619276/ubuntu6_wcunit.png)

 

Note that the equation for column I has changed to account for the new component.

Our model estimates that 414 phones (207 units) have been sold as doubles. When I grabbed this data, the actual total was 264 double packs. Not terribly far off.

Finally, let's look at the rate of unit sales during each interval to get a feel for price elasticity and the effect of time. It's pretty obvious that sales slowed down after the initial cheap phones ran out, and we can see a distinct slope change when each subsequent level was depleted, so we know there's some correlation with price. We also know that sales are probably going to be faster at the beginning when there's more hype and will slow down after that, at least until it gets very close to the end of the campaign.

[![ubuntu7](http://res.cloudinary.com/meshulam/image/upload/h_177,w_550/v1437619231/ubuntu7_eblkma.png)](http://res.cloudinary.com/meshulam/image/upload/v1437619231/ubuntu7_eblkma.png)

Column B is just each timestamp subtracted from the previous. Column H is what we're interested in: total unit sales (cheapest single price level+doubles) normalized over time.

I'm staggered by how much price affects the rate of sales. After the initial $600 level sold out, sales trickled in at just 6% of their previous velocity. **When the price went from $625 to $675, only an 8% increase, the rate slowed by almost 60%**. This corresponds to a crazy-high [price elasticity of demand](http://en.wikipedia.org/wiki/Price_elasticity_of_demand) of 7.3. Any way you cut it, prospective Ubuntu Edge buyers are ridiculously price-sensitive.

What about the effect of time? Early on in the campaign a $830 price point yielded a sales rate of 23.6 units/hour. Later on, this rate was crossed again when the price went up from $725 to $775. Let's split the difference and speculate that if the price only increased to $750, the sales rate would have once again hit exactly 23.6.

This would mean that the passage of 3.5 days (from the start of the $830 interval to the start of the $775 interval) has about the same effect on sales as increasing the price by $80 (9.6%).

Of course it's hard to conclude anything from this limited set of data. But perhaps these observations can inspire future crowdfunding projects to experiment with different pricing schemes. Personally, I like the idea of surprise price *decreases*. You can recapture some of the natural time decay as the campaign goes on, and whoever does this first could get some extra media coverage as well. But it may not be worth it if your early adopters feel like they got screwed.


