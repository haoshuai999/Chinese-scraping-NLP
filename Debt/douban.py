import lxml
import requests
import random
import socket
from lxml.html import fromstring

def scrape(url, post_urls):
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

	page_html_text = requests.get(url, headers=headers).text
	# print(page_html_text)
	page_html = fromstring(page_html_text)
	links = page_html.cssselect("table .title a")
	for link in links:
		post_urls.append(link.get('href'))

	return post_urls

if __name__ == '__main__':
	post_urls = []
	for i in range(120):
		print("scaping page %d" % (i + 1))
		url = "https://www.douban.com/group/678714/discussion?start=" + str(i*25)
		post_urls = scrape(url, post_urls)
		# print(post_urls)

	with open('douban_posts.txt', 'w') as f:
	    for item in post_urls:
	        f.write("%s\n" % item)