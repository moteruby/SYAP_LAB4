class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        return print(f"Алфавит: {self.letters}")

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):
    def __init__(self):
        super().__init__('English', ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
                                     'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
                                     'u', 'v', 'w', 'x', 'y', 'z'])


# Пример использования класса EngAlphabet
eng_alphabet = EngAlphabet()
eng_alphabet.print()  # Выведет все буквы английского алфавита
print(eng_alphabet.letters_num())  # Выведет количество букв в английском алфавите
