from apscheduler.schedulers.background import BackgroundScheduler
from src.application.game_scraper_application import GameScraperApplication
class SchedulerJobManager():

    @staticmethod
    def start_scraping():
        scheduler = BackgroundScheduler()
        scheduler.add_job(GameScraperApplication.read_game, 'interval', minute=30)
        scheduler.start()