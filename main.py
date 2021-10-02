import feedparser
import random
import os
import sys
import json
import urllib

SUB_URL = "https://www.reddit.com/r/ProgrammerHumor"
FALLBACK = {
    "meme_link": "https://raw.githubusercontent.com/Bhupesh-V/memer-action/master/images/header.png",
    "title": "Oops :( looks like we are out of memes.",
    "src": "https://github.com/Bhupesh-V/memer-action",
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
    "Content-Type": "application/json",
}


NS = {"ns": "http://www.w3.org/2005/Atom"}

def request(url, data=None, method=None):
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req) as response:
            res = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        print(e.reason)
        exit()
    return res


def parseXML():
    data = request(f"{SUB_URL}/new.rss")
    tree = ET.fromstring(data)
    entries = tree.findall("ns:entry", namespaces=NS)


    for e in entries:
        title = e.find("ns:title", namespaces=NS).text
        content = e.find("ns:content", namespaces=NS).text
        img = content[
            content.find("https://i.redd.it") : content.find("link") - 3
        ]
        print(title, link)

def getMeme(filter_posts="hot"):
    memelist = []
    memedict = {}
    f = feedparser.parse(f"{SUB_URL}/{filter_posts}.rss")
    print(f.status)

    print(len(f.entries))
    for entry in f.entries:
        post_content = entry["content"][0]["value"]
        img = post_content[
            post_content.find("https://i.redd.it") : post_content.find("link") - 3
        ]
        if img != "":
            memedict["title"] = entry["title"]
            memedict["src"] = str(entry["link"])
            memedict["meme_link"] = img
            memelist.append(memedict)

    if len(memelist) != 0:
        random.shuffle(memelist)
#     elif os.environ["INPUT_FALLBACK"]:
#         fallback_dict = json.loads(os.environ["INPUT_FALLBACK"])
#         if FALLBACK.keys() == fallback_dict.keys():
#             memelist.append(fallback_dict)
#         else:
#             print("Key Error, make sure keys are", FALLBACK.keys())
#             sys.exit(0)
    else:
        memelist.append(FALLBACK)

    return memelist[0]


def main():
    filter_by = "new"
    print(feedparser.__version__)
    parseXML()
    if filter_by not in ["hot", "top", "new", "rising"]:
        print("filter must be one of hot, top, new or rising")
        sys.exit(0)
    meme = getMeme(filter_by)
    print(f"::set-output name=meme::{meme['meme_link']}")
    print(f"::set-output name=title::{meme['title']}")
    print(f"::set-output name=source::{meme['src']}")


if __name__ == "__main__":
    main()
