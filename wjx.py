import requests
import re
import time
import random


class wenjuanxing(object):
    def __init__(self, url, choice, proxies=None):
        self.proxies = proxies
        self.wj_url = url
        self.post_url = None
        self.header1 = {
            "Connection": 'close',
            "Cache-Control": 'max-age=0',
            "sec-ch-ua": '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
            "sec-ch-ua-mobile": '?0',
            "Upgrade-Insecure-Requests": '1',
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
            "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            "Sec-Fetch-Site": 'none',
            "Sec-Fetch-Mode": 'navigate',
            "Sec-Fetch-User": '?1',
            "Sec-Fetch-Dest": 'document',
            "Referer": 'https://ks.wjx.top/',
            "Accept-Encoding": 'gzip, deflate',
            "Accept-Language": 'zh-CN,zh;q=0.9,en-CN;q=0.8,en;q=0.7'
        }
        self.header2 = {
            "Connection": 'close',
            "Content-Length": '79',
            "sec-ch-ua": '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
            "Accept": 'text/plain, */*; q=0.01',
            "X-Requested-With": 'XMLHttpRequest',
            "sec-ch-ua-mobile": '?0',
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
            "Content-Type": 'application/x-www-form-urlencoded; charset=UTF-8',
            "Origin": 'https://www.wjx.cn',
            "Sec-Fetch-Site": 'same-origin',
            "Sec-Fetch-Mode": 'cors',
            "Sec-Fetch-Dest": 'empty',
            "Referer": 'https://www.wjx.cn/vm/wFQmBUU.aspx',
            "Accept-Encoding": 'gzip, deflate',
            "Accept-Language": 'zh-CN,zh;q=0.9,en-CN;q=0.8,en;q=0.7'
        }
        self.data = {
            'submitdata': choice
        }

    def get_ktimes(self):
        """
        随机生成一个ktimes,ktimes是构造post_url需要的参数，为一个整数
        :return:
        """
        self.ktimes = random.randint(50, 100)
        return self.ktimes

    def get_response(self):
        """
        访问问卷网页，获取网页代码
        :return: get请求返回的response
        """
        session = requests.Session()
        response = session.get(url=self.wj_url, headers=self.header1, proxies=self.proxies)
        self.session = session
        self.response = response
        return response

    def get_jqnonce(self):
        """
        通过正则表达式找出jqnonce,jqnonce是构造post_url需要的参数
        :return: 找到的jqnonce
        """
        jqnonce = re.search(r'.{8}-.{4}-.{4}-.{4}-.{12}', self.response.text)
        return jqnonce.group()

    def get_rn(self):
        """
        通过正则表达式找出rn,rn是构造post_url需要的参数
        :return: 找到的rn
        """
        self.rn = re.search(r'\d{9,10}\.\d{8}', self.response.text).group()
        return self.rn

    def distanc(self, a):
        result = []
        b = self.ktimes % 10
        if b == 0:
            b = 1
        for char in list(a):
            f = ord(char) ^ b
            result.append(chr(f))
        return ''.join(result)

    def get_id(self):
        """
        通过正则表达式找出问卷id,问卷是构造post_url需要的参数
        :return: 找到的问卷id
        """
        self.id = re.search(r'(?<=activityId \=)\d+', self.response.text).group()
        return self.id

    def get_start_time(self):
        """
        通过正则表达式找出问卷starttime,问卷是构造post_url需要的参数
        :return: 找到的starttime
        """
        self.start_time = re.search(r'\d+?/\d+?/\d+?\s\d+?:\d{2}:\d{2}', self.response.text).group()
        return self.start_time

    def get_rname(self):
        return re.search('(?<=2\$).*?(?=\}3)', self.data["submitdata"]).group()

    def get_jqParam(self):
        """
        使用 rn,starttime,activityId三个参数
        :return:  jqParam的值
        """
        le = int(self.rn.split(".")[0])
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
        starttime = int((time.mktime(time.strptime(self.start_time, '%Y/%m/%d %X'))) * 1000)
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
        littleEndian = fn + locaOffset + int(self.id)

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

    def set_post_url(self):
        """
        生成post_url
        :return:
        """

        self.get_response()  # 获取response
        start_time = self.get_start_time()  # 获取starttime
        ktimes = self.get_ktimes()  # 获取ktimes
        rname = self.get_rname()  # 获取rname
        print(rname)
        jqnonce = self.get_jqnonce()  # 获取jqnonce
        rn = self.get_rn()  # 获取rn
        id = self.get_id()  # 获取问卷id
        jqsign = self.distanc(jqnonce)  # 获取jqsign
        jcn = self.distanc(rname)  # 获取jcn
        jqParam = self.get_jqParam()  # 获取jqParam
        t = '{}{}'.format(int(time.time()), random.randint(100, 200))  # 生成一个时间戳，最后三位为随机数
        lct = self.get_ktimes()  # 获取lct
        url = f'https://www.wjx.cn/vm/Yfd6yGW.aspx&starttime={start_time}&source=directphone&submittype=1&ktimes={ktimes}&hlv=1&rn={rn}&jqpram={jqParam}&jcn={jcn}&t={t}&jqnonce={jqnonce}&jqsign={jqsign}'
        self.post_url = url  # 设置url
        print(self.post_url)

    def post_data(self):
        """
        发送数据给服务器
        :return: 服务器返回的结果
        """
        session = self.session
        response = session.post(url=self.post_url, data=self.data, headers=self.header2, proxies=self.proxies)
        return response

    def run(self):
        """
        填写一次问卷
        :return:
        """
        self.set_post_url()
        result = self.post_data()
        print(result.text)


for j in range(0, 5):
    submessage = "1$侧记大}2$1}3$1"
    w = wenjuanxing('https://www.wjx.cn/vm/mFhmwDW.aspx', submessage)
    try:
        w.run()
    except:
        pass
