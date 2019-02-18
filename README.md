# BasketBallReferenceGameLogs
Scrape game logs for the entire career of a player


Dependencies:

python 3.6

scrapy


1. clone repository
2. find player code of the player of interest (its in the url on basketball reference: The url for Giannis' page is https://www.basketball-reference.com/players/a/antetgi01.html. His player code is antetgi01
3. scrapy crawl careerLogs -a playerCode=\<player code> -o \<output filename>.csv -t csv

