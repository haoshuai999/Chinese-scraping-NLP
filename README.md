# Scrape data from douban, zhihu and calculate word frequency
Douban, similiar to IMDB, is a Chinese movie review website. People also talk about many different life issues on douban group. I scraped the posts and comments from the discussion page.
Zhihu, similiar to Quora, is a Chinese question-and-answer website. I scraped all the answers by analyzing JSON files from their API

## About the files
The file douban.py is used to scrape a list of posts from a douban group.\
The file douban_post.py and zhihu.py is used to scrape data.\
The file word_division.py is used to calculate the word frequency.