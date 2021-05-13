# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from scrapy.loader.processors import MapCompose, TakeFirst
import scrapy


def clean_photo(values):
    if values[:2] == '//':
        return f'http:{values}'
    return values


class AvitoRealEstateItem(scrapy.Item):
    _id = scrapy.Field()
    url = scrapy.Field(output_processor=TakeFirst())
    title = scrapy.Field(output_processor=TakeFirst())
    floor_number = scrapy.Field(output_processor=TakeFirst())
    floors_in_house = scrapy.Field(output_processor=TakeFirst())
    type_of_house = scrapy.Field(output_processor=TakeFirst())
    rooms_count = scrapy.Field(output_processor=TakeFirst())
    square = scrapy.Field(output_processor=TakeFirst())
    living_square = scrapy.Field(output_processor=TakeFirst())
    square_of_kitchen = scrapy.Field(output_processor=TakeFirst())
    images = scrapy.Field(input_processor=MapCompose(clean_photo))
    time_publish = scrapy.Field(output_processor=TakeFirst())
    name = scrapy.Field(output_processor=TakeFirst())
    name_url = scrapy.Field(output_processor=TakeFirst())
