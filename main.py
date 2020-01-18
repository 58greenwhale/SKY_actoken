import requests
import execjs
import json
from Decode import AnalysiAES


class Decrypt(object):
    """
    新版解密四库一平台
    """

    def __init__(self):
        """
            创建request session对象用于保存cookie以及相同的用户访问
        """
        self.request = requests.session()
        with open('./js/fb.js', 'r', encoding='utf-8') as f:
            self.fb_js = f.read()
        with open('./js/zidingyi.js', 'r', encoding='utf-8') as f:
            self.two_decode = f.read()
        with open('./js/core.js', 'r', encoding='utf-8') as f:
            self.core_js = f.read()
        self.node = execjs.get('Node')
        self.fb = self.node.compile(self.fb_js, cwd=r'D:\nodejs\node-v12.13.0-win-x64\node_modules')
        self.decode = self.node.compile(self.two_decode)
        self.core = self.node.compile(self.core_js)
        self.bg_path = 'picture/bg.jpg'
        self.token = ''

    def start_sky(self):
        """
        第一次访问，并获取需要点击的验证码。
        :return:
        """
        url = 'http://jzsc.mohurd.gov.cn/data/company?complexname='
        header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'jzsc.mohurd.gov.cn',
            'Referer': 'https://www.google.com/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'

        }
        first_set_cookie = self.request.get(url, headers=header)
        self.get_check()

    def get_check(self):
        """
        获取网易验证码
        :return:
        """
        header = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Host': 'c.dun.163yun.com',
            'Referer': 'http://jzsc.mohurd.gov.cn/data/company?complexname=',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
        }
        post_data = {
            'id': 'c2e691560a1b4e76b71fd37eed97f46a',
            'fp': self.fb.call('xiangbeixx'),
            'https': 'false',
            'type': 'undefined',
            'version': '2.13.3',
            'dpr': '1.25',
            'dev': '1',
            'cb': self.core.call('get_cb'),
            'ipv6': 'false',
            'width': '0',
            'referer': 'http://jzsc.mohurd.gov.cn/data/company',
            'callback': '__JSONP'
        }
        url = 'http://c.dun.163yun.com/api/v2/get'
        catch = self.request.get(url=url, params=post_data, headers=header)
        data = json.loads(catch.text[8: -2])['data']
        self.token = data['token']
        if data['type'] == 3:
            response2 = self.request.get(url=data['bg'][0])
            with open(self.bg_path, 'wb') as f:
                f.write(response2.content)
            # return data['front']
        print(post_data)
        print(catch.text)


X = Decrypt()
X.start_sky()
# print(node.name)
# fb = node.compile(fb_js, cwd=r'D:\nodejs\node-v12.13.0-win-x64\node_modules')
