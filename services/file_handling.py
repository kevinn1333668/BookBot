import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}

def _get_part_text(text: str, start: int, page_size: int) -> tuple[str, int]:
    end_simbol = ['.', ',', '!', ':', ';', '?']
    end = start+page_size
    while text[end:][:1] in end_simbol:
        end -= 1
    text = text[start:end]
    text = text[: max(map(text.rfind, end_simbol))+1]
    return text, len(text)





def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='UTF-8') as file:
        text = file.read()
        page_text: bool | str = True
        page = 1
        size = 0

        while page_text:
            page_text, temp_size = _get_part_text(text, size, PAGE_SIZE)
            if not(temp_size):
                break
            book[page] = page_text.lstrip()
            page += 1
            size += temp_size

prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))