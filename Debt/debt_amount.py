import pandas as pd
import numpy as np
import re
import statistics

df = pd.read_csv("douban_posts_combine.csv")
debt_list = []

for title in df['Title']:
	# print(title)
	if re.search(r'([0-9]*\.[0-9]+|[0-9]+)[wW万]', title) is not None:
		match = re.search(r'([0-9]*\.[0-9]+|[0-9]+)[wW万]', title).group()
		print(match)
		debt_str = re.sub(r'[wW万]', '', match)
		debt = float(debt_str) * 10000
		debt_list.append(debt)
	elif re.search(r'([0-9]*\.[0-9]+|[0-9]+)[kK千]', title) is not None:
		match = re.search(r'([0-9]*\.[0-9]+|[0-9]+)[kK千]', title).group()
		print(match)
		debt_str = re.sub(r'[kK千]', '', match)
		debt = float(debt_str) * 1000
		debt_list.append(debt)

df_out = pd.DataFrame(debt_list,columns=['Debt Amount'])
df_out.to_csv("debt_amount.csv", index=False)

print("平均数为%f" % statistics.mean(debt_list))
print("中位数为%f" % statistics.median(debt_list))
print("众数为%f" % statistics.mode(debt_list))