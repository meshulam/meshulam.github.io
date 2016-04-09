---
layout: post
title: Passive Footswitch to MIDI Using Your Soundcard
date: '2009-01-20 12:32:21'
---


So a few months ago I scavenged some footswitches from the secret electrical engineering department free stuff room. I didn't really have a plan for them, so I terminated them with 1/4" plugs forgot about them.

{% include _image.html img="2009-01-20-img_2398_ewut7g.jpg" lightbox_img="2009-01-20-img_2398_ewut7g.jpg" caption="Footswitch" title="Footswitch"  %}
Then the other day I read about some software that MOTU is coming out with called [Volta](http://createdigitalmusic.com/2009/01/16/analog-meet-digital-motu-volta-connects-the-mac-to-cv-synths-effects-graphically/). It converts digital (MIDI, etc) control signals to analog control voltage for interfacing computers with analog synth gear. The cool, elegant part about it is that it does this by using your existing hardware. If you have a multichannel audio interface, which MOTU just happens to sell, the audio outputs become general voltage outputs using Volta.

This got me thinking that it would be pretty easy to do the opposite: I could use the inputs on my (coincidentally MOTU-brand) audio interface to hook up a footswitch to my (Windows) computer. Since the switch is just a passive momentary switch (short circuit when pressed down, open otherwise) I would need a voltage source in series with the switch to provide a signal that could be detected by the sound card. Most audio interfaces have a DC-blocking highpass filter on the input to protect it from stupidity-based damage. Because of this filtering, the digital signal doesn't look how one might expect. A back-of-the-envelope sketch illustrates:

{% include _image.html img="2009-01-20-img_2401_qegyly.jpg" lightbox_img="2009-01-20-img_2401_qegyly.jpg" caption="The effect of the DC blocking filter" title="Diagram"  %}
</div>The first step was to install a battery inside the footswitch. Since there would be virtually no current drawn from the battery, I elected to install the battery in a moderately permanent fashion, soldering wires directly to the terminals and hot gluing the battery in place. Note to potential future employers: this is not representative of my overall regard for safety, it's just a weekend project and I didn't have any battery clips around.

{% include _image.html img="2009-01-20-img_2387_ozijtj.jpg" lightbox_img="2009-01-20-img_2387_ozijtj.jpg" caption="Don't try this at home, kids" title="battery"  %}
{% include _image.html img="2009-01-20-img_2393_sriqc4.jpg" lightbox_img="2009-01-20-img_2393_sriqc4.jpg" caption="Inside the case with battery installed" title="inside"  %}
</div>I reattached the top half of the case and plugged it into one of the line inputs on my sound card. I tested it out and it worked exactly as expected. Note that I installed the battery backwards so the 'on' pulse is negative instead of positive:

{% include _image.html img="2009-01-20-fullscreen-capture-1172009-41841-pm_rpzasg.jpg" caption="fullscreen-capture-1172009-41841-pm" title="fullscreen-capture-1172009-41841-pm"  %}
Switch depressed for ~2 seconds, then for a fraction of a second
</div>With the hardware side finished, I had to decide the best way to control music software with the footswitch. I settled upon converting it to a MIDI note event. I installed [Maple Virtual Midi Cable,](http://www.hurchalla.com/Maple_driver.html) a tiny piece of software for Windows which provides virtual MIDI ports for sending data between programs. Then, I built up a patch in [PD](http://puredata.info/) to convert the positive and negative pulses to MIDI. This was my first foray into PD, so I'm sure there's some trivial way to implement this that I didn't know about.

{% include _image.html img="2009-01-20-pdswitch_qfrkza.png" url="http://blog.meshul.am/blog/wp-content/uploads/2009/01/footswitch.pd" caption="PD code to convert analog data to MIDI" title="footswitch.pd"  %}
Convert soundcard input to MIDI. Links to pd file.
</div>And that's it. As I implemented it, it takes the input from the third channel of the sound card and outputs a MIDI note on when the switch is depressed and a note off when it's released. Note that a velocity of zero is the same as a note off message. This patch could be easily parallelized by duplicating it and changing the ADC channel and MIDI note numbers.

The only downside to this simple method is that you can't generalize it to continuous controllers like a knob or expression pedal. You would need to send an AC signal through the controller since the highpass filter doesn't allow you to see small or slow variations in level, just impulses or quick steps. So I'll leave that modification for another day.


