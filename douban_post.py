import lxml
import requests
import csv
import random
import pandas as pd
from lxml.html import fromstring

def scrape(url):
	user_agent_list = [
		"Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
		"Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1)",
		"Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11",
		"Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML, likeGecko)Chrome / 17.0.963.56Safari / 535.11",
		"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)",
		"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)"
	]


	headers = {
		'User-Agent': random.choice(user_agent_list)
	}
	print(url)
	all_post_text = []
	page_html_text = requests.get(url, headers=headers).text
	page_html = fromstring(page_html_text)
	title = page_html.cssselect("title")[0]
	title_text = title.text_content().strip()
	time = page_html.cssselect(".color-green")[0]
	time_text = time.text_content()
	try:
		main_post = page_html.cssselect(".topic-content p")[0]
		main_post_text = main_post.text_content().strip()
	except:
		main_post_text = ''
	
	try:
		reply = page_html.cssselect(".reply-content")
		for text in reply:
			all_post_text.append(text.text_content().strip())
	except:
		reply = ''

	all_post_text.append(title_text)
	all_post_text.append(main_post_text)

	return (time_text,all_post_text)

if __name__ == '__main__':
	f = open("douban_post.txt", "r")
	urls = f.readlines()
	urls = [line.rstrip('\n') for line in urls]
	time_array = []
	post_array = []
	count = 0
	for url in urls:
		count += 1
		time, post =scrape(url)
		time_array.append(time)
		post_array.append(post)
		if count % 10 == 0:
			print("output csv")
			df = pd.DataFrame(list(zip(time_array, post_array)), columns=['Time', 'Post'])
			df.to_csv("douban_post.csv", index=False, encoding='gb18030')

	df = pd.DataFrame(list(zip(time_array, post_array)), columns=['Time', 'Post'])
	df.to_csv("douban_post.csv", index=False, encoding='gb18030')
