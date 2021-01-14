import pandas as pd 

df = pd.read_csv("douban_posts.csv")

for i in range(10):
	if i > 1:
		print(i)
		df_temp = pd.read_csv("douban_posts" + str(i) + ".csv")
		df = df.append(df_temp)

print(df)
df.to_csv("douban_posts_combine.csv", index=False, encoding='utf_8_sig')