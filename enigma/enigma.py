from dataclasses import dataclass

from .interior import PlugBoard, Rotor, Reflector, LETTERS


@dataclass
class EnigmaI:

    plug_board: PlugBoard
    rotors: list[Rotor]
    reflector: Reflector
    cnt: int = 1

    def encrypt(self, text):
        return ''.join([self.__go_through(char) for char in text])

    def decrypt(self, text):
        return self.encrypt(text)

    def __go_through(self, char):

        char = char.upper()
        if char not in LETTERS:
            return char

        # for rotor in self.rotors:
        #     rotor.step()
        #     if rotor.letters[-1] != rotor.notch:
        #         break

        for i, rotor in enumerate(self.rotors[:-1]):
            if rotor.letters[0] == rotor.notch:
                next_roter = self.rotors[i+1]
                rotor.step()
                next_roter.step()
            elif i == 0:
                rotor.step()
            else:
                break

        # V Q

        print(self.cnt, '|', self.rotors[0].letters[0], self.rotors[0].steps,
                             self.rotors[1].letters[0], self.rotors[1].steps,
                             self.rotors[2].letters[0], self.rotors[2].steps)
        self.cnt += 1

        index = LETTERS.index(char)

        index = self.plug_board.convert_forward(index)

        for rotor in self.rotors:
            index = rotor.convert_forward(index)


        index = self.reflector.reflect(index)

        for rotor in reversed(self.rotors):
            index = rotor.convert_backward(index)

        index = self.plug_board.convert_backward(index)

        return LETTERS[index]
