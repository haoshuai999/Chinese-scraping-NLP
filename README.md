# Scrape data from douban, zhihu and calculate word frequency
Douban, similiar to IMDB, is a Chinese movie review website. People also talk about many different life issues on douban group. I scraped the posts and comments from the discussion page.
Zhihu, similiar to Quora, is a Chinese question-and-answer website. I scraped all the answers by analyzing JSON files from their API

## About the files
The file "douban.py" is used to scrape a list of posts from a douban group.\
The file "douban_post.py" and "zhihu.py" is used to scrape data.\
The file "word_division.py" is used to calculate the word frequency.\
The folder "Debt" is used for scraping a douban group about debt.
- The "douban.py", "douban_post.py" and "word_division.py" are similar to the files above
- The file "solution.py" is used to calculate the word frequency for a subset of the data
- The file "append_df.py" is used to concatenate the CSV files I scraped
- The file "debt_amount.py" is used to calculate how much debt people in the group owed