#coding=utf-8

from SESearch.Baidu import BaiduSearch
from SESearch.Bing import BingSearch
from SESearch.Google import GoogleSearch
from SESearch.Jike import JikeSearch
from SESearch.Pangu import PanguSearch
from SESearch.Sogou import SogouSearch
from SESearch.Soso import SosoSearch
from SESearch.So import SoSearch
from SESearch.YouDao import YouDaoSearch
from SESearch.Yahoo import YahooSearch

from VideoSearch.Iqiyi import IqiyiSearch
from VideoSearch.BingVideo import BingVideoSearch
from VideoSearch.Soku import SokuSearch
from VideoSearch.SinaVideo import SinaVideoSearch
from VideoSearch.PanguVideo import PanguVideoSearch

from MobileSearch.BaiduWap import BaiduWapSearch
import ConfigParser

class SearchFactory:
    
    def __init__(self,keyword,path):
        self.keyword = keyword
        self.path = path
        
    def start(self):
        config = ConfigParser.ConfigParser();
        config.read("config.ini")
        
        se = "SearchEngine"
        
        name = "bing"
        value = config.get(se, name)
        if value == "1":
            print "bing..."
            bing = BingSearch(self.keyword,self.path,name)
            bing.start()
    
        name = 'google'
        value = config.get(se,name)
        if value == "1":
            print "google..."
            google = GoogleSearch(self.keyword,self.path,name)
            google.start()
            
        name = 'baidu'
        value = config.get(se, name)
        if value == "1":
            print "baidu..."
            baidu = BaiduSearch(self.keyword,self.path,name)
            baidu.start()
            
        name = "jike"
        value = config.get(se,name)
        if value == "1":
            print "jike..."
            jike = JikeSearch(self.keyword,self.path,name)
            jike.start()
            
        name = "pangu"
        value = config.get(se,name)
        if value == "1":
            print "pangu..."
            pangu = PanguSearch(self.keyword,self.path,name)
            pangu.start()
            
        name = "sogou"
        value = config.get(se,name)
        if value == "1":
            print "sogou..."
            sogou = SogouSearch(self.keyword,self.path,name)
            sogou.start()
            
        name = "soso"
        value = config.get(se,name)
        if value == "1":
            print "soso..."
            soso = SosoSearch(self.keyword,self.path,name)
            soso.start()
            
        name = "so"
        value = config.get(se, name)
        if value == "1":
            print "so..."
            so = SoSearch(self.keyword,self.path,name)
            so.start()
            
        name = "youdao"
        value = config.get(se, name)
        if value == "1":
            print "youdao..."
            youdao = YouDaoSearch(self.keyword,self.path,name)
            youdao.start()
            
        name = "yahoo"
        value = config.get(se,name)
        if value == "1":
            print "yahoo..."
            yahoo = YahooSearch(self.keyword,self.path,name)
            yahoo.start()
            
        video = "Video"
        
        name = 'iqiyi'
        value = config.get(video,name)
        if value == "1":
            print "iqiyi..."
            iqiyi = IqiyiSearch(self.keyword,self.path,name)
            iqiyi.start()
            
        name = "bing_video"
        value = config.get(video, name)
        if value == "1":
            print 'bing video...'
            bingVideo = BingVideoSearch(self.keyword,self.path,name)
            bingVideo.start()
            
        name = "soku"
        value = config.get(video,name)
        if value == "1":
            print "soku..."
            soku = SokuSearch(self.keyword,self.path,name)
            soku.start()
            
        name = "sina_video"
        value = config.get(video,name)
        if value == "1":
            print "sina video..."
            sina = SinaVideoSearch(self.keyword,self.path,name)
            sina.start()
            
        name = "pangu_video"
        value = config.get(video,name)
        if value == "1":
            print "pangu video..."
            pangu = PanguVideoSearch(self.keyword,self.path,name)
            pangu.start()
            
        wap = "Mobile"
        
        name = "baidu_wap"
        value = config.get(wap,name)
        if value == "1":
            print "biadu wap..."
            baiduWap = BaiduWapSearch(self.keyword,self.path,name)
            baiduWap.start()
            
