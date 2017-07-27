#coding=utf-8

from bs4 import BeautifulSoup
from Base.BaseSearch import BaseSearch

class YahooSearch(BaseSearch):
    
    def __init__(self,keyword,path,seName):
        urls = self.getUrl(keyword)
        self.page = BaseSearch.page
        BaseSearch.__init__(self,urls,path,seName)
        
    def getUrl(self,keyword):
        urls = []
        for num in range(self.page):
            urls.append('http://www.yahoo.cn/s?q='+keyword+'&page='+str(num+1))
        return urls

    def parseHtml(self,html):
        soup = BeautifulSoup(html)
        results = soup.findAll("h3",{"class","title"})
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
            
        
            
    
        
