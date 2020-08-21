from CookiesPool.RedisControl import RedisClient
from CookiesPool.weibo.PhoneSMS import SMS
from selenium import webdriver
from conf import Settings
import time


class BasicGenerator:
    def __init__(self, website):
        self.DB_ACCOUNT = RedisClient(website, 'Account')
        self.DB_COOKIES = RedisClient(website, 'Cookies')

    def get_account(self):
        users = self.DB_ACCOUNT.all_usr()
        for user in users:
            yield user

    def save_cookie(self, usr, cookies):
        self.DB_COOKIES.set(usr, cookies)

    def generate(self, *args):
        raise SyntaxError('Please overwrite the <Function generate>')

    def run(self):
        raise SyntaxError('Please overwrite the <Function run>')


class WeiBoCookiesGenerator(BasicGenerator):
    def __init__(self, website, phone_number):
        super(WeiBoCookiesGenerator, self).__init__(website)
        self.phone_number = phone_number
        self.website = website

    def generate(self, account, phone_number, sms):
        usr, pwd = account, self.DB_ACCOUNT.get(account)
        try:
            chrome_option = webdriver.ChromeOptions()
            chrome_option.add_experimental_option('excludeSwitches', ['enable-automation'])
            driver = webdriver.Chrome(options=chrome_option)
        except Exception:
            raise Exception('Please configure the Chrome first')
        driver.delete_all_cookies()
        driver.get(Settings.GENERATOR_LOGIN_URL[self.website])
        time.sleep(1)
        driver.find_element_by_id('loginName').send_keys(usr)
        driver.find_element_by_id('loginPassword').send_keys(pwd)
        driver.find_element_by_id('loginAction').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="vdVerify"]/div[1]/div/div/div[4]/span/a').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="vdVerify"]/div[3]/div[2]/div[1]/div/div[1]/div/a').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('//*[@id="others"]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/span/input')\
            .send_keys(phone_number)
        driver.find_element_by_class_name('m-btn').click()
        sms.send()
        driver.find_element_by_xpath('//*[@id="msgVerify"]/div[1]/div/div/div[2]/a[2]').click()
        cookies = driver.get_cookies()
        print(cookies)
        self.save_cookie(usr, cookies)

    def run(self):
        accounts = self.get_account()
        for account in accounts:
            if account not in self.DB_COOKIES.all_usr():
                print('正在为账号：%s 生成Cookie......请稍后...' % account)
                sms_obj = SMS('1069009010021', 'DLYZ')
                self.generate(account, self.phone_number, sms_obj)
                print('账号：%s 生成Cookie成功！' % account)
                break
