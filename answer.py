from lxml import etree
import json

ans = {}
with open('1.json', 'r') as f:
    ans = json.load(f)
ff = open('answer.text', 'w+')
html = etree.parse('1.html', etree.HTMLParser())
nodes = html.xpath('//div[@class="field ui-field-contain"]')
keys = ans.keys()
for node in nodes:
    num = node.xpath('./@id')[0][3:]
    id = node.xpath('./@topic')[0]
    if int(id) < 3:
        continue
    if id in keys:
        s = '{}    {} \n'.format(str(int(num)-2), ans[id])
        ff.write(s)
    else:
        s = '{}    {} \n'.format(str(int(num)-2), '')
        ff.write(s)
ff.flush()
ff.close()

