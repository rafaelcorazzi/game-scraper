from src.infrasctructure.services.scraper_services import  ScraperServices


s = ScraperServices()

for a in s.list_of_console():
    print(a.console_plataform_name)
    jogos = s.list_of_games_by_plataform(a.console_plataform_code)
    for j in jogos:
        g = s.game_details(j.link, j.reference_id, a.console_plataform_code)
        print(g.to_json())