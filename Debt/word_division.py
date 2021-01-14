import jieba
import pandas as pd
import numpy as np
import re
from collections import Counter

jieba.load_userdict('userdict.txt')
df = pd.read_csv("douban_posts_combine.csv")

print(len(df))
count = 0
for index, row in df.iterrows():
	if isinstance(row['Title'], str) and isinstance(row['Post'], str) and isinstance(row['Reply'], str):
		if '疫情' in row['Title'] or '疫情' in row['Post'] or '疫情' in row['Reply'] or '新冠' in row['Title'] or '新冠' in row['Post'] or '新冠' in row['Reply']:
			count += 1

print(count)
all_texts = df['Title'].tolist() + df['Post'].tolist() + df['Reply'].tolist()

cut_words = ""
for text in all_texts:
	if isinstance(text, str):
		text = re.sub(r'[^\w\s]','',text)
		seg_list = jieba.cut(text)
		cut_words += (" ".join(seg_list))

all_words = cut_words.split()
# print(all_words)
c = Counter()
for x in all_words:
	if len(x)>1 and x != '\r\n':
		c[x] += 1

print('\nResult：')
with open('frequency.txt', 'w', encoding='utf-8') as f:
	for (k,v) in c.most_common():
		print("%s:%d" % (k, v))
		f.write("%s:%d\n" % (k, v))



