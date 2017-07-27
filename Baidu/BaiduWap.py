#coding=utf-8

from bs4 import BeautifulSoup
from Base.BaseSearch import BaseSearch

class BaiduWapSearch(BaseSearch):
    
    def __init__(self,keyword,path,seName):
        urls = self.getUrl(keyword)
        self.page = BaseSearch.page
        BaseSearch.__init__(self,urls,path,seName)
        
    def getUrl(self,keyword):
        urls = []
        urls.append('http://wap.baidu.com/ssid=0/from=0/bd_page_type=1/uid=6B69A7C9A27EBEBE163BF64D43101123/s?word='+keyword+'&uc_param_str=upssntdnvelami&st_1=111041&st_2=102041&pu=sz%40224_220&idx=20000&tn_1=webmain&tn_2=fwapadv&ct_2=%E6%90%9CWap')
        return urls

    def parseHtml(self,html):
        soup = BeautifulSoup(html)
        results = soup.findAll("div",{"class","resitem"})
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
            
        
            
    
        
