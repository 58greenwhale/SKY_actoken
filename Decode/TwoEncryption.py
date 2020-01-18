import requests
import execjs
import json
from startSIKUYI.AnalysisDataPackge import AnalysiAES


with open('zidingyi.js', 'r', encoding='utf-8') as f:
    source = f.read()
node = execjs.get('Node')
validate = 'Vqs1w94kbtmKQF7r0khDncumaGD4ZBrmwTvzEtYflVO7M4gSuBNAZlGQZAfac52lemymj0l+h7DExKKNQie/epYZ2Vlj9Z9jyEIcYLV0KSY9eIHb4mI90xic6zFblliBsDPgOJY3lithNvYZRzzlzlG2RQk0pO3P9Y0gaN5uWjk='
fb = r'xiaykr2QauSRU0d1MSd808YiDfU4uY/p44tq7uf/dyhrWQtLY5nZcNB/xNsNUe\1lpLYy8JwZQPm4+/7jvNuw7SfWoI5IvgO6fOksB/kAWXVXrvCdV4DraE3ehG8daOAR3k+Vy\X3Ac2WfKyqc+JVGPTJRebjp5lyTqnmXouOIf09e6h:1579157300412'
core = node.compile(source)
cb = core.call('xiangbei', validate, fb)

headers = {'Accept': 'application/json, text/plain, */*',
           'Accept-Language': 'zh-CN,zh;q=0.9',
           'Content-Type': 'application/x-www-form-urlencoded',
           'Origin': 'http://jzsc.mohurd.gov.cn',
           'Referer': 'http://jzsc.mohurd.gov.cn/data/company?complexname=',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
           }
data = {
    'NECaptchaValidate': cb
}
result = requests.post(url='http://jzsc.mohurd.gov.cn/api/webApi/captchaVerifier/verify', headers=headers, data=data)
