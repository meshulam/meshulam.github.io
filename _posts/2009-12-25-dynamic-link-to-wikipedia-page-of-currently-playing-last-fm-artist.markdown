---
title: Dynamic link to currently playing Last.FM artist
date: '2009-12-25 15:46:10'
---


*Obligatory acknowledgment of lack of posting recently. I hope to be updating my blog more regularly. Also, look for a redesign in the near future.*

I wrote a simple PHP script that redirects to the Wikipedia page for your most recently played artist on Last.fm:

> [http://blog.meshul.am/scripts/lastwiki.php?user=capzloc](http://blog.meshul.am/scripts/lastwiki.php?user=capzloc)

This could be useful if you save the URL your bookmarks toolbar; simply replace "capzloc" with your own [Last.fm](http://last.fm/) username.

I've posted the code below. Not much to it, loads the recently played XML through the old last.fm backend, audioscrobbler. Then performs an I'm Feeling Lucky Google search for the most recent artist on the wikipedia.org domain. It could be easily modified to redirect to the Last.fm page, Amazon album page, etc.

lastwiki.php:

< ?php /* lastwiki.php * Redirects to wikipedia page for currently playing artist for specified last.fm user. * * Usage: lastwiki.php?user=putUserHere * * http://blog.meshul.am * Matt Meshulam * Public Domain */ $user = isset($_GET['user']) ? $_GET['user'] : "capzloc"; $file = "http://ws.audioscrobbler.com/1.0/user/$user/recenttracks.xml"; $xml = simplexml_load_file("$file"); $currArtist = $xml->track[0]->artist; header( "Location: http://www.google.com/search?q=$currArtist site:wikipedia.org&btnI=I'm+Feeling+Lucky" ) ; ?>


