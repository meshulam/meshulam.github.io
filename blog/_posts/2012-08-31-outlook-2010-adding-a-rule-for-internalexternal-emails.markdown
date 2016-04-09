---
layout: post
title: 'Outlook 2010: Adding a rule for internal/external emails'
date: '2012-08-31 18:47:34'
---


After banging my head against my desk in frustration for months, I finally figured out a way to create a rule in Outlook that moves emails sent from an internal address. First I tried using the "specific words in the sender's address" condition, using my company's domain name as the word. This works for any specific external domains but it didn't work for me in this case. My guess is that Exchange email addresses are represented differently behind the scenes, causing a bug in this filter.

The solution is to create a condition "with specific words in the message header", and use this string: `X-MS-Exchange-Organization-AuthAs: Internal`

The result should look something like the following:

{% include _image.html img="2012-08-31-outlookrule_aykbxl.png" title="outlookrule"  %}

You could also use `-AuthAs: Anonymous` to catch external emails. I only tested this in my current setup, using Outlook/Exchange 2010. It probably won't work if you don't have Exchange as your email server.

