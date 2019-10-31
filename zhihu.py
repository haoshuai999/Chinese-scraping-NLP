import urllib
import json
import csv
import re
import pandas as pd


def read_json(url):
	with urllib.request.urlopen(url) as url:
		data = json.loads(url.read().decode())
		all_data = data['data']
		next_url = data['paging']['next']
		# print(next_url)
		for entry in all_data:
			post = entry['content'].replace('<br/>', '').replace('<p>', '').replace('</p>', '').replace('<b>',
																										'').replace(
				'</b>', '')
			post = re.sub(r'<figure>(.*)<\/figure>', '', post, flags=re.DOTALL)
			post = re.sub(r'<figure data-size="normal">(.*)<\/figure>', '', post, flags=re.DOTALL)
			post = re.sub(r'<a(.*)<\/a>', '', post, flags=re.DOTALL)
			all_posts.append(post)
	return (next_url, all_posts)


if __name__ == '__main__':
	url_p1 = "https://www.zhihu.com/api/v4/questions/"
	url_p2 = "/answers?include=data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled,is_recognized,paid_info,paid_info_content;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics&limit=10&offset=0&platform=desktop&sort_by=default"
	post_id = ['29273149','21280068','347817291']
	for str in post_id:
		all_posts = []
		url = url_p1 + str + url_p2
		if str == '29273149':
			for i in range(164):
				url, all_posts = read_json(url)
		elif str == '21280068':
			for i in range(160):
				url, all_posts = read_json(url)
		else:
			for i in range(8):
				url, all_posts = read_json(url)
		df = pd.DataFrame(all_posts)
		df.to_csv("zhihu_post_"+ str + ".csv", index=False, encoding='gb18030')
