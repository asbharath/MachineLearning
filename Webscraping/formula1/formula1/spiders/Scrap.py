import scrapy
# from ..items import Formula1Item


class Formula1(scrapy.Spider):

    name = 'formula1'
    start_urls = [
        "https://www.formula1.com/en/results.html/2019/races/1000/australia/race-result.html"
    ]

    def parse(self, response):
        # items = Formula1Item()

        year_links = response.css('div.resultsarchive-filter-container > '
                                 'div.resultsarchive-filter-wrap:nth-child(1) '
                                 'ul.resultsarchive-filter.ResultFilterScrollable > '
                                 'li.resultsarchive-filter-item a::attr(href)')[1].extract()

        category_links = response.css('div.resultsarchive-filter-container > '
                                 'div.resultsarchive-filter-wrap:nth-child(2) '
                                 'ul.resultsarchive-filter.ResultFilterScrollable > '
                                 'li.resultsarchive-filter-item a::attr(href)')[1].extract()

        location_links = response.css('div.resultsarchive-filter-container > '
                                 'div.resultsarchive-filter-wrap:nth-child(3) '
                                 'ul.resultsarchive-filter.ResultFilterScrollable > '
                                 'li.resultsarchive-filter-item a::attr(href)')[1].extract()

        yield {'year_urls': year_links,
               'category_urls':category_links,
               'location_urls':location_links}

        title_heading = response.css('h1.ResultsArchiveTitle::text').extract_first().strip()
        table_heading = response.css('thead th::text').extract()
        print(title_heading)
        print(table_heading)
        rows = response.css('tbody tr')
        for row in rows:
            print(row.css('td:not(.limiter)')[0].css('a::text').extract_first().strip())
            print(row.css('td:not(.limiter)')[1].css('td.dark.hide-for-mobile::text').extract_first().strip())
            print(' '.join(row.css('td:not(.limiter)')[2].css('span.hide-for-tablet::text,span.hide-for-mobile::text').extract()))
            print(row.css('td:not(.limiter)')[3].css('td::text').extract_first().strip())
            print(row.css('td:not(.limiter)')[4].css('td::text').extract_first().strip())
            print(row.css('td:not(.limiter)')[5].css('td::text').extract_first().strip())
