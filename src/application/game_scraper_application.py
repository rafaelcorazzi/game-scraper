import jsonpickle

from src.infrastructure.services.scraper_services import ScraperServices
from src.infrastructure.queue.publisher import Publisher
import json
import pandas as pd

class GameScraperApplication:
    @staticmethod
    def read_game() -> int:
        #GameScraperApplication.__scraper_consoles()
        GameScraperApplication.__scraper_games()
        return 0

    @staticmethod
    def __scraper_consoles() -> bool:
        s = ScraperServices()
        consoles = s.list_of_console()
        Publisher.publish("console.data", json.dumps(consoles))
        return True

    @staticmethod
    def __scraper_games() -> bool:
        s = ScraperServices()
        c, _ = s.list_of_console()
        for a in c:
            jogos = s.list_of_games_by_plataform(a.console_plataform_code)
            print(json.loads(json.dumps("{'data': " + str(json.loads(json.dumps(jogos))) + "}")))
            Publisher.publish("game.data",json.loads(json.dumps("{'data': " + str(json.loads(json.dumps(jogos))) + "}")))

        return True
