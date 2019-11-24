from datetime import datetime
import feedparser
import sqlite3

monthDict = {'Jan': '1', 'Feb': '2', 'Mar': '3', 'Apr': '4', 'May': '5', 'Jun': '6', 'Jul': '7', 'Aug': '8', 'Sep': '9',
             'Oct': '10', 'Nov': '11', 'Dec': '12'}

DB_NAME = 'RSS_reader.db'
DATE_FORMAT = '%d %m %Y %H:%M:%S'


def load_feed(feed_name):
    last_update = convert_date(get_last_update_date(feed_name))
    url = get_url_by_name(feed_name)
    result = feedparser.parse(url)
    new_last_update = result['entries'][0]['published']
    if last_update < convert_date(new_last_update):
        update_last_update_date(feed_name, new_last_update)

    for item in result['entries']:
        if convert_date(item['published']) < last_update:
            break
        add_post(item['title'],
                 item['id'] if id in item else item['link'],
                 item['published'],
                 item['author'],
                 list(map(lambda x: x['term'], item['tags'])),
                 item['summary'],
                 item['content'][0]['value']
                 )


def init_db():
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()

    cursor.execute("CREATE TABLE FeedSource ( feed_name text, url text, img text, subtitle text, last_update text )")
    cursor.execute("CREATE TABLE Post ( title text, link text, date text, author text, tags text, desc text, body text )")
    cursor.execute("INSERT INTO FeedSource VALUES ( 'hongkiat', 'https://www.hongkiat.com/blog/feed', 'https://assets.hongkiat.com/uploads/cropped-hkdc-avatar-32x32.png', 'Tech and Design Tips', 'Fri, 22 Nov 2019 13:43:16 +0000')")

    db.commit()
    db.close()


def add_post(*values):
    print(values)
    # add_row("Post", *values)


def get_posts(feed_name):
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Post WHERE FEED_NAME = '{}'".format(feed_name))
    result = cursor.fetchall()
    db.commit()
    db.close()
    return result


def add_source(*values):
    add_row("FeedSource", *values)


def get_sources():
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM FeedSource")
    result = cursor.fetchall()
    db.commit()
    db.close()
    return result


def update_last_update_date(feed_name, date):
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    cursor.execute("UPDATE FeedSource SET last_update = '{}' WHERE feed_name = '{}'".format(date, feed_name))
    db.commit()
    db.close()


def get_last_update_date(feed_name):
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    cursor.execute("SELECT last_update FROM FeedSource WHERE feed_name = '{}'".format(feed_name))
    result = cursor.fetchone()[0]
    db.close()
    return result


def add_row(table, *values):
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    cursor.execute("INSERT INTO '{}' VALUES '{}'".format(table, str(values).replace("(", "").replace(")", "")))
    db.commit()
    db.close()


def get_url_by_name(feed_name):
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    sql = "SELECT url FROM FeedSource WHERE feed_name = '{}'".format(feed_name)
    cursor.execute(sql)
    result = cursor.fetchone()[0]
    db.close()
    return result

def convert_date(date):
    if date == '':
        return datetime(1970, 5, 12)
    date = date.split(',')[1][1:]
    date = date.split(' ')
    date[1] = monthDict[date[1]]
    date = '{} {} {} {}'.format(*date)
    return datetime.strptime(date, DATE_FORMAT)

print(load_feed("hongkiat"))
