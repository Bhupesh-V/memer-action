import feedparser
import random
import os
import sys

HOST_URL = "https://www.reddit.com/r/ProgrammerHumor"


def getMeme(filter_posts="hot"):
    memelist = []
    memedict = {}
    f = feedparser.parse(f"{HOST_URL}/{filter_posts}.rss")
    for entry in f.entries:
        x = entry['content'][0]['value']
        img = x[x.find("https://i.redd.it"): x.find("link") - 3]
        if img != "":
            memedict["title"] = entry["title"]
            memedict["src"] = str(entry["link"])
            memedict["meme"] = img
            memelist.append(memedict)
        random.shuffle(memelist)
        return memelist[0]


def main():
    filter_by = os.environ["filter"]
    if filter_by not in ["hot", "top", "new", "rising"]:
        sys.exit(0)
    meme = getMeme(filter_by)
    print(f"::set-output name=meme::{meme['meme']}")
    print(f"::set-output name=title::{meme['title']}")
    print(f"::set-output name=source::{meme['src']}")


if __name__ == "__main__":
    main()
