from CookiesPool.RedisControl import RedisClient
import os


class Save:
    def __init__(self):
        self.website = None

    def read_account(self):
        with open('../libs/%s_account.txt' % self.website, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                new_line = line.replace('\n', '')
                split_lst = new_line.split('----')
                usr, pwd = split_lst[0], split_lst[1]
                yield usr, pwd

    def save_account(self):
        conn = RedisClient(website=self.website, kind='Account')
        account_info = self.read_account()
        for usr, pwd in account_info:
            print('正在存储账号: %s，密码为：%s' % (usr, pwd))
            conn.set(usr, pwd)
            print('账号: %s 存储成功' % usr)

    def run(self):
        parent_dir = os.path.dirname(os.path.dirname(__file__))
        for fileName in os.listdir(os.path.join(parent_dir, 'libs')):
            if 'account.txt' in fileName:
                self.website = fileName.split('_')[0]

        if self.website:
            self.save_account()
        else:
            raise NotImplementedError('Please run the command < $ python3 Generate_Account_File.py website > first')
