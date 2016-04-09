---
layout: post
title: Poor man's time sync in Linux
date: '2011-07-27 20:11:44'
---


Want to sync the clocks of multiple Linux machines but don't want to go through the process of setting up NTP? If you're okay with ~1-second precision, you can just run the command:

> sudo date -s "$(ssh user@hostname date '+%Y%m%d %T')"

to set the local machine's clock to the server.


