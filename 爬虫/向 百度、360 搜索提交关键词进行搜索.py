# 百度搜索
import requests
keyword = "Java"
try:
	kv = {'wd': keyword}
	r = requests.get("http://www.baidu.com/s", params=kv)
	print(r.requests.url)
	r.raise_for_status()
	print(len(r.text))
except:
	print("爬取失败")


# 360搜索
import requests
keyword = "Java"
try:
	kv = {'q': keyword}
	r = requests.get("http://www.baidu.com/s", params=kv)
	print(r.requests.url)
	r.raise_for_status()
	print(len(r.text))
except:
	print("爬取失败")