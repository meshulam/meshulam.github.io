import os
import re
import urllib2

# Util script to transform markdown links and images

# Examples:
# Bare image:   ![CAPTION](IMGURL)
# Linked image: [![CAPTION](IMGURL "TITLE")](LINKURL)

POST_DIR = "blog/_posts"
IMAGE_DIR = "images"
EXPECTED_SUBSTRING = "cloudinary"

rex = re.compile(
        """(?P<before>.*)
           !\[(?P<caption>[^]]*)\]      # ![CAPTION]
           \((?P<image_url>[^)\s]*)     # (IMGURL
           (\s+"(?P<title>[^"]*)")?\)   # "TITLE")  - optional
           (\]\((?P<link_url>[^)]*))?   # (LINKURL  - optional
           "?\)?(?P<after>.*)""",       # )
        re.X)


def download(url, prefix=None):
    filename = url.split('/').pop()
    if prefix:
        filename = "{}-{}".format(prefix, filename)
    try:
        response = urllib2.urlopen(url)
    except urllib2.HTTPError as e:
        print("ERROR getting " + url)
        return url

    with open("{}/{}".format(IMAGE_DIR, filename), 'wb') as outfile:
        print("writing {} to {}".format(url, filename))
        data = response.read()
        outfile.write(data)
    return filename

def transform_line(line, prefix=None):
    match = re.search(rex, line)
    if match:
        args = match.groupdict()
        if EXPECTED_SUBSTRING in args['image_url']:
            imgpath = download(args['image_url'], prefix)
        else:
            print("HOTLINKED IMAGE: " + args['image_url'])
            imgpath = args['image_url']

        localimg2 = None
        linkurl = args['link_url']
        if linkurl and EXPECTED_SUBSTRING in linkurl and linkurl != args['image_url']:
            # Download link destinations if they are hosted like images
            localimg2 = download(linkurl, prefix)

        incl = '{% include _image.html '
        incl += 'img="{}" '.format(imgpath)
        if localimg2:
            incl += 'lightbox_img="{}" '.format(localimg2)
        elif linkurl and linkurl != args['image_url']:
            incl += 'url="{}" '.format(linkurl)

        if args['caption']:
            incl += 'caption="{}" '.format(args['caption'])
        if args['title']:
            incl += 'title="{}" '.format(args['title'])

        incl += " %}"
        if args['after'] and args['after'] != args['caption']:
            incl += "\n" + args['after']

        return incl

    return line

def transform_file(filename):
    prefix = filename.split('/').pop()[:10]
    print("transforming " + filename + " prefix: " + prefix)
    with open(filename, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        f.truncate()
        for line in lines:
            outline = transform_line(line, prefix)
            f.write(outline)


def transform_all_files():
    for filename in os.listdir(POST_DIR):
        transform_file(POST_DIR + '/' + filename)

transform_all_files()
