import requests, json, re, time, random
from lxml import etree


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


judge = {
    '错': '2',
    '对': '1'
}
select = {
    'A': '1',
    'B': '2',
    'C': '3',
    'D': '4'
}
headers = {}
with open('header2', 'r') as f:
    for s in f.readlines():
        arr = s.split(':')
        headers[arr[0].strip()] = arr[1].strip()

ans = {}
with open('1.json', 'r') as f:
    ans = json.load(f)

html = etree.parse('1.html', etree.HTMLParser())
text = etree.tostring(html).decode()
nodes = html.xpath('//div[@class="field ui-field-contain"]')
keys = ans.keys()
questAns = {}
questAns['1'] = "哈哈"
questAns['2'] = '2333'
for node in nodes:
    id = node.xpath('./@topic')[0]
    if int(id) < 3:
        continue
    if id in keys:
        if len(ans[id][0]) == 1:
            questAns[id] = judge[ans[id][0]]
        elif len(ans[id][0]) == 0:
            questAns[id] = -2
        else:
            if ans[id][0].find('┋') > 0:
                aaa = ''
                for s in ans[id][0].split('┋'):
                    aaa += select[str(s.strip()[0])]
                questAns[id] = aaa
            else:
                questAns[id] = select[ans[id][0].strip()[0]]
list1 = sorted(int(a) for a in questAns.keys())
ansS = ''
for num in list1:
    ansS += '{}${}'.format(num, questAns[str(num)]) + '}'
ansS = ansS[:-1]
qtr = {}
with open('qtr', 'r') as f:
    for s in f.readlines():
        arr = s.split(':')
        qtr[arr[0].strip()] = arr[1].strip()
activityId = '126512813'
shortid = 'PM73IkN'
jqnonce = re.search(r'.{8}-.{4}-.{4}-.{4}-.{12}', text).group()
ktimes = random.randint(30, 60)

starttime = re.search(r'\d+?/\d+?/\d+?\s\d+?:\d{2}:\d{2}', text).group()
rn = re.search(r'\d{9,10}\.\d{8}', text).group()
qtr['shortid'] = shortid
qtr['t'] = time_stamp = '{}{}'.format(int(time.time()), random.randint(100, 200))
qtr['starttime'] = starttime
qtr['ktimes'] = ktimes
qtr['rn'] = rn
qtr['jcn'] = dan(ktimes,questAns['1'])
qtr['jqpram'] = get_jqParam(rn, starttime, activityId)
qtr['jqnonce'] = jqnonce
qtr['jqsign'] = dan(ktimes, jqnonce)
print(qtr)
print(ansS)
res=requests.post(url='https://ks.wjx.top/joinnew/processjq.ashx', headers=headers, data=ansS)
print(res.text)
