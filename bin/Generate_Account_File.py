import sys


def run():
    with open('../libs/%s_account.txt' % sys.argv[1], 'w', encoding='utf-8') as f:
        for _ in range(3):
            f.write('账号----密码'+'\n')


if __name__ == '__main__':
    run()
