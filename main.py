import feedparser
import random

HOST_URL = "https://www.reddit.com/r/ProgrammerHumor.rss"


def getMeme():
    memelist = []
    memedict = {}
    f = feedparser.parse(HOST_URL)
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
    meme = getMeme()
    print(f"::set-output name=meme::{meme['meme']}")
    print(f"::set-output name=title::{meme['title']}")
    print(f"::set-output name=source::{meme['src']}")


if __name__ == "__main__":
    main()
