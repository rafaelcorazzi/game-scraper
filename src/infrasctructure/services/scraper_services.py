import bs4
import requests
from bs4 import BeautifulSoup
import base64
import hashlib
from typing import List

from src.domain.console_domain import ConsolePlataform

class ScraperServices:
    @staticmethod
    def __html_result(url: str = None) -> bs4.BeautifulSoup:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        return soup

    @staticmethod
    def list_of_console() -> List[ConsolePlataform]:
        #ToDo: alterar para config
        page = ScraperServices.__html_result('https://jogorama.com.br/')
        rows = page.select('.menu')
        plt = []

        i = 0
        for a in rows:
            i += 1
            if i == 2:
                consoles = a.select('li')  # a.select('')
                for b in consoles:
                    console: ConsolePlataform = ConsolePlataform()
                    console.console_plataform_name = b.select_one('a').text.strip()
                    console.console_plataform_code = b.select_one('a').text.strip().replace(' ', '-').lower()
                    plt.append(console)

        return plt