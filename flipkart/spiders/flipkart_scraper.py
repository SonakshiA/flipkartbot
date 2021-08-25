import scrapy
from ..items import FlipkartItem

class flipkartSpider(scrapy.Spider):
    name="Flipkart"
    page_no = 2
    start_urls=['https://www.flipkart.com/search?q=agatha+christie+books&sid=bks&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_15_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_15_na_na_na&as-pos=2&as-type=RECENT&suggestionId=agatha+christie+books%7CBooks&requestId=d9a36955-bdfc-4173-a0cd-50f78d8ad8b8&as-searchtext=agatha+christie&p%5B%5D=facets.language%255B%255D%3DEnglish'
    ]

    def parse(self,response):
        items = FlipkartItem()

        all_books = response.css('div._4ddWXP')

        for books in all_books:

            book = books.css('.s1Q9rs::text').extract()
            price = books.css('._30jeq3::text').extract()
            rating = books.css('div._3LWZlK::text').extract()

            items['title'] = book
            items['price'] = price
            items['rating'] = rating

            yield items

        next_page = 'https://www.flipkart.com/search?q=agatha+christie+books&sid=bks&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_15_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_15_na_na_na&as-pos=2&as-type=RECENT&suggestionId=agatha+christie+books%7CBooks&requestId=d9a36955-bdfc-4173-a0cd-50f78d8ad8b8&as-searchtext=agatha+christie&p%5B%5D=facets.language%255B%255D%3DEnglish&page=' + str(flipkartSpider.page_no)

        if flipkartSpider.page_no <=28:
            flipkartSpider.page_no += 1
            yield response.follow(next_page, callback= self.parse)


