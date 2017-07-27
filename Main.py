#coding=utf-8

import urllib
from Search.WebSearch import SearchFactory
import ConfigParser

if __name__ == '__main__':
    config = ConfigParser.ConfigParser()
    config.read("config.ini")
    path = config.get("SavePath","path")
    keywords = config.get("Keyword", "word")
    
    for keyword in keywords.split(','):
        keyword = keyword.decode("gbk")
        print keyword
        keyword = urllib.quote(str(keyword))
        factory = SearchFactory(keyword,path)
        factory.start()
    
    
    
