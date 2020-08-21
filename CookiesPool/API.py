from CookiesPool.RedisControl import RedisClient
from flask import Flask, g
from conf import Settings

app = Flask(__name__)


@app.route('/')
def index():
    return '<h2>Welcome to the Cookies Pool System</h2>'


@app.route('/<website>/random_cookies')
def random(website):
    conn = redis_conn()
    cookies = getattr(conn, website+'_cookies').random()
    return cookies


def redis_conn():
    for website in Settings.GENERATOR_MAP.keys():
        if not hasattr(g, website):
            setattr(g, website+'_cookies', RedisClient(website, 'Cookies'))
    return g
