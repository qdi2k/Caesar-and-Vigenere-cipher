from os import path
from typing import Dict, Tuple

from cipher import Caesar, Vigenere

language_dict: Dict[str, Tuple[str, str]] = {
            'рус': ('абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
                    'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'),
            'англ': ('abcdefghijklmnopqrstuvwxyz',
                     'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        }


def shift_input(len_alf) -> int:
    """ВВод длины сдвига"""
    shift: str = input('Введите шаг сдвига \n'
                       f'(число от 1 до {len_alf}): ')
    if not shift.isdigit() or int(shift) <= 0 or int(shift) > len_alf:
        while not shift.isdigit() or int(shift) <= 0 or int(
                shift) > len_alf:
            shift: str = input(
                f'Может попробуете ввести число от 1 до {len_alf}: ').strip()
    return int(shift)


def choice_of_two_input(a: str, b: str) -> str:
    """ВВод данных выбор из двух вариантов"""
    answer: str = input(f'Введите "{a}" или "{b}": ').strip().lower()
    if answer != a and answer != b:
        while answer != a and answer != b:
            answer: str = input(
                f'Может попробуете ввести "{a}" или "{b}"? ').strip().lower()
    return answer


def word_input(language) -> str:
    """ВВод слова-ключа"""
    word: str = input('Введите кодовое слово: ').strip().lower()
    if not (word.isalpha() or set(language).isdisjoint(word)):
        while not(word.isalpha() or set(language).isdisjoint(word)):
            word: str = input(
                f'Cлово должно состоять из \n'
                f'{language} \n'
                f'Попробуйте ещё раз: '
            ).strip().lower()
    return word


def read_file() -> str:
    """Чтение входного файла"""
    if not path.isfile('input.txt'):
        while not path.isfile('input.txt'):
            input('Убедитесь что файл input.txt находится в директории '
                  'с этой программой  ')
    with open('input.txt', 'r', encoding='utf-8') as old_file:
        return '\n'.join([line.strip() for line in old_file.readlines()])


def read_package() -> str:
    """Прочитать данные полученные от датчиков"""
    language: Tuple[str, str] = language_dict.get(
        choice_of_two_input('рус', 'англ'))
    cipher: str = choice_of_two_input('шифр', 'дешифр')
    text: str = read_file() if (choice_of_two_input('файл', 'консоль') == 'файл'
                                ) else input('Введите строку: ').strip()
    variant_encode: str = choice_of_two_input('цезарь', 'виженер')
    if variant_encode == 'цезарь':
        shift: int = shift_input(len(language[0]))
        encode: Caesar = Caesar(language, text, shift)
    else:
        word: str = word_input(language[0])
        encode: Vigenere = Vigenere(language, text, word)

    cipher_dict = {
        'шифр': encode.get_encrypt(),
        'дешифр': encode.get_decrypt()
    }
    return cipher_dict.get(cipher)


def main() -> None:
    """Главная функция"""
    if __name__ == '__main__':
        print('Добро пожаловать в программу для шифрования текста')
        print(read_package())
        input('Нажмите Enter для выхода: ')


if __name__ == '__main__':
    main()
