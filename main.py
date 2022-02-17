import re

from src.answer import Answer
from src.matcher import Match, LINES


def main():

    while len(Match.possibles) > 1:
        inserted_word = ask_for_word()
        color_pattern = ask_for_pattern()
        answer = Answer(inserted_word, color_pattern)
        Match.possibles = Match.get_possibles(answer)
        Match.print()
        print(Match.suggestion())


def ask_for_word():

    while True:
        # Pido al usuario
        ans = input("Palabra introducida ").lower()

        # Compruebo que la palabra introducida esté aceptada por Wordle
        if ans not in LINES:
            continue

        # La palabra es correcta
        return ans


def ask_for_pattern():

    while True:

        ans = input("Patron de colores ")

        if re.match(r"[0-2]{5}", ans):
            return ans


if __name__ == "__main__":
    main()
