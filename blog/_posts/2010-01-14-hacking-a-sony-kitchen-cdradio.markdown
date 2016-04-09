---
layout: post
title: Hacking A Sony Kitchen CD/Radio
date: '2010-01-14 19:49:08'
---


[![Product shot](http://res.cloudinary.com/meshulam/image/upload/v1437619424/31P6TKD01NL._SS500_-e1263351260356_h6rjgq.jpg "31P6TKD01NL._SS500_")](http://blog.meshul.am/blog/wp-content/uploads/2010/01/31P6TKD01NL._SS500_.jpg)My mom has had a [Sony ICF-CD543RM](http://www.google.com/products/catalog?q=ICF-CD543RM&oe=utf-8&rls=org.mozilla:en-US:official&client=firefox-a&um=1&ie=UTF-8&cid=6203804586318164240&ei=7DtNS7yCN4jYNaXAyPIM&sa=X&oi=product_catalog_result&ct=result&resnum=3&ved=0CBsQ8wIwAg#ps-sellers) under-counter CD player/radio for about a year. Recently the CD player has gotten pretty unreliable; at first it had a hard time with burned CDs, but it gradually got more picky with what discs it would play. Once it got pretty much unusable, I figured I had nothing to lose by trying to modify the system to give it an 1/8" line-in, which could be used with an external DiscMan or MP3 player. A saner man might have just put some cheap computer speakers in the kitchen, but my mom uses the radio on the unit, and it's nice to not have two separate sound systems in the kitchen.

My goal was to trick the player into playing the signal from the line-in when it was in CD mode. I opened up the beast, hoping that the circuitry be clearly labeled.

<div class="wp-caption aligncenter" id="attachment_542" style="width: 560px">[![](http://res.cloudinary.com/meshulam/image/upload/h_413,w_550/v1437619424/IMG_2761_vziahx.jpg "IMG_2761")](http://res.cloudinary.com/meshulam/image/upload/v1437619424/IMG_2761_vziahx.jpg)CD player innards.

</div>The tan circuit board at the bottom is the radio and amplifier. The CD player is the CD player-shaped thing in the center, and the controls and microcontroller are in the front panel (top). The various circuit boards were connected with ribbon cables, and luckily the wires were well-labeled. The first thing I tried was to cut the stereo audio wires coming from the CD player board and to splice in my own cable. Unfortunately, when I pressed the 'CD' button on the unit it would see that there was no CD inserted and turn off. When I put a CD in, it would spin up but it wouldn't start playing (since it's broken) and no sound could be heard.

<div class="wp-caption alignright" id="attachment_544" style="width: 160px">[![](http://res.cloudinary.com/meshulam/image/upload/c_crop,h_768,w_768,x_0,y_128/h_150,w_150/v1437619424/IMG_2775_lfzsry.jpg "ribbonlabel")](http://res.cloudinary.com/meshulam/image/upload/v1437619424/IMG_2775_lfzsry.jpg)Labeled ribbon cable from controls to amplifier board. Note mute and power pins are tied together.

</div>I knew there must be some sort of control signal telling the amplifier that the CD was ready to pass audio. Sure enough, on the ribbon cable going from the control board to the amp, there was a "mute" line. By metering these lines in the player's various states (radio, cd, standby), I could see that "mute" was held high at 3.3 volts when the radio was playing, but was low in standby mode and broken CD mode. I noticed that the "power" line was high in both playing states and low in standby mode, so I cut the mute wire from the control board and soldered the mute pin to the power pin. See photo at right.

Sure enough, my external audio could now be heard when the player was in CD mode. I picked out a CD that I didn't care about, and put it in the tray as a permanent "dummy disc" to fool the stereo into thinking it was playing from a CD. Now that I had a solution, I tidied up my work.

<div class="wp-caption aligncenter" id="attachment_545" style="width: 560px">[![finished product](http://res.cloudinary.com/meshulam/image/upload/h_413,w_550/v1437619423/IMG_2777_l2y8rk.jpg "IMG_2777")](http://res.cloudinary.com/meshulam/image/upload/v1437619423/IMG_2777_l2y8rk.jpg)External stereo in (left) replacing CD audio; disconnected "mute" wire (right)

</div><div class="wp-caption aligncenter" id="attachment_554" style="width: 560px">[![](http://res.cloudinary.com/meshulam/image/upload/h_413,w_550/v1437619412/IMG_2780_vjczll.jpg "IMG_2780")](http://res.cloudinary.com/meshulam/image/upload/v1437619412/IMG_2780_vjczll.jpg)Almost done: an external CD player playing through the speakers of the under-counter unit.

</div>I was going to Dremel a little hole out of the case for the line-in cable, but I was able to route it through an existing opening on the back of the unit. As I was reassembling the case, I popped off the plastic "eject" button as a reminder that the built-in CD player doesn't work, and so that the crucial dummy disc couldn't be removed. Not too shabby for an hour or two of work, if I may say so myself.

<div class="wp-caption aligncenter" id="attachment_550" style="width: 560px">![reassembled](http://res.cloudinary.com/meshulam/image/upload/h_227,w_550/v1437619423/IMG_2783_wovfeo.jpg "IMG_2783")The reassembled unit, sans "eject" button.

</div>
