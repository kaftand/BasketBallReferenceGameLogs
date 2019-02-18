# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CareergamelogsItem(scrapy.Item):
    # define the fields for your item here like:
    date_game = scrapy.Field()
    age = scrapy.Field()
    team_id = scrapy.Field()
    game_location = scrapy.Field()
    opp_id = scrapy.Field()
    game_result = scrapy.Field()
    gs = scrapy.Field()
    mp = scrapy.Field()
    fg = scrapy.Field()
    fga = scrapy.Field()
    fg_pct = scrapy.Field()
    fg3 = scrapy.Field()
    fg3a = scrapy.Field()
    ft = scrapy.Field()
    fta = scrapy.Field()
    ft_pct = scrapy.Field()
    orb = scrapy.Field()
    drb = scrapy.Field()
    trb = scrapy.Field()
    ast = scrapy.Field()
    stl = scrapy.Field()
    blk = scrapy.Field()
    tov = scrapy.Field()
    pf = scrapy.Field()
    pts = scrapy.Field()
    game_score = scrapy.Field()
