import scrapy
from scrapy.spiders import Rule , CrawlSpider
from scrapy.linkextractors import LinkExtractor 


class StackquesSpider(scrapy.Spider):
    name = "stackques"
    allowed_domains = ["stackoverflow.com"]
    start_urls = ["https://stackoverflow.com/questions?tab=Activate"]
    
    rule = [Rule(LinkExtractor( deny = 'tag/',unique=True),callback= 'parse', follow= True)] 
    
 
    def parse(self, response):
        
        for question in response.css("div.s-post-summary--content h3.s-post-summary--content-title a::attr(href)"):
            yield response.follow(question, self.ques_page_parse)
            
    def  ques_page_parse(self, response):
           
            yield{
                "ques": response.css("")
            }
# &page=%s" % page for page in list(range(10))