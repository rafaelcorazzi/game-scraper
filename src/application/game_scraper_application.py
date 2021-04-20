from src.infrasctructure.services.scraper_services import ScraperServices
from src.infrasctructure.queue.publisher import Publisher
import json
import pandas as pd

class GameScraperApplication:
    @staticmethod
    def read_game() -> int:
        GameScraperApplication.__scraper_consoles()
        #GameScraperApplication.__scraper_games()
        return 0

    @staticmethod
    def __scraper_consoles() -> bool:
        s = ScraperServices()
        consoles = s.list_of_console()
        #df = pd.read_json(json.dumps(consoles))
       #  export_csv = df.to_csv()
        Publisher.publish("console.data", json.dumps(consoles))
        return True

    @staticmethod
    def __scraper_games() -> bool:
        s = ScraperServices()

        for a in s.list_of_console():
            print(a.console_plataform_name)
            jogos = s.list_of_games_by_plataform(a.console_plataform_code)
            Publisher.publish("game.data", json.dumps(jogos))

        return True
