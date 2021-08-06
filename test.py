import re

import requests, json, time, random, selenium
from lxml import etree

session = requests.session()


def dan(ktimes, jqnonce):
    result = []
    b = ktimes % 10
    if b == 0:
        b = 1
    for char in list(jqnonce):
        f = ord(char) ^ b
        result.append(chr(f))
    return ''.join(result)


def get_jqParam(rn, start_time, id1):
    """
    使用 rn,starttime,activityId三个参数
    :return:  jqParam的值
    """
    le = int(rn.split(".")[0])
    state = 3597397
    p1 = 2147483648
    node = 2147483647
    p2 = ~~int(le / p1)
    p3 = 0
    node1 = le & node
    index = 3597397
    p4 = p2 ^ 0
    item = node1 ^ index
    locaOffset = (p4 * p1) + item
    starttime = int((time.mktime(time.strptime(start_time, '%Y/%m/%d %X'))) * 1000)
    offset = int(starttime / 1000)
    node = str(offset)
    if (offset % 10) > 0:
        node = node[::-1]
    fn = int(node + "89123")
    value = list(str(fn) + str(locaOffset))
    a = "kgESOLJUbB2fCteoQdYmXvF8j9IZs3K0i6w75VcDnG14WAyaxNqPuRlpTHMrhz"
    result = list(a)
    id = len(result)
    for i in range(0, len(value)):
        try:
            key = int(value[i])
        except:
            pass
        value1 = result[key]
        el = result[id - 1 - key]
        result[key] = el
        result[id - 1 - key] = value1
    a = "".join(result)
    preCloseCallbackResult = a
    littleEndian = fn + locaOffset + int(id1)

    def abcd3(littleEndian, preCloseCallbackResult):
        while True:
            if littleEndian - 62 < 0:
                return preCloseCallbackResult[littleEndian]
            else:
                p1 = littleEndian % 62
                p2 = int(littleEndian / 62)
                return abcd3(p2, preCloseCallbackResult) + preCloseCallbackResult[p1]

    jqparam = abcd3(littleEndian, preCloseCallbackResult)
    item = 0
    map = list(jqparam)
    for i in range(0, len(jqparam)):
        item = item + ord(map[i])
    el = len(jqparam)
    selected = item % el
    el1 = []
    for i in range(selected, el):
        el1.append(map[i])
    for i in range(0, selected):
        el1.append(map[i])
    jqparam = "".join(el1)
    return jqparam

ip = '{}.{}.{}.{}'.format(112, random.randint(64, 68), random.randint(0, 255), random.randint(0, 255))
headers = {
    'X-Forwarded-For': ip,

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko\) Chrome/71.0.3578.98 Safari/537.36',

}
qtr = {}
ans = ''
# with open('header', 'r') as f:
#     for s in f.readlines():
#         arr = s.split(':')
#         headers[arr[0].strip()] = arr[1].strip()
url = 'https://ks.wjx.top/vm/mFhmwDW.aspx'
res = session.get(url, headers=headers)
cookies = res.headers['Set-Cookie']
text = res.text
html = etree.HTML(text)

with open('qtr', 'r') as f:
    for s in f.readlines():
        arr = s.split(':')
        qtr[arr[0].strip()] = arr[1].strip()
activityId = re.search(r'(?<=jac)\d+', cookies).group()
print(activityId)
jqnonce = re.search(r'.{8}-.{4}-.{4}-.{4}-.{12}', text).group()
ktimes = random.randint(30, 60)
shortid = url.split('/')[-1].split('.')[0]
starttime = re.search(r'\d+?/\d+?/\d+?\s\d+?:\d{2}:\d{2}', text).group()
rn = re.search(r'\d{9,10}\.\d{8}', text).group()
qtr['shortid'] = shortid
qtr['t'] = time_stamp = '{}{}'.format(int(time.time()), random.randint(100, 200))
qtr['starttime'] = starttime
qtr['ktimes'] = ktimes
qtr['rn'] = rn

qtr['jqpram'] = get_jqParam(rn, starttime, activityId)
qtr['jqnonce'] = jqnonce
qtr['jqsign'] = dan(ktimes, jqnonce)

nodes = html.xpath('//div[@class="field ui-field-contain"]')
dic = {}
for node in nodes:
    id = node.xpath('./@topic')[0]
    if id == '1':
        dic[id] = '线不行'
    elif id == '2':
        dic[id] = '1'
    else:
        dic[id] = '1'
qtr['jcn'] = dan(ktimes, dic['1'])
print(qtr)
sortkey = sorted(int(a) for a in dic.keys())
for num in sortkey:
    ans += '{}${}'.format(num, dic[str(num)]) + '}'
urlpost = 'https://ks.wjx.top/joinnew/processjq.ashx'
print(ans[:-1])
res = session.post(url=urlpost, params=qtr, data={'submitdata': ans[:-1]})
print(res.text)
