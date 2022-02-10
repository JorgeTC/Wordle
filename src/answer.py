from src.leter_state import LeterState


class Answer():

    def __init__(self, word: str, colors: str) -> None:
        self.word = word.lower()
        self.colors = self.str_to_colors(colors)
        self.required_letters = self.def_required_place_letters()
        self.not_pressent_letters = self.def_not_pressent_letters()

    def def_not_pressent_letters(self):

        invalid_letters = set()

        for leter, state in zip(self.word, self.colors):
            if state != LeterState.GREY:
                continue
            if leter not in self.required_letters:
                invalid_letters.add(leter)

        return invalid_letters

    def def_required_place_letters(self):

        required = set()

        for leter, state in zip(self.word, self.colors):
            if state == LeterState.YELLOW or state == LeterState.GREEN:
                required.add(leter)

        return required

    def str_to_colors(self, colors):

        return [LeterState(int(char)) for char in colors]
