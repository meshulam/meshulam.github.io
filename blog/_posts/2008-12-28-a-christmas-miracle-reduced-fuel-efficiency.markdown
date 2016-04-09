---
layout: post
title: A Christmas miracle! Reduced fuel efficiency!
date: '2008-12-28 00:42:18'
---


As my tires were spinning out in the snow for the dozenth time, I wondered if there is a significant reduction in fuel efficiency in the winter months. It seems like there should be a pretty sizeable effect: When it's cold, people idle their cars longer, they drive slower, and any snow or ice makes for a less-than-optimal tire-to-road interface. Since I've been doing quite a bit of nothing since I've been home for break, I took it upon myself to find out the answer, with a little help from some of my favorite federal government agencies.

The question I focused on was, "is there a change in average miles-per-gallon as temperature changes?" I could have looked against precipitation levels, or something else, but for now I figured to stay with just temperature. I picked a handful of U.S. states over a range of climates to partially control for any seasonal effects.

**Data sources**

I got monthly state-by-state breakdowns of petroleum product sales from the [Department of Energy](http://tonto.eia.doe.gov/dnav/pet/pet_cons_prim_dcu_nus_m.htm). The number I decided to use was the total for motor gasoline, which includes unleaded, premium, etc. but not diesel fuel. I chose to omit diesel since it is used for much more than just trucks, and it would be unreasonable to expect an accurate absolute "miles per gallon" number anyway. My goal was to see how personal auto efficiency changes with temperature, and as long as there are no drastic changes in the number of trucks and other diesel-powered vehicles on the road, the trends will still come through.

Now that we took care of the "per gallon" part, we need the "miles driven" that goes up in the numerator. For that I used Table 5 of the Federal Highway Administration's [Traffic Volume Trends](http://www.fhwa.dot.gov/ohim/tvtw/tvtpage.cfm) data. This data uses a sensor network across the interstate highway system as well as some dubious statistical witchcraft to estimate how many million miles were driven on *all roads* in each state each month. As far as I could tell, this includes commercial traffic like those diesel trucks I mentioned above, but again we're not going after a literal miles-per-gallon number so this won't be reflected in the trends. I didn't get the best feeling from this data, since there were often some pretty drastic month-to-month changes in miles driven, but I take whatever data I can get. The numbers I used for each month were taken from the following year's report, which goes back and adjusts the numbers to agree with other, more reliable, highway data. I'm not sure it was the right decision, but they weren't too different so I'm not going to sweat it.

Finally, I got monthly mean average temperature data from [Weather Underground](http://www.wunderground.com/) (not to be confused with the other Weather Underground). This takes the average of the high and low temperatures each day of the month and averages them. I figured this was the simplest measure of the temperature over an entire month. The temperatures for each state were taken near the state's center of population, but I tried to stay away from large, climatologically diverse states like California.

The states I used were: Minnesota, Wisconsin, Ohio, and Georgia. This group reflects a range of climates to control for strictly seasonal effects. Furthermore, the states are relatively uniform in climate (no mountainous states were chosen for this reason).

**Results**

About 24 months of data were taken for each state (some months had incomplete data). An estimated miles per gallon was calculated and the median for each state was taken as a baseline measure. For each month, the deviation from the state median efficiency was plotted against its temperature:

{% include _image.html img="2008-12-28-mpgtemp_ejmqp4.gif" caption="mpgtemp" title="mpgtemp"  %}
Although the variance is somewhat high due to the approximations taken, there is a significant downward trend with decreasing temperature below about 40 degrees. As it goes from 40 to 20 degrees Fahrenheit, you lose about two miles per gallon, on the order of 10%. The quadratic trendline gave by far the best fit, with an R-squared of almost exactly 0.5. Note that the trendline indicates a slight dropoff in fuel efficiency with very high temperatures, but I'd need to throw some southwestern states in to see if that trend holds up.

No posts for about a week and a half; I'll be [in Israel](http://blog.meshul.am/2008/11/currency-events/).


