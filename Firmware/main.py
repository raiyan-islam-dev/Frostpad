import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.scanners.keypad import KeysScanner
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

keyboard.extensions.append(MediaKeys())

keyboard.matrix = KeysScanner(
    [board.D0, board.D1, board.D2, board.D3, board.D4, board.D5],
    value_when_pressed=False,
)

encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.D8, board.D7, board.D9),)
encoder_handler.map = (((KC.VOLD, KC.VOLU, KC.MUTE),),)
keyboard.modules.append(encoder_handler)

keyboard.keymap = [
    [KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6],
]

if __name__ == '__main__':
    keyboard.go()
