import feedparser
import random
import os
import sys
import json

SUB_URL = "https://www.reddit.com/r/ProgrammerHumor"
FALLBACK = {
    "meme_link": "https://raw.githubusercontent.com/Bhupesh-V/memer-action/master/images/header.png",
    "title": "Oops :( looks we are out of memes.",
    "src": "https://github.com/Bhupesh-V/memer-action",
}


def getMeme(filter_posts="hot"):
    memelist = []
    memedict = {}
    f = feedparser.parse(f"{SUB_URL}/{filter_posts}.rss")
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
    elif os.environ["INPUT_FALLBACK"]:
        fallback_dict = json.loads(os.environ["INPUT_FALLBACK"])
        if FALLBACK.keys() == fallback_dict.keys():
            memelist.append(fallback_dict)
        else:
            print("Key Error, make sure keys are", FALLBACK.keys())
            sys.exit(0)
    else:
        memelist.append(FALLBACK)

    return memelist[0]


def main():
    filter_by = os.environ["INPUT_FILTER"]
    if filter_by not in ["hot", "top", "new", "rising"]:
        print("filter must be one of hot, top, new or rising")
        sys.exit(0)
    meme = getMeme(filter_by)
    print(f"::set-output name=meme::{meme['meme_link']}")
    print(f"::set-output name=title::{meme['title']}")
    print(f"::set-output name=source::{meme['src']}")


if __name__ == "__main__":
    main()
