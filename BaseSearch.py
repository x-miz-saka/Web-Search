#coding=utf-8

import urllib2
import cookielib
import threading
import time
import os
import ConfigParser

class BaseSearch(threading.Thread):
    
    config = ConfigParser.ConfigParser()
    config.read("config.ini")
    page = config.get("Page", "page")
    page = int(page)
        
    def __init__(self,urls,path,seName):
        threading.Thread.__init__(self)
        self.urls = urls
        self.path = path
        self.seName = seName
        
    def run(self):
        cookie = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        opener.addheaders = [('User-Agent','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2; .NET CLR 1.1.4322)')]
        urllib2.install_opener(opener)
        
        while True:
            try:
                for url in self.urls:
                    print url
                    request = urllib2.urlopen(url,timeout=60)
                    data = request.read()
                    request.close();
                    self.parseHtml(data)
            except Exception as e:
                print e
                time.sleep(300)
                continue
            
            time.sleep(300)
            
    def getFileName(self):
        currentTime = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        filePath = self.path + "//" + self.seName 
        fileName = filePath + "//"+ currentTime + ".txt"
        
        if not os.path.exists(filePath):
            os.makedirs(filePath)
            
        return fileName
    
    def writeFile(self,data,fileName):
        fp = open(fileName,'a')
        fp.write(data)
        fp.close()
            
    def parseHtml(self,html):
        pass
    
    def parseDiv(self,div,fileName):
        pass
