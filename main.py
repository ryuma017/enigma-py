from enigma import EnigmaI
from enigma.interior import PlugBoard, Rotor, Reflector


if __name__ == '__main__':

    plug_board = PlugBoard(pairs='AM FI NV PS TU WZ')

    # rotor1 = Rotor(name='III', initial_position='L')
    # rotor2 = Rotor(name='I', initial_position='B')
    # rotor3 = Rotor(name='II', initial_position='A')

    rotor1 = Rotor(name='III', initial_position='L', offset='V')
    rotor2 = Rotor(name='I', initial_position='B', offset='M')
    rotor3 = Rotor(name='II', initial_position='A', offset='X')

    reflector = Reflector(name='UKW-A')

    enigma = EnigmaI(plug_board, [rotor1, rotor2, rotor3], reflector)

    text = 'HELLO WORLD'
    encrypted_text = enigma.encrypt(text)
    print(encrypted_text)

    # text = 'EQENM URMGV, ZAOE QG URPBZZH ADWOI. AEQP WC KOLI EFK.'
    # decrypted_text = enigma.decrypt(text)
    # print(decrypted_text)

    # rotor = Rotor(name='I', initial_position='A', offset='B')
    # print(rotor.letters)
    # print(rotor.wiring)