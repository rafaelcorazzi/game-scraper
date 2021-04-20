import bs4
import requests
from bs4 import BeautifulSoup
import base64
import hashlib
from typing import List
import re
from src.helpers.utils import Utils
from src.domain.console_domain import ConsolePlataform
from src.domain.console_games_domain import ConsoleGames
from src.domain.game_domain import Game
import maya
import uuid

class ScraperServices:
    @staticmethod
    def __html_result(url: str = None) -> bs4.BeautifulSoup:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        return soup

    @staticmethod
    def game_details(link: str = None, reference_id: str = None, console_code: str = None) -> Game:
        page = ScraperServices.__html_result(f'https://jogorama.com.br/{link}/')
        data_sheet = page.select('.ficha')
        title = re.sub('[^A-Za-z0-9]+', ' ', str(page.findAll('span', attrs={"itemprop": "name"})[0].text))
        owner = re.sub('[^A-Za-z0-9]+', ' ', str(page.findAll('span', attrs={"itemprop": "author"})[0].text))
        publisher = re.sub('[^A-Za-z0-9]+', ' ', str(page.findAll('span', attrs={"itemprop": "publisher"})[0].text))
        genre = '' if len(page.findAll('span', attrs={"itemprop": "genre"})) == 0 else str(page.findAll('span', attrs={"itemprop": "genre"})[0].text)

        game_detail: Game = Game()
        release_year = 0
        release_month = 0
        release_day = 0
        release_date = ''
        if re.search('<b>Lançamento:</b>([^,]+)<br/>', str(data_sheet[0])) is not None:
            released = re.search('<b>Lançamento:</b>([^,]+)<br/>', str(data_sheet[0])).group(1)
            result = re.findall(r'\d+', released)[0];
            release_day = int(result) if len(result) == 2 else 0
            release_year = result if len(result) == 4 else re.findall(r'\d+', released)[1]
            if re.search(r'(?<=de)([\S\s]*)(?=de)', released) is not None:
                release_month = Utils.month_converter(re.search(r'(?<=de)([\S\s]*)(?=de)', released).group(1).replace(' ', ''))

        if release_month > 0 and release_day > 0:
            release_date = maya.parse(f'{release_year}-{release_month}-{release_day}').datetime()

        game_detail.reference_id = reference_id
        game_detail.title = title
        game_detail.console_code = console_code
        game_detail.release_date = release_date
        game_detail.release_year = release_year
        game_detail.cover_image = base64.b64encode(requests.get(f"https://jogorama.com.br/thumbr.php?l=180&a=400&img=capas/{reference_id}.jpg").content)
        game_detail.owner = owner
        game_detail.publisher = publisher
        game_detail.genre = genre
        #print(f'{reference_id} - {title} - {owner} - {publisher} - {genre} - {release_date} - {release_year}')
        return game_detail

    @staticmethod
    def list_of_games_by_plataform(console_code: str = None) -> List[ConsoleGames]:
        page = ScraperServices.__html_result(f'https://jogorama.com.br/jogos/{console_code}/lista-de-jogos/')
        rows_games = page.select('.lista')
        glst = []
        for r in rows_games:
            consoles_games = r.select('li')
            for c in consoles_games:
                for z in c.find_all('a', href=True):
                    game_list: ConsoleGames = ConsoleGames()
                    game_list.console_code = console_code
                    game_list.reference_id = z['href'].split("/")[3]
                    game_list.title = z['title'].strip()
                    game_list.link = z['href']
                    glst.append(game_list.to_json())
        return glst

    @staticmethod
    def list_of_console() -> List[ConsolePlataform]:
        # ToDo: alterar para config
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
                    console.console_uuid = str(uuid.uuid5(uuid.NAMESPACE_URL, b.select_one('a').text.strip().replace(' ', '-').lower()))
                    plt.append(console.to_json())

        return plt
