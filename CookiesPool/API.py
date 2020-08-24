from CookiesPool.RedisControl import RedisClient
from CookiesPool.Tester import WeiBoCookiesTester
from flask import Flask, g
from conf import Settings

app = Flask(__name__)


@app.route('/')
def index():
    return '<h2>Welcome to the Cookies Pool System</h2>'


@app.route('/<website>/random')
def random(website):
    conn = redis_conn()
    while True:
        cookies_dict = getattr(conn, website+'_cookies').random()
        usr, cookies = list(cookies_dict.keys())[0], list(cookies_dict.values())[0]
        obj = WeiBoCookiesTester(website)
        obj.test(cookies, usr, Settings.TEST_URL[website])
        if obj.STATUS:
            return cookies
        else:
            return 'All cookies are invalid, please generate again'


@app.route('/<website>/count')
def count(website):
    conn = redis_conn()
    counts = getattr(conn, website+'_cookies').count()
    return str(counts)


def redis_conn():
    for website in Settings.GENERATOR_MAP.keys():
        if not hasattr(g, website):
            setattr(g, website+'_cookies', RedisClient(website, 'Cookies'))
    return g
