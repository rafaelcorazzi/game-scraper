from apscheduler.schedulers.background import BackgroundScheduler
from src.application.game_scraper_application import GameScraperApplication


class SchedulerJobManager:
    @staticmethod
    def start_scraping():
        GameScraperApplication.read_game()
        # scheduler = BackgroundScheduler()
        # scheduler.add_job(GameScraperApplication.read_game, 'interval', hour=24)
        # scheduler.start()
