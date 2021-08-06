import  requests
headers = {}
with open('header2', 'r') as f:
    for s in f.readlines():
        arr = s.split(':')
        headers[arr[0].strip()] = arr[1].strip()

print(requests.get(url='https://ks.wjx.top/wjx/join/completemobile2.aspx?activityid=mFhmwDW&joinactivity=110055244577&sojumpindex=17&tvd=2NrwsglfDx0%3d&costtime=33&comsign=2A33A12740CCA2977357CDB0CD2401EA74F0E5D9',headers=headers).text)