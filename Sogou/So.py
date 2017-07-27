#coding=utf-8

from bs4 import BeautifulSoup
from Base.BaseSearch import BaseSearch

class SoSearch(BaseSearch):
    
    def __init__(self,keyword,path,seName):
        urls = self.getUrl(keyword)
        self.page = BaseSearch.page
        BaseSearch.__init__(self,urls,path,seName)
        
    def getUrl(self,keyword):
        urls = []
        for num in range(self.page):
            page = str(num+1)
            urls.append('http://www.so.com/s?q='+keyword+'&pn='+page+'&j=0&_re=0')
        return urls

    def parseHtml(self,html):
        soup = BeautifulSoup(html)
        results = soup.findAll("ul",{"class","result"})
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
            
        
            
    
        
