import requests
import re
import time
headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"
}
skey = 'SCU112948T8f1a1f8df0635cadde3c3d5904c122cc5f58e93c25346'  # 你的server酱skey

url = 'https://www.52pojie.cn/forum.php?mod=forumdisplay&fid=24&filter=author&orderby=dateline&typeid=29'

def push():
    server_url = "https://sc.ftqq.com/%s.send" % skey
    res = getHTMLText2(url)
    des = re.findall('class="s xst">(.*?)</a>', res)[0]
    print(des)
    params = {
        "text": '爷，您关注的帖子更新啦！',
        "desp": des
    }
    response = requests.get(server_url, params=params)
    json_data = response.json()
    if json_data['errno'] == 0:
        print(" 推送成功。")
    else:
        print("推送失败")


def getHTMLText(url):
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()  # 如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "网站访问异常"


def main(*args):
    res1 = getHTMLText(url)
    id = re.findall('tbody id="(.*?)">', res1)[1] #正则匹配id
    print(id)
    time.sleep(880)  #等待
    res = getHTMLText(url)
    id2 = re.findall('tbody id="(.*?)"', res)[1] #正则匹配id
    print(id2)
    if id == id2:
        print("暂无帖子更新")
    else:
        push()
        print('爷，您关注的帖子更新啦！')



if __name__ == "__main__":
    main()
    getHTMLText(url)
