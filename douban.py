import lxml
import requests
from lxml.html import fromstring

def scrape(urls, post_urls):
	page_html_text = requests.get(urls).text
	# print(page_html_text)
	page_html = fromstring(page_html_text)
	links = page_html.cssselect("table .title a")
	for link in links:
		post_urls.append(link.get('href'))

	return post_urls

if __name__ == '__main__':
	post_urls = []
	for i in range(98):
		print("scaping page %d" % i)
		urls = "https://www.douban.com/group/painmc/discussion?start=" + str(i*25)
		post_urls = scrape(urls, post_urls)
		# print(post_urls)

	with open('douban_post.txt', 'w') as f:
	    for item in post_urls:
	        f.write("%s\n" % item)