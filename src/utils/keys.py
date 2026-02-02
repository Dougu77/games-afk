from pynput.keyboard import KeyCode, Key
from enum import Enum

class KeysChoice(int, Enum):
    WASD = 1
    ARROWS = 2

WASD_KEYS = [
    KeyCode.from_char('w'),
    KeyCode.from_char('a'),
    KeyCode.from_char('s'),
    KeyCode.from_char('d'),
]

ARROW_KEYS = [
    Key.up,
    Key.left,
    Key.down,
    Key.right,
]

KEYS_NAMES = {
    KeyCode.from_char('w'): 'W',
    KeyCode.from_char('a'): 'A',
    KeyCode.from_char('s'): 'S',
    KeyCode.from_char('d'): 'D',
    Key.up: 'Cima',
    Key.left: 'Esquerda',
    Key.down: 'Baixo',
    Key.right: 'Direita',
}

def get_key_name(key: Key | KeyCode) -> str:
    return KEYS_NAMES.get(key, str(key))
