"""
Источник https://hh.ru/search/vacancy?schedule=remote&L_profession_id=0&area=113
вакансии удаленной работы.

Задача: Обойти с точки входа все вакансии и собрать след данные:

1. название вакансии
2. оклад (строкой от до или просто сумма)
3. Описание вакансии
4. ключевые навыки - в виде списка названий
5. ссылка на автора вакансии

Перейти на страницу автора вакансии,
собрать данные:

1. Название
2. сайт ссылка (если есть)
3. сферы деятельности (списком)
4. Описание

Обойти и собрать все вакансии данного автора.
"""

import scrapy

from ..loaders import HHLoader
from ..spiders.xpaths import HH_PAGE_XPATH, HH_VACANCY_XPATH


class HhSpider(scrapy.Spider):
    name = "hh"
    allowed_domains = ["hh.ru"]
    start_urls = [
        "https://hh.ru/search/vacancy?schedule=remote&L_profession_id=0&area=113"
    ]

    def _get_follow_xpath(self, response, xpath, callback):
        for url in response.xpath(xpath):
            yield response.follow(url, callback=callback)

    def parse(self, response):
        callbacks = {"pagination": self.parse, "vacancy": self.vacancy_parse}

        for key, xpath in HH_PAGE_XPATH.items():
            yield from self._get_follow_xpath(response, xpath, callbacks[key])

    def vacancy_parse(self, response):
        loader = HHLoader(response=response)
        loader.add_value("url", response.url)
        for key, xpath in HH_VACANCY_XPATH.items():
            loader.add_xpath(key, xpath)

        yield loader.load_item()

    def company_parse(self, response):
        pass
