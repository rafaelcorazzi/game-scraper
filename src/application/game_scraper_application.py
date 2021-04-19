from src.infrasctructure.services.scraper_services import ScraperServices
from src.infrasctructure.queue.publisher import Publisher

class GameScraperApplication:
    @staticmethod
    def read_game() -> int:
        # result_console = GameScraperApplication.__scraper_consoles()
        GameScraperApplication.__scraper_games()
        return 0

    @staticmethod
    def __scraper_consoles() -> bool:
        return True

    @staticmethod
    def __scraper_games() -> bool:
        s = ScraperServices()

        for a in s.list_of_console():
            print(a.console_plataform_name)
            jogos = s.list_of_games_by_plataform(a.console_plataform_code)
            for j in jogos:
                g = s.game_details(j.link, j.reference_id, a.console_plataform_code)
                Publisher.publish("game.data", g.to_json())

        return True
