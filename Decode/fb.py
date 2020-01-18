import requests
import execjs
import json

with open(r'E:\DecryptSKY\xiangbei.min.js', 'r', encoding='utf-8') as f:
    source = f.read()

node = execjs.get('Node')
# print(node.name)
core = node.compile(source, cwd=r'D:\nodejs\node-v12.13.0-win-x64\node_modules')
# core = node.compile(source)
fb = core.call('xiangbeiActoken')
print(fb)
