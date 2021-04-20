from src.domain.base_domain import BaseDomain


class ConsolePlataform(BaseDomain):
    def __init__(self, console_plataform_name: str = None,
                 console_plataform_code: str = None,
                 console_uuid: str = None):
        self.console_plataform_name = console_plataform_name
        self.console_plataform_code = console_plataform_code
        self.console_uuid = console_uuid

    @staticmethod
    def mapper(data):
        return ConsolePlataform(**data)
