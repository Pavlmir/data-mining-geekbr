AVITO_RIELT_XPATH = {
    "title": 'div.title-info-main h1.title-info-title span::text',
    "images": "//div[contains(@class, 'gallery-img-frame')]/@data-url",
    'floor_number': "//span[text()='Этаж: ']/parent::li/text()",
    'floors_in_house': "//span[text()='Этажей в доме: ']/parent::li/text()",
    'type_of_house': "//span[text()='Тип дома: ']/parent::li/text()",
    'name': "//div[contains(@class, 'seller-info-name js-seller-info-name')]/a/text()",
    'rooms_count': "//span[text()='Количество комнат: ']/parent::li/text()",
    'square': "//span[text()='Общая площадь: ']/parent::li/text()",
    'living_square': "//span[text()='Жилая площадь: ']/parent::li/text()",
    'square_of_kitchen': "//span[text()='Площадь кухни: ']/parent::li/text()",
    'time_publish': "//div[contains(@class, 'title-info-metadata-item-redesign')]/text()",
    'name_url': "//div[contains(@class, 'seller-info-name js-seller-info-name')]/a/@href",
}
