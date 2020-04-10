import feedparser
import random

HOST_URL = "https://www.reddit.com/r/ProgrammerHumor.rss"


def getMeme():
    memelist = []
    print("Memes from ProgrammerHumor")
    f = feedparser.parse(HOST_URL)
    for entry in f.entries:
        x = entry['content'][0]['value']
        print("Title: " + entry["title"])
        print("Post: " + str(entry["link"]))
        img = x[x.find("https://i.redd.it"): x.find("link") - 3]
        print("Meme: " + img, end="\n")
        memelist.append(img)
        random.shuffle(memelist)
        return memelist[0]


def main():
    meme = getMeme()
    print(f"::set-output name=meme::{meme}")


if __name__ == "__main__":
    main()
