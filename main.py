from src.infrasctructure.services.scraper_services import  ScraperServices


s = ScraperServices()

for a in s.list_of_console():
    print(a.console_plataform_name)