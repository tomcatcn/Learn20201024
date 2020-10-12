import requests
import re


class MzSpider:
    def __init__(self):
        self.baseurl = "http://www.mca.gov.cn/article/sj/xzqh/2020/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
            
            }
    def get_html(self):
        res = requests.get(self.baseurl,headers=self.headers)
        res.encoding = "utf-8"
        res = res.text
        # print(res)
        return res
    def parse_html(self,res):
        p = re.compile('class="artitlelist" href="(.*?)"' ,re.S)
        url_list = p.findall(res)

        return url_list
    
    def parse_two(self,url_list):
        url = url_list[0]
        url = 'http://www.mca.gov.cn' + url
        print(url)
        res = requests.get(url,headers=self.headers)
        with open("false.html","a",encoding=('utf-8')) as f:
            f.write(res.text)
    
    def run(self):
        res = self.get_html()
        url_list = self.parse_html(res)
        print(url_list)
        self.parse_two(url_list) 
    
    
if __name__ == "__main__":
    spider = MzSpider()
    spider.run()