from datetime import datetime
import feedparser
import sqlite3
import re

monthDict = {'Jan': '1', 'Feb': '2', 'Mar': '3', 'Apr': '4', 'May': '5', 'Jun': '6', 'Jul': '7', 'Aug': '8', 'Sep': '9',
             'Oct': '10', 'Nov': '11', 'Dec': '12'}

DB_NAME = 'RSS_reader.db'
DATE_FORMAT = '%d %m %Y %H:%M:%S'

"""
    You could say that open separate connection to DB for each query is not a clever idea. Yeah, i know that.
"""


def init_db():
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()

    cursor.execute("CREATE TABLE FeedSource (feed_name text, feed_title text, url text, img text, subtitle text, last_update text )")
    cursor.execute("CREATE TABLE Post (feed_id int, title text, link text, date text, author text, tags text, desc text, body text )")

    db.commit()
    db.close()


def load_feed(feed_id):
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    sql = "SELECT url, last_update FROM FeedSource WHERE feed_id = '{}'".format(feed_id)
    cursor.execute(sql)
    result = cursor.fetchone()
    db.close()

    last_update = convert_date(result[1])
    url = result[0]
    result = feedparser.parse(url)
    new_last_update = result['feed']['published'] if 'published' in result['feed'] else result['feed']['updated']

    # check if we already have relevant data
    if last_update < convert_date(new_last_update):
        update_last_update_date(feed_id, new_last_update)
        return

    for item in result['entries']:
        if convert_date(item['published']) < last_update:
            break
        add_post(feed_id,
                 item['title'] if 'title' in item else '',
                 item['id'] if 'id' in item else item['link'],
                 item['published'] if 'published' in item else '',
                 item['author'] if 'author' in item else '',
                 list(map(lambda x: x['term'], item['tags'] if 'tags' in item else [])),
                 item['summary'] if 'summary' in item else '',
                 item['content'][0]['value'] if 'content' in item and len(item) > 0 and 'value' in item['content'][0] else ''
                 )
    return True


def get_posts(feed_id):
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    sql = "SELECT * FROM Post WHERE feed_id = '{}'".format(feed_id)
    cursor.execute(sql)
    result = cursor.fetchall()
    db.close()
    return result


def add_feed(url):
    result = feedparser.parse(url)
    if 'bozo_exception' in result:
        return False
    feed = result['feed']
    add_row("FeedSource",
            parse_url(url),
            feed['title'],
            url,
            feed['image']['href'] if 'image' in feed else '',
            feed['subtitle'] if 'subtitle' in feed else '',
            result['feed']['published'] if 'published' in result['feed'] else result['feed']['updated']
            )

    feed_id = get_feed_id(url)
    # TODO rewrite mb?
    for item in result['entries']:
        add_post(feed_id,
                 item['title'] if 'title' in item else '',
                 item['id'] if 'id' in item else item['link'],
                 item['published'] if 'published' in item else '',
                 item['author'] if 'author' in item else '',
                 list(map(lambda x: x['term'], item['tags'] if 'tags' in item else [])),
                 item['summary'] if 'summary' in item else '',
                 item['content'][0]['value'] if 'content' in item and len(item) > 0 and 'value' in item['content'][0] else ''
                 )
    return True


def get_feed_id(url):
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    sql = "SELECT rowid FROM FeedSource WHERE url = '{}'".format(url)
    cursor.execute(sql)
    result = cursor.fetchone()
    db.close()
    return result[0]


def remove_feed(feed_id):
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    sql = "DELETE FROM FeedSource WHERE feed_id = '{}'".format(feed_id)
    cursor.execute(sql)
    db.commit()
    db.close()
    remove_posts_by_feed_id(feed_id)


def get_feeds():
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    cursor.execute("SELECT rowid, * FROM FeedSource")
    result = cursor.fetchall()
    db.close()
    return result


def update_last_update_date(feed_id, date):
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    cursor.execute("UPDATE FeedSource SET last_update = '{}' WHERE feed_id = '{}'".format(date, feed_id))
    db.commit()
    db.close()


def add_post(*values):
    add_row("Post", *values)


def add_row(table, *values):
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    values = tuple(map(lambda x: str(x).replace("'", '"').replace('\n', '').replace('\t', ''), values))
    sql = "INSERT INTO {} VALUES ({})".format(table, str(values).replace("(", "").replace(")", "")).replace('[', '"[').replace(']', ']"')
    cursor.execute(sql)
    db.commit()
    db.close()


def remove_posts_by_feed_id(feed_id):
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    sql = "DELETE FROM Post WHERE feed_id = '{}'".format(feed_id)
    cursor.execute(sql)
    db.commit()
    db.close()

def convert_date(date):
    if date == '':
        return datetime(1970, 5, 12)
    date = date.split(',')[1][1:].split(' ')
    date[1] = monthDict[date[1]]
    date = '{} {} {} {}'.format(*date)
    return datetime.strptime(date, DATE_FORMAT)


def parse_url(url):
    temp = url.split('/')
    if temp[0] != 'http:' and temp[0] != 'https:':
        return temp[0].replace('www.', '')
    else:
        return temp[2].replace('www.', '')


rss = [
    'https://www.hongkiat.com/blog/feed',
    'https://en.wikipedia.org/w/index.php?title=Special:NewPages&feed=rss',
    'https://habr.com/ru/rss/best/daily/?fl=ru',
    'http://rss.cnn.com/rss/edition.rss',
    'https://www.liga.net/tech/technology/rss.xml',
    'https://www.liga.net/news/photo/rss.xml',
    'https://www.liga.net/tech/gadgets/rss.xml',
    'http://api.flickr.com/services/feeds/photos_public.gne?tags=<neon>,<city>',
    ]


def fill_DB():
    init_db()
    for feed in rss:
       print(add_feed(feed))

# fill_DB()
#
#     print(result['entries'][0])
#     print(result['feed']['published'] if 'published' in result['feed'] else result['feed']['updated'])
#     print()
#     for item in result['entries'][0]:
#         print(item)
#     print()

