from CookiesPool.SaveAccount import RedisClient
from conf import Settings
import requests
import json
import time


class BasicTester:
    def __init__(self, website):
        self.DB_ACCOUNT = RedisClient(website, 'Account')
        self.DB_COOKIES = RedisClient(website, 'Cookies')
        self.TEST_DELAY = Settings.TEST_DELAY
        self.STATUS = False

    def test(self, cookies,  usr, test_url):
        print('账号：%s，正在检测Cookies......' % usr)
        try:
            res = requests.get(test_url, cookies={'cookie': cookies}, allow_redirects=False)
            if res.status_code == 200:
                res.json()
                self.STATUS = True
                print(cookie_dict)
                print('账号：%s Cookies有效' % usr)
            elif res.status_code == 302:
                self.STATUS = False
                print('账号：%s Cookies失效，删除cookies' % usr)
                self.DB_COOKIES.delete(usr)
            else:
                print('网页已不存在，请更换检测URL')
        except json.JSONDecodeError:
            print('账号：%s，Cookie无效' % usr)
            self.DB_COOKIES.delete(usr)
            self.STATUS = False
            print('账号：%s，Cookie已删除' % usr)
        except ConnectionError as e:
            print('连接异常', e.args)


class WeiBoCookiesTester(BasicTester):
    def __init__(self, website):
        super(WeiBoCookiesTester, self).__init__(website)
        self.website = website

    def run(self):
        test_url = Settings.TEST_URL[self.website]
        cookies_group = self.DB_COOKIES.all()
        for usr, cookies in cookies_group.items():
            self.test(cookies, usr, test_url)
            time.sleep(self.TEST_DELAY)
