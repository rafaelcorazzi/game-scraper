from src.domain.base_domain import BaseDomain
from datetime import datetime


class Game(BaseDomain):
    def __init__(self, console_code: str = None,
                 reference_id: str = None,
                 cover_image: str = None,
                 title: str = None,
                 release_date: datetime = None,
                 release_year: int = None,
                 genre: str = None,
                 publisher: str = None,
                 owner: str = None):

        self.console_code = console_code
        self.reference_id = reference_id
        self.title = title
        self.genre = genre
        self.release_year = release_year
        self.cover_image = cover_image
        self.publisher = publisher
        self.owner = owner
        self.release_date = release_date

    @staticmethod
    def mapper(data):
        return Game(**data)
