#!/usr/bin/env python3
from urllib.request import urlopen
from urllib.parse import quote
from urllib.parse import unquote
from queue import Queue
import re
import time


def get_content(name) -> str:
    """
    Функция возвращает содержимое вики-страницы name из русской Википедии.
    В случае ошибки загрузки или отсутствия страницы возвращается None.
    """
    path = "https://ru.wikipedia.org/wiki/" + quote(name)
    with urlopen(path) as source:
        text = source.read().decode("utf-8")
    return text
    pass


def extract_content(page) -> tuple:
    """
    Функция принимает на вход содержимое страницы и возвращает 2-элементный
    tuple, первый элемент которого — номер позиции, с которой начинается
    содержимое статьи, второй элемент — номер позиции, на котором заканчивается
    содержимое статьи.
    Если содержимое отсутствует, возвращается (0, 0).
    """
    if page is None:
        return 0, 0
    begins = list(re.finditer("<p>", page))
    ends = list(re.finditer("</p>", page))
    return begins[0].start(), ends[-1].end()
    pass


def extract_links(page, begin, end) -> list:
    """
    Функция принимает на вход содержимое страницы и начало и конец интервала,
    задающего позицию содержимого статьи на странице и возвращает все имеющиеся
    ссылки на другие вики-страницы без повторений и с учётом регистра.
    """
    text = page[begin:end]
    expression = re.compile(r'"/wiki/[^\s.jpeg]+"')
    links = re.findall(expression, text)
    result = set()
    for link in links:
        link = link.replace("\"", "")
        link = unquote(link).replace("/wiki/", "")
        result.add(link)
    return list(result)
    pass


def make_chain(paths: list, start: str) -> list:
    result = list()
    last_tuple = paths[-1]
    result.append(last_tuple[1])
    pre_last_page = last_tuple[0]
    result.append(pre_last_page)
    while pre_last_page != start:
        for (parent, child) in paths:
            if child == pre_last_page:
                pre_last_page = parent
                result.append(parent)
                break
    return result


def find_chain(start, finish):
    """
    Функция принимает на вход название начальной и конечной статьи и возвращает
    список переходов, позволяющий добраться из начальной статьи в конечную.
    Первым элементом результата должен быть start, последним — finish.
    Если построить переходы невозможно, возвращается None.
    """
    current_page_name = start
    visited = list()
    paths = list()
    q = Queue()
    q.put(("", current_page_name))
    while current_page_name != finish:
        # current_page_name = q.get()[1]
        current_tuple = q.get()
        paths.append(current_tuple)
        print(current_tuple)
        print("q size: " + str(q.qsize()) + " " + "v size: " + str(len(visited)))
        current_page_name = current_tuple[1]
        visited.append(current_page_name)
        current_page = get_content(current_page_name)
        borders = extract_content(current_page)
        pages_to_visit = extract_links(current_page, borders[0], borders[1])
        for page in pages_to_visit:
            if page not in visited:
                q.put((current_page_name, page))
            else:
                continue
    return make_chain(paths, start)
    pass


def main():
    find_chain("Транспортный самолёт", "Воздушное судно")
    pass


if __name__ == '__main__':
    main()
