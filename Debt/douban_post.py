import lxml
import requests
import csv
import random
import time
import socket
import pandas as pd
from lxml.html import fromstring

def scrape(url):
	socket.setdefaulttimeout(5)

	user_agent_list = [
		"Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
		"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
		"Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML, likeGecko)Chrome / 17.0.963.56Safari / 535.11"
	]

	f = open("http_proxies.txt", "r")
	proxy_list = f.readlines()
	
	# proxy_list = ['socks5h://199.255.96.233:8080']
	proxy = random.choice(proxy_list)

	# print(proxy)
	proxies = {"http": proxy}

	headers = {
		'User-Agent': random.choice(user_agent_list)
	}
	
	print(url)
	reply_text = []
	try:
		page_html_text = requests.get(url, headers=headers, proxies = proxies).text
	except:
		print("not using proxy %s", proxy)
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
			reply_text.append(text.text_content().strip())
	except:
		reply = ''


	return (time_text, title_text, main_post_text, reply_text)

if __name__ == '__main__':
	f = open("douban_posts.txt", "r")
	urls = f.readlines()
	urls = [line.rstrip('\n') for line in urls]
	print(len(urls))
	time_array = []
	title_array = []
	post_array = []
	reply_array = []
	count = 0
	# print(urls[500:])
	for url in urls[2680:]:
		count += 1
		date, title, post, reply = scrape(url)
		time_array.append(date)
		title_array.append(title)
		post_array.append(post)
		reply_array.append(reply)
		if count % 50 == 0:
			print(count)
			print("output csv")
			df = pd.DataFrame(list(zip(time_array, title_array, post_array, reply_array)), columns=['Time', 'Title', 'Post', 'Reply'])
			df.to_csv("douban_posts10.csv", index=False, encoding='utf_8_sig')
			time.sleep(10)
			

	df = pd.DataFrame(list(zip(time_array, title_array, post_array, reply_array)), columns=['Time', 'Title', 'Post', 'Reply'])
	df.to_csv("douban_posts10.csv", index=False, encoding='utf_8_sig')
