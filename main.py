import re

from src.answer import Answer
from src.matcher import Match


def main():

    while len(Match.possibles) > 1:
        print(Match.suggestion())
        inserted_word = ask_for_word()
        color_pattern = ask_for_pattern()
        answer = Answer(inserted_word, color_pattern)
        Match.possibles = Match.get_possibles(answer)
        Match.print()


def ask_for_word():

    while True:
        # Pido al usuario
        ans = input("Palabra introducida ")

        # Compruebo que la palabra introducida esté aceptada por Wordle
        if ans not in Match.lines:
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
