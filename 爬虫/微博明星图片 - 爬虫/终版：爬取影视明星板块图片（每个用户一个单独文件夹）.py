# -*- coding: utf-8 -*-

import sys
import os
import urllib
import urllib2
import cookielib
import base64
import re
import json
import rsa
import binascii
import threading, requests, math, random
#from bs4 import BeautifulSoup

mx=raw_input("输入要爬的起始页码：".decode('utf-8').encode('gbk'))
my=raw_input("输入要爬的结尾页码：".decode('utf-8').encode('gbk'))
mx=int(mx)
my=int(my)

#新浪微博的模拟登陆
class weiboLogin:
    def enableCookies(self):
            #获取一个保存cookies的对象
            cj = cookielib.CookieJar()
            #将一个保存cookies对象和一个HTTP的cookie的处理器绑定
            cookie_support = urllib2.HTTPCookieProcessor(cj)
            #创建一个opener,设置一个handler用于处理http的url打开
            opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
            #安装opener，此后调用urlopen()时会使用安装过的opener对象
            urllib2.install_opener(opener)

    #预登陆获得 servertime, nonce, pubkey, rsakv
    def getServerData(self):
            url = 'http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=ZW5nbGFuZHNldSU0MDE2My5jb20%3D&rsakt=mod&checkpin=1&client=ssologin.js(v1.4.18)&_=1442991685270'
            data = urllib2.urlopen(url).read()
            p = re.compile('\((.*)\)')
            try:
                    json_data = p.search(data).group(1)
                    data = json.loads(json_data)
                    servertime = str(data['servertime'])
                    nonce = data['nonce']
                    pubkey = data['pubkey']
                    rsakv = data['rsakv']
                    return servertime, nonce, pubkey, rsakv
            except:
                    print 'Get severtime error!'
                    return None
                

    #获取加密的密码
    def getPassword(self, password, servertime, nonce, pubkey):
            rsaPublickey = int(pubkey, 16)
            key = rsa.PublicKey(rsaPublickey, 65537) #创建公钥
            message = str(servertime) + '\t' + str(nonce) + '\n' + str(password) #拼接明文js加密文件中得到
            passwd = rsa.encrypt(message, key) #加密
            passwd = binascii.b2a_hex(passwd) #将加密信息转换为16进制。
            return passwd

    #获取加密的用户名
    def getUsername(self, username):
            username_ = urllib.quote(username)
            username = base64.encodestring(username_)[:-1]
            return username

     #获取需要提交的表单数据   
    def getFormData(self,userName,password,servertime,nonce,pubkey,rsakv):
        userName = self.getUsername(userName)
        psw = self.getPassword(password,servertime,nonce,pubkey)
        
        form_data = {
            'entry':'weibo',
            'gateway':'1',
            'from':'',
            'savestate':'7',
            'useticket':'1',
            'pagerefer':'http://weibo.com/p/1005052679342531/home?from=page_100505&mod=TAB&pids=plc_main',
            'vsnf':'1',
            'su':userName,
            'service':'miniblog',
            'servertime':servertime,
            'nonce':nonce,
            'pwencode':'rsa2',
            'rsakv':rsakv,
            'sp':psw,
            'sr':'1366*768',
            'encoding':'UTF-8',
            'prelt':'115',
            'url':'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
            'returntype':'META'
            }
        formData = urllib.urlencode(form_data)
        return formData

    #登陆函数
    def login(self,username,psw):
            self.enableCookies()
            url = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)'
            servertime,nonce,pubkey,rsakv = self.getServerData()
            formData = self.getFormData(username,psw,servertime,nonce,pubkey,rsakv)
            headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0'}
            req  = urllib2.Request(
                    url = url,
                    data = formData,
                    headers = headers
            )
            result = urllib2.urlopen(req)
            text = result.read()
            print text
            #还没完！！！这边有一个重定位网址，包含在脚本中，获取到之后才能真正地登陆
            p = re.compile('location\.replace\([\'"](.*?)[\'"]\)')
            try:
                    login_url = p.search(text).group(1)
                    print login_url
                    #由于之前的绑定，cookies信息会直接写入
                    urllib2.urlopen(login_url)
                    print "Login success!"
            except:
                    print 'Login error!'
                    return 0

            #访问主页，把主页写入到文件中
            url = 'http://weibo.com/u/2679342531/home?topnav=1&wvr=6'
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            text = response.read()
            fp_raw = open("D://weibo.html","w+")
            fp_raw.write(text)
            fp_raw.close()
            #print text
            
wblogin = weiboLogin()
print u'登录'
username = raw_input("username:")
password = raw_input('password:')
wblogin.login(username,password)


#创建每个栏目的保存目录
def mkDir(dirName):  
    dirpath = os.path.join(sys.path[0], dirName)  
    if not os.path.exists(dirpath):  
        os.mkdir(dirpath)  
    return dirpath  
def mkDirs(dirName):  
    dirpath = os.path.join(sys.path[0], dirName)  
    if not os.path.exists(dirpath):  
        os.makedirs(dirpath)  
    return dirpath  



isExists=os.path.exists(".\\temps")
if not isExists:
    os.makedirs("temps\\qb")
    os.makedirs("temps\\whcg")
    os.makedirs("temps\\mntp")
    os.makedirs("temps\\sgtp")
    os.makedirs("temps\\mt")
    os.makedirs("temps\\mx")
    os.makedirs("temps\\mte")
else:
    pass



#爬影视明星网页
for www in range(mx,my+1):
    XXX = urllib2.urlopen("https://d.weibo.com/1087030002_2976_1003_2?page="+str(www)+"#Pl_Core_F4RightUserList__4") # 影视明星
    html = XXX.read().decode("utf8","ignore").encode("gbk","ignore")    
    fp_raw = open("temps\\whcg\\"+str(www)+".txt","w+")
    fp_raw.write(html)
    fp_raw.close()
    f= open('temps\\whcg\\'+str(www)+'.txt','rb')
  
    findtxt = '<strong  usercard='
    lnfindtxt = len(findtxt)
    txt = f.readlines()
    txt = str(txt)

    pos1 = txt.find(findtxt)
    pos2 = txt.find(findtxt, pos1+1)
    pos3 = txt.find(findtxt, pos2+1)
    pos4 = txt.find(findtxt, pos3+1)
    pos5 = txt.find(findtxt, pos4+1)
    pos6 = txt.find(findtxt, pos5+1)
    pos7 = txt.find(findtxt, pos6+1)
    pos8 = txt.find(findtxt, pos7+1)
    pos9 = txt.find(findtxt, pos8+1)
    pos10 = txt.find(findtxt, pos9+1)
    ID1 =  txt[pos1+6+lnfindtxt:pos1+16+lnfindtxt]
    ID2 = txt[pos2+6+lnfindtxt:pos2+16+lnfindtxt]
    ID3 = txt[pos3+6+lnfindtxt:pos3+16+lnfindtxt]
    ID4 = txt[pos4+6+lnfindtxt:pos4+16+lnfindtxt]
    ID5 = txt[pos5+6+lnfindtxt:pos5+16+lnfindtxt]
    ID6 = txt[pos6+6+lnfindtxt:pos6+16+lnfindtxt]
    ID7 =  txt[pos7+6+lnfindtxt:pos7+16+lnfindtxt]
    ID8 = txt[pos8+6+lnfindtxt:pos8+16+lnfindtxt]
    ID9 = txt[pos9+6+lnfindtxt:pos9+16+lnfindtxt]
    ID10 = txt[pos10+6+lnfindtxt:pos10+16+lnfindtxt]    
    
    ID=[ID1,ID2,ID3,ID4,ID5,ID6,ID7,ID8,ID9,ID10]
    print ID
    f.close()



    for some in ID:
        OID = "100505" + some
        COOKIES = "SUB=_2AkMhFc9hf8NhqwJRmPoRym_jaI9_ygvEiebDAHzsJxJjHlE47Gaj8oPkdVHDdzd9ToAkUSPIsxRx; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WWM2vn1KHS_k1aSj6DvSDWv; SINAGLOBAL=7552724259118.417.1447641174437; ULV=1447691774405:2:2:2:6434341784127.688.1447691774390:1447641174455; YF-Page-G0=7f5e11c19f51c6954c5e18e40c0b1444; _s_tentry=-; Apache=6434341784127.688.1447691774390; USRANIME=usrmdinst_29"; # Your cookies.
        CRAWL_PHOTOS_NUMBER = 186
        # Configuration END     
        

        COOKIES = dict((l.split('=') for l in COOKIES.split('; ')))
        #先创建保存图片的目录
        OOID=OID.replace("100505","")
        SAVE_PATH=str(OOID) + "/"
        def mkDir(dirName):  
            dirpath = os.path.join(sys.path[0], dirName)  
            if not os.path.exists(dirpath):  
                os.mkdir(dirpath)  
            return dirpath  
        SAVE_PATH = mkDir(SAVE_PATH)  
        TEMP_LastMid = ""       
        

        def save_image(image_name):
            #if not os.path.isfile(SAVE_PATH + image_name):
            sina_image_url = 'http://ww1.sinaimg.cn/large/' + image_name
            response = requests.get(sina_image_url, stream=True)
            image = response.content
            try:
                print(image_name)
                with open(SAVE_PATH+image_name,"wb") as image_object:
                    image_object.write(image)
                    return
            except IOError:
                print("IO Error\n")
                return
            finally:
                image_object.close      
        
        

        def get_album_photos_url(page):
            global TEMP_LastMid
            data={
                'ajwvr':6,
                'filter':'wbphoto|||v6',
                'page': page,
                'count':20,
                'module_id':'profile_photo',
                'oid':OID,
                'uid':'',
                'lastMid':TEMP_LastMid,
                'lang':'zh-cn',
                '_t':1,
                'callback':'STK_' + str(random.randint(10000000000000, 900000000000000))
            }
            #print(data)
            #print(COOKIES)
            album_request_result = requests.get('http://photo.weibo.com/page/waterfall',  params = data, cookies = COOKIES).text
            #print(album_request.headers)
            TEMP_LastMid = re.compile(r'"lastMid":"(\d+)"').findall(album_request_result)
            print(TEMP_LastMid)
            return (re.compile(r'(\w+.png|\w+.gif|\w+.jpg)').findall(album_request_result))     

        if __name__ == '__main__':
            for i in range(1, int(math.ceil(CRAWL_PHOTOS_NUMBER / 20.0))):
                threads = []
                for image_name in get_album_photos_url(i):
                    #save_image(image_name);
                    threads.append(threading.Thread(target=save_image, args=(image_name,)))
                for t in threads:
                    #t.setDaemon(True)
                    t.start()
