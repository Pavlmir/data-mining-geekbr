# -*- coding: utf-8 -*-
import scrapy
from ..items import AvitoRealEstateItem
from ..spiders.xpaths import AVITO_RIELT_XPATH
from scrapy.loader import ItemLoader


class AvitoSpider(scrapy.Spider):
    name = 'avito'
    allowed_domains = ['avito.ru']
    city = "irkutsk"
    start_urls = [f"https://www.avito.ru/{city}/kvartiry/prodam-ASgBAgICAUSSA8YQ"]

    def parse(self, response):
        for num in response.xpath('//div[@data-marker="pagination-button"]//span/text()'):
            try:
                tmp = int(num.get())
                yield response.follow(f'/{self.city}/kvartiry/?p={tmp}', callback=self.parse)

            except TypeError as e:
                continue
            except ValueError as e:
                continue

        for ads_url in response.css('div.item_table h3.snippet-title a.snippet-link::attr("href")'):
            yield response.follow(ads_url, callback=self.parse_ads)

    def parse_ads(self, response):
        item = ItemLoader(AvitoRealEstateItem(), response)
        item.add_value('url', response.url)
        item.add_css('title', 'div.title-info-main h1.title-info-title span::text')
        item.add_xpath('photos', "//div[contains(@class, 'gallery-img-frame')]/@data-url")
        item.add_value('floor_number', response.xpath("//span[text()='Этаж: ']/parent::li/text()").extract()[1])
        item.add_value('floors_in_house',
                       response.xpath("//span[text()='Этажей в доме: ']/parent::li/text()").extract()[1])
        item.add_value('type_of_house', response.xpath("//span[text()='Тип дома: ']/parent::li/text()").extract()[1])
        item.add_value('rooms_count',
                       response.xpath("//span[text()='Количество комнат: ']/parent::li/text()").extract()[1])
        item.add_value('square', response.xpath("//span[text()='Общая площадь: ']/parent::li/text()").extract()[1])
        item.add_value('living_square',
                       response.xpath("//span[text()='Жилая площадь: ']/parent::li/text()").extract()[1])
        item.add_value('square_of_kitchen',
                       response.xpath("//span[text()='Площадь кухни: ']/parent::li/text()").extract()[1])
        item.add_value('time_publish',
                       response.xpath("//div[contains(@class, 'title-info-metadata-item-redesign')]/text()").extract()[
                           0])
        item.add_value('name', response.xpath(
            "//div[contains(@class, 'seller-info-name js-seller-info-name')]/a/text()").extract()[0])
        item.add_value('name_url', response.xpath(
            "//div[contains(@class, 'seller-info-name js-seller-info-name')]/a/@href").extract()[0])
        # loader = AvitoRealEstateItem(response=response)
        # loader.add_value("url", response.url)
        # for key, xpath in AVITO_RIELT_XPATH.items():
        #     loader.add_xpath(key, xpath)

        yield item.load_item()
