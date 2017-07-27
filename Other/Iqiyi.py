#coding=utf-8

from Base.BaseSearch import BaseSearch
from bs4 import BeautifulSoup

class IqiyiSearch(BaseSearch):
    
    def __init__(self,keyword,path,seName):
        urls = self.getUrl(keyword)
        self.page = BaseSearch.page
        BaseSearch.__init__(self,urls,path,seName)
        
    def getUrl(self,keyword):
        urls = []
        for num in range(self.page):
            urls.append('http://so.iqiyi.com/so/q_'+keyword+'_sort__page_'+str(num+1)+'_ctg_')
        return urls
    
    def parseHtml(self,html):
        soup = BeautifulSoup(html)
        results = soup.findAll("div",{"class","List"})
        fileName = self.getFileName()
        
        for item in results:
            self.parseDiv(item,fileName)
            
        self.writeFile("1", fileName)
            
    def parseDiv(self,div,fileName):
        soup = BeautifulSoup(str(div))
        urls = soup.findAll("a",{"class","sea_Img_box"})
        
        for url in urls:
            realUrl = url.get("href")
            self.writeFile(realUrl+'\n', fileName)
            
        
            
