import jieba
import pandas as pd
import re
from collections import Counter

jieba.load_userdict('userdict.txt')
df = pd.read_csv("zhihu_post_part2.csv", encoding='gb18030')
all_texts = df['Posts'].tolist()

cut_words = ""
for text in all_texts:
	text = re.sub("[A-Za-z0-9\：\·\—\，\。\“ \” \！ \[ \] ]", "", text)
	seg_list = jieba.cut(text)
	cut_words += (" ".join(seg_list))

all_words = cut_words.split()
# print(all_words)
c = Counter()
for x in all_words:
	if len(x)>1 and x != '\r\n':
		c[x] += 1

print('\nResult：')
with open('frequency_part2.txt', 'w', encoding='gb18030') as f:
	for (k,v) in c.most_common():
		print("%s:%d" % (k, v))
		f.write("%s:%d\n" % (k, v))



