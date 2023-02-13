import requests
from bs4 import BeautifulSoup


def count_html_tags(url: str, attributes: bool = False) -> int:
    counter = 0
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    all_html_tags = soup.findAll()
    if attributes:
        for tag in all_html_tags:
            if tag.attrs:
                counter += 1
        return counter
    else:
        return len(all_html_tags)


if __name__ == "__main__":
    url = "https://greenatom.ru/"
    print(f"Количество HTML-тегов в коде главной страницы сайта greenatom.ru: {count_html_tags(url=url)}.")
    print(f"Среди них тегов с атрибутами: {count_html_tags(url=url, attributes=True)}")
    