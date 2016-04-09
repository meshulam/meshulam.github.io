---
layout: post
title: Archiving a website with Amazon S3
date: '2013-08-24 16:14:16'
---


About five years ago, my friend Zach and I made the EnerJar, an open-source hardware design for a power meter. We created a website, enerjar.net, to document the design. We used the Drupal CMS framework so that we could easily update the content and allow users to comment on it.

After a few months, the site sat pretty much unchanged, but it was still backed by a database, PHP, and a bit of configuration on a shared hosting environment. After having to fix the site a few times after surprise upgrades and configuration changes, I decided to transition it to a static website where it could live reliably for the rest of time.

Static websites have many benefits over ones which rely on server-side scripting: they're cheaper and simpler to host, have virtually no risk of security breaches, and are much more scalable. Of course the downside is that users can't really interact with static websites, so they only work if you're okay with a simple read-only product.

Here's how I transitioned enerjar.net into a static site hosted on Amazon S3:


## Step 0: prepare the site

You're effectively taking a picture of each page on your website, so any dynamic features will no longer work. This includes comments, searching (sometimes), and submitting new content. If you're transitioning a site that uses a framework like WordPress or Drupal, you'll want to disable any of these features in advance so that visitors don't even see them. Otherwise they get an error message when trying to actually submit a comment or something.


## Step 1: download the site

From any Unix/Linux/OSX command line, you can use wget to recursively download all the resources on your site. I used the following command:

~~~
wget --recursive --page-requisites --html-extension --convert-links --domains enerjar.net http://enerjar.net/
~~~

"recursive" says to follow links on the page and continue to follow any links on the sub-pages. "page-requisites" tells wget to download not just the page itself, but resources like CSS and Javascript files. "domains" limits the recursive link-following to the enerjar.net domain, so it doesn't try to download external links.

I begrudgingly used "html-extension" and "convert-links" to rename every downloaded page file so that it ends with the .html extension. **This could break outside links to your site, but it means you don't need to manually configure content types for these files on S3. **If a page URL doesn't end with a file extension, for example, *something.com/blog/entry1*, wget will download it without an extension, to a file called entry1. The problem is that S3 doesn't know that entry1 is an html file, so when visiting the re-hosted page, your browser will download the file instead of displaying it as an actual page. By adding the .html extension on download we avoid this problem. Maybe someone knows a better way to do this, but I was lazy and this was good enough for me.


## Step 2: Test the downloaded site

Open the HTML files that you downloaded with wget and make sure that everything shows up correctly and that links still work. For some reason wget didn't download some of the images on the site, so I had to manually get them and put them in the proper directories. Once everything looks good, you are ready for the fun parts.


## Step 3: Create a new S3 bucket

If you don't already have one, open an Amazon Web Services account and create a new S3 bucket. Put it in whatever region you want, but **the name of the bucket must be exactly the same as your root domain name**. So I named my bucket "enerjar.net".


## Step 3: Upload the site contents

After fiddling with various command-line tools for AWS, I gave up and used Amazon's Java uploader in the browser. You need to use the Java one to upload directories, otherwise you'll need to manually recreate the directory tree and upload files into each folder separately. Be sure to upload the site into the root directory of the bucket.


## Step 4: configure static website hosting

In "properties" for the bucket, select *Static website hosting->Enable website hosting*. Set your root and error documents as necessary.


## Step 5: Custom domain

Follow [Amazon's tutorial](http://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html) for setting up DNS for hosting a static site with your own domain. The only snag I hit was that it didn't autocomplete the domain name for the alias. I thought it needed to be the domain of the actual S3 bucket (e.g. enerjar.net.s3-website-blahblah), but it actually just expects the root domain for the region where your bucket lives. In my case, *s3-website-us-west-2.amazonaws.com*.


## Step 6: DNS and finishing up

As covered in the linked tutorial in step 5, you'll need to set up your domain to use Amazon's name servers. Make sure you also transfer any other DNS records (mailservers, subdomains, etc) to your Route 53 configuration.

That's it! You should now have a rock-solid, super-cheap hosting setup for your now-static website.


