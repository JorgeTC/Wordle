from src.leter_state import LeterState


class Answer():

    def __init__(self, word: str, colors: str="00000") -> None:
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

    def colorize_word(self, target):

        # Incializo una lista para guardar los colores
        colors = [LeterState.GREY] * 5

        not_green = set()
        # Escribo las letras acertadas
        for index, letter in enumerate(target):

            # Se ha acertado la letra, escribo un verde
            if letter == self.word[index]:
                colors[index] = LeterState.GREEN

            # En caso contrario la guardo como letra por adivinar
            not_green.add(letter)

        # Escribo las letras amarillas
        for index, letter in enumerate(self.word):

            # Si ya lo he pintado de verde, no hago nada más
            if colors[index] == LeterState.GREEN:
                continue

            # Si aún es gris, miro si es una letra que esté en la palabra
            if letter in not_green:
                colors[index] = LeterState.YELLOW

        return colors
