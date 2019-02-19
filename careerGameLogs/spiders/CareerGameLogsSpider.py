import scrapy
from .. import items

class CareerGameLogsSpider(scrapy.Spider):
    name = "careerLogs"

    def start_requests(self):
        yield scrapy.Request(url=f"https://www.basketball-reference.com/players/{self.playerCode[0]}/{self.playerCode}.html",
                             callback=self.findCareers)  #

    def findCareers(self, response):
        pergameTable = response.css("table#per_game")
        links = pergameTable.xpath('.//th[@data-stat="season"]/a/@href').extract()
        for link in links:
            yield response.follow(url=link, callback=self.parse)

    def parse(self, response):
        if response.status == 503:
            response.follow(url=response.url, callback=self.parse)
        table = response.css("table#pgl_basic")
        tableRows = table.css("tbody tr")
        dataStats = ["date_game", "age", "team_id", "game_location", "opp_id", "game_result",
                     "gs", "mp", "fg", "fga", "fg_pct", "fg3", "fg3a", "ft", "fta", "ft_pct",
                     "orb", "drb", "trb", "ast", "stl", "blk", "tov", "pf", "pts", "game_score"]
        for row in tableRows:
            rowItem = items.CareergamelogsItem()
            badRow = False
            for stat in dataStats:
                element = row.xpath(f'.//*[@data-stat="{stat}"]//text()').extract()
                if len(element) == 0:
                    element = [""]
                    if stat == "gs":
                        badRow = True
                elif element[0] == "Date":
                    badRow = True
                rowItem[stat] = element
            if not badRow:
                yield rowItem