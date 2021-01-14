import jieba
import pandas as pd
import numpy as np
import re
from collections import Counter

jieba.load_userdict('userdict.txt')
df = pd.read_csv("douban_posts_combine.csv", encoding='utf_8_sig')
all_titles = df['Title'].tolist()
other_content = df['Post'].tolist() + df['Reply'].tolist()

df_solution = df[df['Title'].str.contains(r'(上岸|建议)')]
df_solution.to_csv("debt_solution2.csv", index=False, encoding='utf_8_sig')

cut_words = ""
for index, row in df.iterrows():
	if re.search(r'(上岸|建议)', row['Title']):
		print(row['Title'])
		if isinstance(row['Post'], str) and isinstance(row['Reply'], str):
			text = re.sub(r'[^\w\s]','', row['Post']) + re.sub(r'[^\w\s]','', row['Reply'])
			seg_list = jieba.cut(text)
			cut_words += (" ".join(seg_list))

all_words = cut_words.split()
# print(all_words)
c = Counter()
for x in all_words:
	if len(x)>1 and x != '\r\n':
		c[x] += 1

print('\nResult：')
with open('solution_frequency2.txt', 'w', encoding='utf-8') as f:
	for (k,v) in c.most_common():
		print("%s:%d" % (k, v))
		f.write("%s:%d\n" % (k, v))



