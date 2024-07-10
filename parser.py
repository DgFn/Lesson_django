import dataclasses
from pprint import pprint

import requests
from bs4 import BeautifulSoup


@dataclasses.dataclass
class Parser:
    title: str
    subtitle: list

    def get(self):
        return dataclasses.asdict(self)


def main():
    dict_title = []
    r = requests.get('https://teachmeskills.by/kursy/obuchenie-python-online',
                     headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    soup = BeautifulSoup(r.text, 'html.parser')
    links = soup.find_all('div', class_='t517__sectioninfowrapper')
    for link in links:
        title = link.find('div', class_='t517__section-title t-name t-name_lg t517__bottommargin')
        subtitles = link.find('div', class_='t517__section-text t-text t-text_sm')

        if title is None:
            continue
        if subtitles is None:
            continue

        c = Parser(title.text, subtitles.text)
        dict_title.append(c.get())
    print(dict_title)


main()

