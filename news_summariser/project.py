import feedparser
import datetime

def main():
    headlines=get_headlines()
    cleaned=[clean_headline(h) for h in headlines]
    display(cleaned)
    save_to_file(cleaned)

def get_headlines():
    feed=feedparser.parse("http://feeds.bbci.co.uk/news/india/rss.xml")
    titles=[entry.title for entry in feed.entries]
    return titles

def clean_headline(headline):
    return headline.strip()


def display(headlines):
    for i, headline in enumerate(headlines, 1):
        print(f"{i}. {headline}")


def save_to_file(headlines):
    tdy=datetime.date.today()
    filename=f"news_{tdy}.txt"
    with open(filename, "w") as f:
        for headline in headlines:
            f.write(headline + "\n")


if __name__ == "__main__":
    main()