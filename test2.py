import re

import requests, json, time, random, selenium
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
    p3 = ~~int(state / p1)
    node1 = le & node
    index = state & node
    p4 = p2 ^ p3
    item = node1 ^ index
    locaOffset = (p4 * p1) + item
    starttime = int((time.mktime(time.strptime(start_time, '%Y/%m/%d %H:%M:%S'))) * 1000)
    print(starttime)
    # starttime=1628075946440
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
        if littleEndian - 62 < 0:
            return preCloseCallbackResult[littleEndian]
        else:
            p1 = littleEndian % 62
            p2 = int(littleEndian / 62)
            return abcd3(p2, preCloseCallbackResult) + preCloseCallbackResult[p1]

    jqparam = abcd3(littleEndian, preCloseCallbackResult)
    print('*'*3,jqparam)
    item = 0
    map = list(jqparam)
    for i in range(0, len(jqparam)):
        item += ord(map[i])
    el = len(jqparam)

    selected = item % el
    el1 = []
    for i in range(selected, el):
        el1.append(map[i])
    for i in range(0, selected):
        el1.append(map[i])
    jqparam = "".join(el1)
    return jqparam


ktimes = 46
jqnonce = '2cdb7fe5-27e8-428e-945b-79baaadb8257'
rn = '1886775139.87896948'
stt = '2021/8/6 23:39:57'
#'2021-08-05 22:05:07'
#1628172307000
#1628172307000
id1 = '126547691'
#2038388918
print(dan(ktimes, jqnonce))
print(dan(ktimes, '线不行'))
print(get_jqParam(rn, stt, id1))
