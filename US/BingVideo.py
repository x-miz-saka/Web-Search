#coding=utf-8

from bs4 import BeautifulSoup
from Base.BaseSearch import BaseSearch

class BingVideoSearch(BaseSearch):
    
    def __init__(self,keyword,path,seName):
        urls = self.getUrl(keyword)
        self.page = BaseSearch.page
        BaseSearch.__init__(self,urls,path,seName)
        
    def getUrl(self,keyword):
        urls = []
        urls.append('http://cn.bing.com/videos/search?q='+keyword+'&qs=n&pq='+keyword+'&sc=8-4&sp=-1&sk=&FORM=PORE')
        return urls

    def parseHtml(self,html):
        soup = BeautifulSoup(html)
        results = soup.findAll("span",{"class","sg_cv"})
        fileName = self.getFileName()
        
        for item in results:
            self.parseDiv(item,fileName)
            
        self.writeFile("1", fileName)
            
    def parseDiv(self,div,fileName):
        soup = BeautifulSoup(str(div))
        urls = soup.findAll("a")
        
        for url in urls:
            realUrl = url.get("href")
            self.writeFile(realUrl+'\n', fileName)
            
        
            
    
        
