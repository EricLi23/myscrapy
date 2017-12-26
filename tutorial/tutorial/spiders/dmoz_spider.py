import scrapy


class DemoSpider(scrapy.spiders.Spider):
    name = 'domz'
    allow_domains = ["domz.org"]
    start_urls = [
        "http://www.dmoztools.net/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoztools.net/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        filename = response.url.split("/"[-2])
        with open(filename, 'wb') as f:
            f.write(response.body)
