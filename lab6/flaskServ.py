from flask import *
from math import ceil
from db_connector import *
import base64

app = Flask(__name__, template_folder='./static/templates')
NEWS_ON_PAGE = 10


@app.route('/')
def main_page():
    feeds = get_feeds()
    return render_template('main.html', feeds=feeds)


@app.errorhandler(404)
def not_found(e):
    return redirect(url_for('main_page'))


@app.route('/feed/<feed_id>')
def feed(feed_id):
    if get_feed(feed_id) == None:
        return redirect(url_for('main_page'))
    load_feed(feed_id)
    feeds = get_feeds()
    current_feed = ''
    for item in feeds:
        if int(item[0]) == int(feed_id):
            current_feed = item
            break
    if current_feed == '':
        return redirect(url_for('main_page'))
    articles = list(map(lambda x: list(map(lambda y: y, x)), get_posts(current_feed[0])))
    pages = ceil(len(articles)/NEWS_ON_PAGE)
    articles = articles[0:NEWS_ON_PAGE]
    for article in articles:
        article[3] = ' '.join(article[3].split(' ')[1:-1])
        article[5] = article[5].replace('"', '').replace('[', '').replace(']', '').split(', ')
    return render_template('feed.html', feeds=feeds, current_feed=current_feed, articles=articles, pages=pages, feed_id=feed_id)


@app.route('/rest/feed/<feed_id>/<page>')
def feed_page(feed_id, page):
    page = int(page)
    if get_feed(feed_id) == None:
        return redirect(url_for('main_page'))
    load_feed(feed_id)
    feeds = get_feeds()
    current_feed = ''
    for item in feeds:
        if int(item[0]) == int(feed_id):
            current_feed = item
            break
    if current_feed == '':
        return redirect(url_for('main_page'))
    articles = list(map(lambda x: list(map(lambda y: y, x)), get_posts(current_feed[0])))
    pages = ceil(len(articles) / NEWS_ON_PAGE)
    if pages < page or page < 1:
        return jsonify({'error': 'Wrong page number'})
    else:
        articles = articles[(page-1) * NEWS_ON_PAGE: page * NEWS_ON_PAGE]
    for article in articles:
        article[3] = ' '.join(article[3].split(' ')[1:-1])
        article[5] = article[5].replace('"', '').replace('[', '').replace(']', '').split(', ')
    return jsonify({'articles': articles})


@app.route('/rest/feed/add', methods=['POST'])
def rest_add_feed():
    url = request.data.decode('utf8').split('=')[1]
    url = url.replace('_', '/').replace('-', '+').replace('*', '=')
    url = base64.urlsafe_b64decode(url)
    url = url.decode('utf8')
    if get_feed_id(url) > 0:
        return jsonify({'error': 'Already exist'})
    if not add_feed(url):
        return jsonify({'error': 'Not found'})
    feed_id = get_feed_id(url)
    feed = get_feed(feed_id)
    return jsonify({
        'feed_id': feed_id,
        'feed_name': feed[0],
        'feed_title': feed[1]
    })


@app.route('/rest/feed/remove', methods=['DELETE'])
def rest_remove_feed():
    id = request.data.decode('utf8').split('=')[1]
    if remove_feed(id):
        return jsonify({'success': 'success'})
    else:
        return jsonify({'error': 'Error'})