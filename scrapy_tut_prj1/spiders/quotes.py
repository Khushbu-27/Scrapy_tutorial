import scrapy
from scrapy.spiders import Rule, CrawlSpider 
from scrapy.linkextractors import LinkExtractor 


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]
                
                #   "https://quotes.toscrape.com/page/2/",
                #   "https://quotes.toscrape.com/page/3/",
                #   "https://quotes.toscrape.com/page/4/",
                #   "https://quotes.toscrape.com/page/5/"]
                
    # rules = [Rule(LinkExtractor(allow = 'page/', deny = 'tag/'), callback= 'parse', follow=True)]
    
    def parse(self, response):
        
        for next_page in response.css("li.next a"):
            yield response.follow(next_page, self.parse)
            
        for quote in response.css("div.quote span.text::text"):
            # text = quote.css("span.text::text").get(),
            # author = quote.css("small.author::text").get(),
            # tags = quote.css("div.tags a.tag::text").getall()
            
            yield{
                # 'Text': text,
                # 'Author': author,
                # 'Tags': tags
                "qoute": quote.get()
            }