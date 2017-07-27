#coding=utf-8

from bs4 import BeautifulSoup
from Base.BaseSearch import BaseSearch

class BaiduSearch(BaseSearch):
    
    def __init__(self,keyword,path,seName):
        urls = self.getUrl(keyword)
        self.page = BaseSearch.page
        BaseSearch.__init__(self,urls,path,seName)
        
    def getUrl(self,keyword):
        urls = []
        for num in range(self.page):
            if num == 0:
                urls.append('http://www.baidu.com/s?wd='+keyword+'&pn=0&ie=utf-8&usm=3')
            else:
                pn = 10*(num-1)
                urls.append('http://www.baidu.com/s?wd='+keyword+'&pn='+str(pn)+'&ie=utf-8&usm=3&rsv_page=1')
        return urls

    def parseHtml(self,html):
        soup = BeautifulSoup(html)
        results = soup.findAll("h3",{"clsss","t"})
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
            
        
            
    
        
