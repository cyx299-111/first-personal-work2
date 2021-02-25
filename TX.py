import re
import urllib.request
import random
import time


#构建用户代理
uapools = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0",
    ]

#从用户代理池随机选取一个用户代理
def ua(uapools):
    thisua=random.choice(uapools)
    #print(thisua)
    headers=("User-Agent",thisua)
    opener=urllib.request.build_opener()
    opener.addheaders=[headers]
    #设置为全局变量
    urllib.request.install_opener(opener)
 
def get_comment(html):  # 爬取单页评论
    pat = '"content":"(.*?)"'
    comment = re.compile(pat, re.S).findall( html)
    return comment

def get_lastId(html):  # 获取lastId
    pat = '"last":"(.*?)"'
    lastId = re.compile(pat,re.S).findall(html)[0]
    # print(lastId)
    return lastId

def saveData(comment):
    with open("comments.txt", "a+", encoding="utf-8") as file:
        # file.write(str(comment))
        for i in comment:
            i = i.replace("\n", "")
            file.write(i)
            file.write("\n")

def main():
    lastId = "0"
    page = "1614130891759"
    ua(uapools)
    
    for i in range(0, 12699//10):
        time.sleep(1)
        url = "https://video.coral.qq.com/varticle/5963120294/comment/v2?callback=_varticle5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor=" + lastId + "&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132&_=" + str(page)
        html = urllib.request.urlopen(url).read().decode("utf-8")  # 获取网页
        comment = get_comment(html)  # 获取评论
        # print(comment)
        saveData(comment)  # 保存评论
        lastId = get_lastId(html)  # 获取lastId
        page = int(page) + 1
        print(page)
            
main()