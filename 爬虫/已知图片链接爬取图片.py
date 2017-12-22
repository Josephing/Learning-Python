import requests
import os
url = "http://img0.dili360.com/rw17/ga/M01/02/E5/wKgBzFQ3PamAKFjyAAmhm4OCs9k158.jpg"
root = "D://pics//"
path = root + url.split('/')[-1]
try:
	if not os.path.exists(root):
		os.mkdir(root)
	if not os.path.exists(path):
		r = requests.get(url)
		with open(path, 'wb') as f:
			f.write(r.content)
			f.close()
			print("文件保存成功")
	else:
		print("文件已存在")
except:
	print("爬取失败")