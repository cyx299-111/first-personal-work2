import jieba
import json

txt = open("comments.txt", "r", encoding='utf-8').read()
words  = jieba.lcut(txt)

dataDict = {}
countList = []

# 创建停用词列表
stopwords = [line.strip() for line in open('stop_words.txt', encoding='UTF-8').readlines()]

outlist = []
for word in words:
    if word in stopwords:
        continue
    else:
        outlist.append(word)

# 统计词语出现次数
counts = {}

for word in words:
     if len(word) == 1:
         continue
     else:
        counts[word] = counts.get(word,0) + 1

items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) 
countList = []
for i in range(len(items)):
    countDict = {}
    word, count = items[i]
    if count >= 10:
        countDict['name'] = word
        countDict['value'] = count
        countList.append(countDict)

data = {}
data['data'] = countList
print(data)
with open('comments.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
