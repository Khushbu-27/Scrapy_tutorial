import scrapy
from scrapy import FormRequest

class AutologinSpider(scrapy.Spider):
    name = "autologin"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/login"]

    def parse(self, response):
        
        csrf_token = response.xpath("//*[@name = 'csrf_token']/@value").get()
        print(csrf_token)
        yield FormRequest.from_response(response, formdata={
            
            "csrf_token": csrf_token,
            "username": "user",
            "password": "1234"
        },
        callback= self.parse_after_login)
        
    def parse_after_login(self, response):
        
        # print(response.request.headers)
        status = response.css("div.col-md-4 p::text")
      
        if status == 'Login':
            print("login failed")
            
        elif status == 'Logout':
            print("login was sucessfull")
        