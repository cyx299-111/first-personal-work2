import io
import jieba
import json

txt = io.open("comments.txt", "r", encoding='utf-8').read()
words  = jieba.lcut(txt)

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
