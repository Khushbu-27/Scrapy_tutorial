import scrapy
from scrapy_tut_prj1.items import BookItem 

class BookSpider(scrapy.Spider):
    name = "book"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        
        books = response.xpath("//article[@class = 'product_pod']")
        
        for book in books:
            
            title = book.xpath("./h3/a/@title").get(),
            price = book.xpath("./div[@class ='product_price']/p[@class= 'price_color']/text()").get()
            rating = book.xpath("./p[ contains(@class, 'star-rating')]/@class").get()
            
            # print(title,price,rating)
            bookItem = BookItem()
            
            bookItem["title"] = title
            bookItem["price"] = price
            bookItem["rating"] = rating
            
            yield bookItem
            
        