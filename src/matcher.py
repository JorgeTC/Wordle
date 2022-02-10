import concurrent.futures
from itertools import repeat

from src.answer import Answer
from src.leter_state import LeterState

# Cargo la lista con todas las palabras
all_words = open("res/list.txt", "r", encoding="utf-8")
LINES = all_words.readlines()
# Elimino los saltos de linea
LINES = [word[:-1] for word in LINES]
all_words.close()


class Match():

    # Palabras posibles, actualizaré esta lista
    possibles = LINES.copy()

    count_in_parallel = concurrent.futures.ThreadPoolExecutor(max_workers=100)

    @classmethod
    def get_possibles(cls, answer: Answer):
        new_possibles = []

        for word in cls.possibles:

            if not possible_word(word, answer):
                continue

            new_possibles.append(word)

        return new_possibles

    @classmethod
    def count_possibles(cls, answer: Answer) -> int:

        count_in_parallel = concurrent.futures.ThreadPoolExecutor(max_workers=100)
        counter = sum(
            list(count_in_parallel.map(possible_word, cls.possibles, repeat(answer))))

        return counter

    @classmethod
    def print(cls):
        for word in cls.possibles:
            print(word)

    @classmethod
    def suggestion(cls):

        suggestion = ""
        min_punctuation = len(LINES)

        # Itero todas las palabras que me permite el juego
        for word in LINES:

            # Evalúo la palabra
            curr_punctuation = cls.punctuation_for_word(word)

            # Si la palabra me descarta más elementos, la tomo como nueva sugerencia
            if curr_punctuation < min_punctuation:
                suggestion = word
                min_punctuation = curr_punctuation

        return suggestion

    @classmethod
    def punctuation_for_word(cls, word):

        answer = Answer(word)
        punctuation = 0

        # Iteremos todas las posibles respuestas
        executor = concurrent.futures.ThreadPoolExecutor(max_workers=100)
        punctuation = sum(list(executor.map(
            cls.punctuation_for_word_and_target, repeat(answer), cls.possibles)))
        # for target in cls.possibles:
        #     punctuation += cls.punctuation_for_word_and_target(answer, target)

        # Hago una media y la devuelvo
        return punctuation/len(cls.possibles)

    @classmethod
    def punctuation_for_word_and_target(cls, answer: Answer, target: str):
        # Coloreemos la palabra con el target actual
        answer.colors = answer.colorize_word(target)
        answer.required_letters = answer.def_required_place_letters()
        answer.not_pressent_letters = answer.def_not_pressent_letters()

        # Dada esa respuesta, obtengamos cuántas palabras válidas existen
        return cls.count_possibles(answer)


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
