import feedparser

def get_news(count):
    feed_url = "https://hnrss.org/frontpage"

    feed = feedparser.parse(feed_url)
    return [entry["title"] + ": " + entry["link"] for entry in feed.entries[:count]]
