from lxml import etree
import os, json,openpyxl

with open('1.json', 'r') as f:
    ans = json.load(f)

for html in os.listdir('answer'):
    htm = etree.parse(os.path.join('answer', html), etree.HTMLParser())
    nodes = htm.xpath('//div[@class="data__items"]')
    print(len(nodes))
    for node in nodes:
        id = node.xpath('./@topic')[0]
        if int(id) < 3:
            continue
        answer = node.xpath('./div[@class="data__key"]/div/div[@class="answer-ansys"]/div/text()')
        ans[id] = answer



with open('1.json', 'w+') as f:
    json.dump(ans, f)
