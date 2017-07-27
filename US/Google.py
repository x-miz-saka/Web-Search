#coding=utf-8

from bs4 import BeautifulSoup
from Base.BaseSearch import BaseSearch

class GoogleSearch(BaseSearch):
    
    def __init__(self,keyword,path,seName):
        urls = self.getUrl(keyword)
        self.page = BaseSearch.page
        BaseSearch.__init__(self,urls,path,seName)
        
    def getUrl(self,keyword):
        urls = []
        urls.append('http://www.google.com/search?sourceid=chrome&;ie=UTF-8&q='+keyword+'&start=0&num=100') 
        return urls

    def parseHtml(self,html):
        soup = BeautifulSoup(html)
        results = soup.findAll("h3",{"class","r"})
        fileName = self.getFileName()
        
        for item in results:
            self.parseDiv(item,fileName)
            
        self.writeFile("1\n", fileName)
            
    def parseDiv(self,div,fileName):
        soup = BeautifulSoup(str(div))
        urls = soup.findAll("a")
        for url in urls:
            realUrl = url.get("href")[7:]
            self.writeFile(realUrl+'\n', fileName)
            
        
