from src.domain.base_domain import BaseDomain
from datetime import datetime


class ConsoleGames(BaseDomain):
    def __init__(self, console_code: str = None,
                 reference_id: str = None,
                 title: str = None,
                 link: str = None):

        self.console_code = console_code
        self.reference_id = reference_id
        self.title = title
        self.link = link


    @staticmethod
    def mapper(data):
        return ConsoleGames(**data)
