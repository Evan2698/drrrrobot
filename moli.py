import requests
#response = urllib.request.urlopen('http://www.baidu.com')
#print(response.read())


def ask_question(msg):
    url = 'http://i.itpk.cn/api.php?question=%s'%(msg)
    ret = requests.get(url)
    if ret.status_code == 200:        
        return ret.text
    return "我就是不想回答你～～～."
