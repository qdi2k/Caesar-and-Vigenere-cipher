from typing import Tuple


class Encryption:
    """Базовый класс кодирования"""
    FIRST_ALF: int = 0
    SECOND_ALF: int = 1

    def __init__(self,
                 language: Tuple[str, str],
                 text: str) -> None:
        self.language = language
        self.text = text

    def get_len_language(self) -> int:
        """Получить длину алфавита"""
        return len(self.language[self.FIRST_ALF])

    def get_len_text(self) -> int:
        """Получить длину текста"""
        return len(self.text)

    def get_char(self, char: str, case: str,  key: int) -> str:
        """Получить символ кодирования"""
        return case[(case.find(char) + key + self.get_len_language())
                    % self.get_len_language()]


class Caesar(Encryption):
    """Шифрование Цезаря"""
    def __init__(self,
                 language: Tuple[str, str],
                 text: str,
                 shift: int) -> None:
        super().__init__(language, text)
        self.shift = shift

    def encode(self, key: int, lowercase: str, uppercase: str) -> str:
        """Формирование выдаваемого текста"""
        total: str = ''
        for char in self.text:
            if char in lowercase:
                total += self.get_char(char, lowercase, key)
            elif char in uppercase:
                total += self.get_char(char, uppercase, key)
            else:
                total += char
        return total

    def get_encrypt(self) -> str:
        """Получение кодированного текста"""
        return self.encode(self.shift, self.language[self.FIRST_ALF],
                           self.language[self.SECOND_ALF])

    def get_decrypt(self) -> str:
        """Получение декодированного текста"""
        return self.encode(-self.shift, self.language[self.FIRST_ALF],
                           self.language[self.SECOND_ALF])


class Vigenere(Encryption):
    """Шифрование Виженера"""
    def __init__(self,
                 language: Tuple[str, str],
                 text: str,
                 word: str) -> None:
        super().__init__(language, text)
        self.word = word

    def get_repeat_key(self):
        """Получение повторяющегося ключа"""
        return (self.word * (self.get_len_text() // len(self.word) + 1)
                )[:self.get_len_text()]

    def encode(self,
               key: str,
               lowercase: str,
               uppercase: str,
               encrypting=True) -> str:
        """Формирование выдаваемого текста"""
        total: str = ''
        for i in range(len(self.text)):
            if self.text[i] in lowercase:
                total += self.get_char(self.text[i], lowercase,
                                       lowercase.find(key[i]) if encrypting
                                       else - lowercase.find(key[i]))
            elif self.text[i] in uppercase:
                total += self.get_char(self.text[i], uppercase,
                                       lowercase.find(key[i]) if encrypting
                                       else - lowercase.find(key[i]))
            else:
                total += self.text[i]
        return total

    def get_encrypt(self) -> str:
        """Получение кодированного текста"""
        return self.encode(self.get_repeat_key(),
                           self.language[self.FIRST_ALF],
                           self.language[self.SECOND_ALF])

    def get_decrypt(self) -> str:
        """Получение декодированного текста"""
        return self.encode(self.get_repeat_key(),
                           self.language[self.FIRST_ALF],
                           self.language[self.SECOND_ALF],
                           encrypting=False)
