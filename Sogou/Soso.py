#coding=utf-8

from bs4 import BeautifulSoup
from Base.BaseSearch import BaseSearch

class SosoSearch(BaseSearch):
    
    def __init__(self,keyword,path,seName):
        urls = self.getUrl(keyword)
        self.page = BaseSearch.page
        BaseSearch.__init__(self,urls,path,seName)
        
    def getUrl(self,keyword):
        urls = []
        for num in range(self.page):
            page = num+1
            urls.append('http://www.soso.com/q?w='+keyword+'&lr=&sc=web&ch=w.p&num=10&gid=&cin=&site=&sf=0&sd=0&nf=&pg='+str(page))
        return urls

    def parseHtml(self,html):
        soup = BeautifulSoup(html)
        results = soup.findAll("h3")
        fileName = self.getFileName()
        for item in results:
            self.parseDiv(item,fileName)
            
        self.writeFile("1\n", fileName)
            
    def parseDiv(self,div,fileName):
        soup = BeautifulSoup(str(div))
        urls = soup.findAll("a")
        
        for url in urls:
            realUrl = url.get("href")
            self.writeFile(realUrl+'\n', fileName)
            
        
            
    
        
