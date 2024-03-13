from scrapy import Spider


class PremierligaSpider(Spider):
    name = "premierliga"
    start_urls = [
        "https://premierliga.ru/tournament-table/",
    ]

    def parse(self, response):
        for tr in response.css(".stats-tournament-table tr")[2:]:
            yield {
                "place": tr.css(".place::text").get().strip(),
                "club": tr.css(".club > p > a::text").get(),
                "all_games": tr.css("td:nth-child(4) p::text").get().strip(),
                "all_win": tr.css("td:nth-child(5) p::text").get().strip(),
                "all_draw": tr.css("td:nth-child(6) p::text").get().strip(),
                "all_lose": tr.css("td:nth-child(7) p::text").get().strip(),
                "all_goals": "-".join(tr.css("td:nth-child(8) p span::text").getall()),
                "points": tr.css("td:nth-child(9) p::text").get().strip(),
                "home_win": tr.css("td:nth-child(13) p::text").get().strip(),
                "home_draw": tr.css("td:nth-child(14) p::text").get().strip(),
                "home_lose": tr.css("td:nth-child(15) p::text").get().strip(),
                "home_goals": "-".join(tr.css("td:nth-child(16) p span::text").getall()),
                "away_win": tr.css("td:nth-child(18) p::text").get().strip(),
                "away_draw": tr.css("td:nth-child(19) p::text").get().strip(),
                "away_lose": tr.css("td:nth-child(20) p::text").get().strip(),
                "away_goals": "-".join(tr.css("td:nth-child(21) p span::text").getall()),
            }
