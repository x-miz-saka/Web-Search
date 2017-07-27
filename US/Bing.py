#coding=utf-8

from bs4 import BeautifulSoup
from Base.BaseSearch import BaseSearch

class BingSearch(BaseSearch):
    
    def __init__(self,keyword,path,seName):
        urls = self.getUrl(keyword)
        self.page = BaseSearch.page
        BaseSearch.__init__(self,urls,path,seName)
        
    def getUrl(self,keyword):
        urls = []
        for num in range(self.page):
            if num == 0:
                urls.append('http://cn.bing.com/search?q='+keyword+'&qs=n&pq='+keyword+'&sc=8-3&sp=-1&sk=&first=1&FORM=PORE')
            else:
                first = num*10
                urls.append('http://cn.bing.com/search?q='+keyword+'&qs=n&pq='+keyword+'&sc=8-3&sp=-1&sk=&first='+str(first)+'&FORM=PORE')
        return urls

    def parseHtml(self,html):
        soup = BeautifulSoup(html)
        results = soup.findAll("div","sb_tlst")
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
            
        
            
    
        
