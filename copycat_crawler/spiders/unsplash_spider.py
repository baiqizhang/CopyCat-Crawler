import scrapy

from copycat_crawler.items import ImageItem

class UnsplashSpider(scrapy.Spider):
    name = "unsplash"
    allowed_domains = ["unsplash.com"]
    start_urls = [
        "https://unsplash.com/"
    ]

    def parse(self, response):
        imgs = response.css('.qa-photo').xpath('a/img')
        for img in imgs:
            #print 'src =', img.xpath('@src').extract(), 'alt =', img.xpath('@alt').extract()

            item = ImageItem()
            item['image_urls'] = img.xpath('@src').extract()
            item['author'] = 'unsplash'
            item['desc'] = img.xpath('@alt').extract()

            yield item