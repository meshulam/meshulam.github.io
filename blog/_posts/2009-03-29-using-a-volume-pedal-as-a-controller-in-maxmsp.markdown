---
layout: post
title: Using a Volume Pedal as a Controller in Max/MSP
date: '2009-03-29 10:52:09'
---


So a few months back, I showed [how to use a footswitch as a MIDI controller](http://blog.meshul.am/2009/01/passive-footswitch-to-midi-using-your-soundcard/) using your soundcard and PD. I hinted at being able to use a similarly simple technique for a continuous controller, so that what I'll be covering today. Thanks to my electronic music class, I've recently been doing a lot of work in Max/MSP, PD's expensive big brother, so that's the platform I used for this hack. It could be just as easily implemented in PD or another signal processing language.

[![img_2475](http://res.cloudinary.com/meshulam/image/upload/h_225,w_300/v1437619468/img_2475_ic1rt6.jpg "img_2475")](http://res.cloudinary.com/meshulam/image/upload/v1437619468/img_2475_ic1rt6.jpg)

This is a pretty simple trick, we are just sending a sine wave into the volume pedal and then measuring its level when it comes out. The level can then be used as a parameter to control any patch in Max/MSP or could be converted to a MIDI control.

For hardware, you'll need a volume pedal (obviously) and a soundcard with at least one extra input and one extra output. My volume pedal is a big, beautiful cast iron number that I got years ago when I built my theremin. I had to change the potentiometer in it from a 500k to a 1k (it was all I had lying around), but your results may vary depending on your soundcard. I think anything 1k-100k should be fine.

Connect the output of your soundcard to the "instrument" jack on the pedal, and connect the pedal's other jack to your soundcard's input.  That's it for the hardware! The patch itself isn't much more complicated. Let's take a look:

<div class="wp-caption alignleft" id="attachment_287" style="width: 286px">[![pedalpatch](http://res.cloudinary.com/meshulam/image/upload/v1437619467/pedalpatch_brleht.png "pedalpatch")](http://blog.meshul.am/blog/wp-content/uploads/2009/03/pedal.pat)Click to download pedal.pat

</div>This patcher is designed to be used as an object within another patch. It takes two arguments, the input channel and output channel of the soundcard, respectively. For example, you might write into an object box *"pedal 2 3"* if you want to use input 2 and output 3. It has a single input port, which calibrates the control signal to 1 when you send it a bang. The output is a floating point number representing the position of the pedal.

The nitty-gritty is actually pretty simple, a 5 kHz sine wave is generated and output. The peakamp~ object keeps track of the maximum level it's seen in the past 20 ms and this level is divided by the calibration value. That's it!

I'm using this as part of a bigger program designed for live performance. I'll talk more about it as I get closer to finishing it.


