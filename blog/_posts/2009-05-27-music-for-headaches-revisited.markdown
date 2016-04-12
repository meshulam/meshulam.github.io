---
layout: post
title: '"Music for Headaches" revisited'
date: '2009-05-27 16:31:21'
---


As I mentioned [a few posts back]({% post_url 2009-04-25-music-to-get-a-headache-to %}), I had the opportunity to perform in the final concert for my electronic music class. For the performance I developed a Max/MSP patch from the ground up that allowed me to record samples from a microphone and alter then in real-time.

*[Choose your own blog adventure: If you just want to hear the recording of the performance, scroll to the end of this post. If your eyes didn't glaze over when I said "Max/MSP," continue reading below]*

When I started the project, my goal was to develop a super-flexible framework for performing live sample-based music. I've never been all that impressed with computer-based musical performance. There's a fine balancing point where the performer needs to have enough control to be able to express himself, but if there is too much flexibility, or if the interface isn't intuitive, the performer can't affect the sound in a meaningful way. My humble attempt at cracking the most difficult problem in electronic music resulted in a Max/MSP patch I call Phonogene. The original [phonogene](http://en.wikipedia.org/wiki/Musique_concr%C3%A8te#The_phonogene) was a device invented in the mid-1950's which first allowed the pitch and speed of a sound to be varied independently (more [here](http://www.joostnieuwenburg.nl/phonogene.html)). Let's take a look at the Max patch's interface:

{% include _image.html img="2009-05-27-max-patch-default-ui_wdzouz.png" lightbox_img="2009-05-27-max-patch-default-ui_wdzouz.png" title="defaultUI"  %}
Other than the blinding ugliness of the UI, you'll notice that there are four identical channel strips. Each channel has number boxes for pitch, length, and speed. The vertical fader is a volume control, and the two knobs are "drunkenness" controls. These add an element of randomness to the playback. The top knob controls how much the pitch will vary on its own and the bottom knob adjusts the variance of the speed. Below this section is a waveform viewer which shows the sample that has been recorded into each channel. On the far right side are two volume level meters: a master level and a meter for a backing track.

Since the keyboard and mouse are kind of lame, I opted to use a MIDI keyboard controller to operate the patch. Since I wasn't interested in making traditional tonal music, I just used it as a box with a bunch of buttons and knobs:

{% include _image.html img="2009-05-27-img_2589_mlwxcq.jpg" lightbox_img="2009-05-27-img_2589_mlwxcq.jpg" caption='"Custom" MIDI Controller' title="controller"  %}
Here's how it works: you select a track or tracks by holding down its respective key, then change a parameter by using the corresponding wheel or button. For example, to reset track 1 to its original pitch and speed, I would press the "Track 1" key and the "Reset" key at the same time.

I used a footswitch to trigger recording, which allowed me to keep my hands free for percussion instruments or other soundmaking toys. The patch remembers the last track to be selected, and records into that track when the footswitch is held down. Let's look at Phonogene's UI one more time, now in the middle of a performance:

{% include _image.html img="2009-05-27-max-patch-ui-in-use_tzmkky.png" lightbox_img="2009-05-27-max-patch-ui-in-use_tzmkky.png" caption="phonogene-ui-in-use" title="phonogene-ui-in-use"  %}
The waveforms for each sample are at the bottom of each track, as is a black vertical line showing the playback position within each sample. The red square at the top of track four shows that it was the last track to be selected, so when the "record" pedal is pressed, the microphone will record into track four.

I'm not going publish the patch at this point because it is pretty messy and there are still some changes I'd like to make to it. In the coming months I'll probably write some shorter posts about specific parts of Phonogene, complete with downloadable code, but for now here's just a picture of the top-level patch:

{% include _image.html img="2009-05-27-max-patch_cykftl.png" lightbox_img="2009-05-27-max-patch_cykftl.png" caption="Top-level Phonogene patch in Max/MSP" title="max-patch"  %}
I wish Max/MSP had a decent text-based syntax. I've had it with these stupid little boxes and wires.

Finally, here's the recording of "Music for Headaches" from my performance at the concert. To clarify, not everything you hear was recorded and manipulated live. After rehearsing many times, I decided that having some pre-edited backing sounds would expand the---excuse the term---sonic possibilites. All the live samples were vocal-based, except for the jangling keys sound.

<object data="http://s3.amazonaws.com/stlth/static/production/swf/audio_controller.swf" height="100" type="application/x-shockwave-flash" width="400"><param name="wmode" value="opaque"></param><param name="flashvars" value="song_label=converted-music_for_headaches_live_converted.mp3&music_track=http://drop.io/download/public/jwx3qs028ycqaasr5ymt/40823f5d295e9fa5058230effa2071ef2a544728/59cb7ae0-13d6-012c-f976-f6f33324943c/a2e6a100-22c7-012c-dfad-fbd1135ecf2a/converted-music_for_headaches_live_converted.mp3&autoplay=false"></param><param name="src" value="http://s3.amazonaws.com/stlth/static/production/swf/audio_controller.swf"></param></object>

[Download](http://drop.io/khoxooz/asset/music-for-headaches-live-mp3)


