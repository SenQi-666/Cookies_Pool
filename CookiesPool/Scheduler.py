from multiprocessing import Process
from CookiesPool.Generator import *
from CookiesPool.Tester import *
from CookiesPool.API import app
from conf import Settings
import time


class Dispatch:
    def __init__(self):
        self.GENERATOR_MAP = Settings.GENERATOR_MAP
        self.GENERATOR_DELAY = Settings.GENERATOR_DELAY
        self.TESTER_MAP = Settings.TESTER_MAP
        self.TESTER_DELAY = Settings.TESTER_DELAY
        self.HOST = Settings.API_HOST
        self.PORT = Settings.API_PORT
        self.GENERATOR_PROCESS = Settings.GENERATOR_PROCESS
        self.TESTER_PROCESS = Settings.TESTER_PROCESS
        self.API_PROCESS = Settings.API_PROCESS
        self.PHONE_NUMBER = Settings.PHONE_NUMBER

    def cookies_generate(self):
        while True:
            print('开始生成Cookies......')
            try:
                for website, cls in self.GENERATOR_MAP.items():
                    print('%s 站点的Cookies正在生成中，请稍后......' % website)
                    generator = eval(cls+'(%s, %s)' % (website, self.PHONE_NUMBER))
                    generator.run()
                    print('%s 站点的Cookies生成完成' % website)
                    time.sleep(self.GENERATOR_DELAY)
            except Exception as e:
                print(e.args)

    def cookies_tester(self):
        while True:
            print('开始检测Cookies......')
            try:
                for website, cls in self.TESTER_MAP.items():
                    print('正在检测 %s 站点的Cookies，请稍后......' % website)
                    tester = eval(cls+'(%s)' % website)
                    tester.run()
                    print('%s 站点的Cookies检测完成' % website)
                    time.sleep(self.TESTER_DELAY)
            except Exception as e:
                print(e.args)

    def api(self):
        print('API接口开始运行......')
        app.run(host=self.HOST, port=self.PORT)

    def run(self):
        if self.GENERATOR_PROCESS:
            generator_process = Process(target=self.cookies_generate)
            generator_process.start()

        if self.TESTER_PROCESS:
            tester_process = Process(target=self.cookies_tester)
            tester_process.start()

        if self.API_PROCESS:
            api_process = Process(target=self.api)
            api_process.start()
