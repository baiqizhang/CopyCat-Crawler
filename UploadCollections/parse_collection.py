import urllib2
from bs4 import BeautifulSoup as BS


def download_page(url):
    print "Parsing page: %s" % url
    res = urllib2.urlopen(url)
    return res.read()


def parse(html):
    soup = BS(html, "lxml")
    photos = soup.select(".sheet.photo-container")
    jsonList = []
    for photo in photos:
        json = {}
        try:
            author_section = photo.select(".photo-description.photo-description--top .photo-description__author")[0]
            json['author_name'] = author_section.h2.a.text
            json['author_profile'] = author_section.a.img.get("src")

            image_section = photo.select(".photo.qa-photo")[0]
            image = image_section.select("a.photo__image-container")[0]
            json["src"] = image.img.get("src")
            jsonList.append(json)
        except (IndexError, KeyError, AttributeError) as e:
            print e
    return jsonList


def generate_json(url):
    html = download_page(url)
    return parse(html)



