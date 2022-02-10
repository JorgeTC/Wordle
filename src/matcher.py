from src.leter_state import LeterState
from src.answer import Answer


class Match():

    # Cargo la lista con todas las palabras
    all_words = open("res/list.txt", "r", encoding="utf-8")
    lines = all_words.readlines()
    # Elimino los saltos de linea
    lines = [word[:-1] for word in lines]
    # Palabras posibles, actualizaré esta lista
    possibles = lines.copy()
    all_words.close()

    @classmethod
    def update_possibles(cls, answer: Answer):

        new_possibles = []

        for word in cls.possibles:

            if not possible_word(word, answer):
                continue

            new_possibles.append(word)

        cls.possibles = new_possibles

    @classmethod
    def print(cls):
        for word in cls.possibles:
            print(word)


def possible_word(word: str, answer: Answer):

    required_letters = answer.required_letters.copy()

    for index, letter in enumerate(word):

        # Miro que la letra no esté ya prohibida
        if letter in answer.not_pressent_letters:
            return False

        # Miro qué me dicen los colores de la posición actual
        if answer.colors[index] == LeterState.GREEN and letter != answer.word[index]:
            return False

        # Elimino la letra actual del conjunto
        required_letters.discard(letter)

    return len(required_letters) == 0
