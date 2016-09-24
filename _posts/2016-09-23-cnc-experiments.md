---
title: "CNC Experiments: Baltic Birch Plywood"
---

I'm planning some projects involving CNCing shapes from plywood
and wanted to get a better sense of what tools/feedrates/etc will produce
the best results. There's a near-infinite supply of anecdotal feeds &
speeds advice 
online, but not nearly as much data from controlled tests.

I recently bought some new end mills and was doing some test cuts of my own, 
and figured the results might be helpful for others.

## TL;DR

To cut parts from Baltic birch plywood, use a 1/4" 2-flute straight end mill at 
10k RPM and a feed rate of 150-200 IPM. Use conventional milling and a max pass 
depth of 0.25".

## The setup

**Material:** 12mm (measured 0.470") Baltic Birch plywood

**Tools:** Two brand new 2-flute 1/4" end mills:

* Freud 04-110 1/4" straight
* Freud 76-102 1/4" down spiral

**CNC:** 48x96 inch ShopBot PRS at Pumping Station: One

I modeled a small test shape in Fusion 360 and generated sevaral toolpaths 
with varying feed rate, number of depth passes, and milling direction. Spindle speed was
a constant 10k RPM. 

{% include _image.html img="2016-09-23-toolpath.png" caption="Fig 1: Fusion 360 model and toolpaths" %}

Here are the 8 samples I cut:

| Sample | Tool | Feed rate (IPM) | Passes | Milling direction |
| ------ | ---- | --------------- | ------ | ------------------|
| A1 | Straight | 75 | 2 | Conventional |
| A2 | Straight | 150 | 2 | Conventional |
| A3 | Straight | 225 | 2 | Conventional |
| A4 | Straight | 150 | 1 | Conventional |
| B1 | Downcut | 150 | 2 | Climb |
| B2 | Downcut | 150 | 2 | Conventional |
| B3 | Downcut | 225 | 2 | Conventional |
| B4 | Downcut | 150 | 1 | Conventional |

## Results

I swapped the slowest cut (A1) for medium-speed climb cut (B1) when I switched from
the straight to the downcut bit. I originally planned to redo all 4 parts as climb cuts,
but decided to just do one for comparison as I knew conventional was better for my
purposes (more on that later).

### Straight vs. Downcut

The side walls of the downcut cuts had subtle ridges, while the straight tool's cuts
were almost perfectly smooth. The downcut was louder when cutting, and I 
assume those two things are related. The shaft of the downcut bit is about 1/4" shorter
than the straight bit, so it's possible the collet didn't get as good of a grip
on the downcut, causing some chatter. Not sure what else could have caused it,
I certainly didn't expect such a difference in finish between two such similar tools.

{% include _image.html img="2016-09-23-downcut-edges.jpg" caption="Fig 2: Downcut parts. From top: B4, B2, B3" %}

{% include _image.html img="2016-09-23-straight-edges.jpg" caption="Fig 3: Straight flute parts. From top: A4, A2, A3" %}

The straight flute parts had a slightly cleaner bottom surface, which is expected, but the difference was very
minor. I wouldn't consider the difference to be significant, and would probably disappear entirely
with light sanding (I didn't sand at all before these photos).

### Feed rate

I varied the feed rate from a definitely-too-low 75 IPM (0.00375" chip load) to
225 IPM (0.01125" chip load). The ShopBot can comfortably go a little faster, but 
I stopped there because with such a small part, it would have been unlikely to
ever accelerate much faster than that.

There was very little difference in cut quality over this 300% variation
in speed. The slowest cuts were slightly louder than the others, and the
chips produced were noticably smaller, but nothing too concerning. One
of the biggest effects of changing feed rate is the lifetime of the tool,
so perhaps there would be a noticeable difference in that regard between
150 and 225 IPM. But for hobbyist-level usage, I'd be comfortable recommending
anything in that range.

I'd like to test even higher chip loads by reducing spindle speed below 10,000 RPM, 
but that will need to wait for the next round of experiments.

### Climb vs. conventional milling & other dimensional variations

I've noticed that climb toolpaths tend to produce parts slightly larger than their
specified dimensions, and conventional toolpaths are usually right on.
I think this is because of the deflection of the bit from the
difference in force between the two sides of the path. 

On each part, I used calipers to measure the width of the two "teeth":

|Cut type | Min (inches) | Max (inches) | Count |
|---------|--------------|--------------|-------|
|**As designed** | 0.940 | 0.940 | - |
|Conventional 2-pass | 0.937 | 0.941 | 10 |
| Climb 2-pass | 0.950 | 0.951 | 2 |
| Conventional 1-pass | 0.929 | 0.931 | 4 |

The climb cut was about 0.01" oversized, and the 1-pass conventional cut
was about 0.01" undersized. Precise dimensioning in wood is always
an uphill battle due to heat- and humidity-related expansion, but these 
0.01" variations make a big difference for joinery. 

The long slots on each part were designed to be as wide as the thickness of the
material (0.470") to allow two parts to slot into each other. 
The smaller 1-pass parts could slide into each other easily,
with some wiggle when joined. The conventional 2-pass parts could be joined
with some force, but were difficult to re-separate. The climb-milled parts
were too big (resulting in a slot too narrow) to be joined at all.

{% include _image.html img="2016-09-23-straight-dims.jpg" caption="Fig 4: Straight bit parts with dimensions" %}

{% include _image.html img="2016-09-23-downcut-dims.jpg" caption="Fig 5: Downcut bit parts with dimensions" %}

### Pass depth/number of passes

The A4 and B4 tests cut a single ~0.5" deep pass instead of splitting
the depth into two passes. It sounded like the spindle was struggling a little more
than with the other cuts, but the quality of the finish was still great. In fact, 
some of the 2-pass parts had a visible line halfway through the part at the
bottom of the first pass (see Figure 3 above), so the single pass actually had
a better finish.

The different sound when cutting, combined with the smaller finished dimension,
leads me to believe that cutting 1/2" deep is causing excess vibration in the tool.
If you're really in a hurry it works well enough, but I'd advise going a little
faster and taking two passes instead.

## Conclusion

These tests didn't cover the full range of every CNC parameter I'm interested in, but
I definitely learned a lot by this more scientific approach. Hopefully others
will find these observations useful as well!
