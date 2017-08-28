import re
 
string = "http://weibo.com/u/3107069674?refer_flag=1087030701_2976_2006_7&is_all=1"
pattern = re.compile("http://weibo.com/u/(.*?)\?")
items = re.findall(pattern, string)
print items