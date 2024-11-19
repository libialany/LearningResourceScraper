from pathlib import Path
from dotenv import load_dotenv
load_dotenv()
import os
import scrapy
from news.items import NewsItem  

class QuotesSpider(scrapy.Spider):
    name = "news"
    # custom_settings = {'FEEDS': {'data/%(name)s/%(name)s_%(time)s.jsonl': {'format': 'jsonlines',}}}

    def start_requests(self):
        
        urls = [
           os.getenv("URL_BASE"),
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        new_item = NewsItem()
        for quote in response.css('div.SummaryItemWrapper-iwvBff.XhVwU.summary-item.summary-item--has-border.summary-item--has-rule.summary-item--article.summary-item--no-icon.summary-item--text-align-left.summary-item--layout-placement-side-by-side-desktop-only.summary-item--layout-position-image-left.summary-item--layout-proportions-33-66.summary-item--side-by-side-align-center.summary-item--side-by-side-image-right-mobile-false.summary-item--standard'):
            new_item['title'] = quote.css('h3.SummaryItemHedBase-hiFYpQ.kgaBCS.summary-item__hed::text').get()
            new_item['date'] = quote.css('time.BaseWrap-sc-gjQpdd.BaseText-ewhhUZ.SummaryItemBylinePublishDate-ctLSIQ.iUEiRd.dOvoaC.kiqveE.summary-item__publish-date::text').get()
            yield new_item
        
        next_page = response.css("div.SummaryListCallToActionWrapper-fngYcb.bXdTPE.summary-list__call-to-action-wrapper a::attr(href)").get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
