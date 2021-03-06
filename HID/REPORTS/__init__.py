# encoding=utf-8
import HID.CODE

RELEASE = bytes([0] * 8)

CHARS = {
    'a': bytes([0, 0, HID.CODE.KEY_A, *[0] * 5]), 'A': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_A, *[0] * 5]),
    'b': bytes([0, 0, HID.CODE.KEY_B, *[0] * 5]), 'B': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_B, *[0] * 5]),
    'c': bytes([0, 0, HID.CODE.KEY_C, *[0] * 5]), 'C': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_C, *[0] * 5]),
    'd': bytes([0, 0, HID.CODE.KEY_D, *[0] * 5]), 'D': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_D, *[0] * 5]),
    'e': bytes([0, 0, HID.CODE.KEY_E, *[0] * 5]), 'E': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_E, *[0] * 5]),
    'f': bytes([0, 0, HID.CODE.KEY_F, *[0] * 5]), 'F': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_F, *[0] * 5]),
    'g': bytes([0, 0, HID.CODE.KEY_G, *[0] * 5]), 'G': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_G, *[0] * 5]),
    'h': bytes([0, 0, HID.CODE.KEY_H, *[0] * 5]), 'H': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_H, *[0] * 5]),
    'i': bytes([0, 0, HID.CODE.KEY_I, *[0] * 5]), 'I': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_I, *[0] * 5]),
    'j': bytes([0, 0, HID.CODE.KEY_J, *[0] * 5]), 'J': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_J, *[0] * 5]),
    'k': bytes([0, 0, HID.CODE.KEY_K, *[0] * 5]), 'K': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_K, *[0] * 5]),
    'l': bytes([0, 0, HID.CODE.KEY_L, *[0] * 5]), 'L': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_L, *[0] * 5]),
    'm': bytes([0, 0, HID.CODE.KEY_M, *[0] * 5]), 'M': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_M, *[0] * 5]),
    'n': bytes([0, 0, HID.CODE.KEY_N, *[0] * 5]), 'N': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_N, *[0] * 5]),
    'o': bytes([0, 0, HID.CODE.KEY_O, *[0] * 5]), 'O': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_O, *[0] * 5]),
    'p': bytes([0, 0, HID.CODE.KEY_P, *[0] * 5]), 'P': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_P, *[0] * 5]),
    'q': bytes([0, 0, HID.CODE.KEY_Q, *[0] * 5]), 'Q': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_Q, *[0] * 5]),
    'r': bytes([0, 0, HID.CODE.KEY_R, *[0] * 5]), 'R': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_R, *[0] * 5]),
    's': bytes([0, 0, HID.CODE.KEY_S, *[0] * 5]), 'S': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_S, *[0] * 5]),
    't': bytes([0, 0, HID.CODE.KEY_T, *[0] * 5]), 'T': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_T, *[0] * 5]),
    'u': bytes([0, 0, HID.CODE.KEY_U, *[0] * 5]), 'U': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_U, *[0] * 5]),
    'v': bytes([0, 0, HID.CODE.KEY_V, *[0] * 5]), 'V': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_V, *[0] * 5]),
    'w': bytes([0, 0, HID.CODE.KEY_W, *[0] * 5]), 'W': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_W, *[0] * 5]),
    'x': bytes([0, 0, HID.CODE.KEY_X, *[0] * 5]), 'X': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_X, *[0] * 5]),
    'y': bytes([0, 0, HID.CODE.KEY_Y, *[0] * 5]), 'Y': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_Y, *[0] * 5]),
    'z': bytes([0, 0, HID.CODE.KEY_Z, *[0] * 5]), 'Z': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_Z, *[0] * 5]),

    '1': bytes([0, 0, HID.CODE.KEY_1, *[0] * 5]), '!': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_1, *[0] * 5]),
    '2': bytes([0, 0, HID.CODE.KEY_2, *[0] * 5]), '@': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_2, *[0] * 5]),
    '3': bytes([0, 0, HID.CODE.KEY_3, *[0] * 5]), '#': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_3, *[0] * 5]),
    '4': bytes([0, 0, HID.CODE.KEY_4, *[0] * 5]), '$': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_4, *[0] * 5]),
    '5': bytes([0, 0, HID.CODE.KEY_5, *[0] * 5]), '%': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_5, *[0] * 5]),
    '6': bytes([0, 0, HID.CODE.KEY_6, *[0] * 5]), '^': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_6, *[0] * 5]),
    '7': bytes([0, 0, HID.CODE.KEY_7, *[0] * 5]), '&': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_7, *[0] * 5]),
    '8': bytes([0, 0, HID.CODE.KEY_8, *[0] * 5]), '*': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_8, *[0] * 5]),
    '9': bytes([0, 0, HID.CODE.KEY_9, *[0] * 5]), '(': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_9, *[0] * 5]),
    '0': bytes([0, 0, HID.CODE.KEY_0, *[0] * 5]), ')': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_0, *[0] * 5]),

    '\n': bytes([0, 0, HID.CODE.ENTER, *[0] * 5]),
    'ESC': bytes([0, 0, HID.CODE.ESC, *[0] * 5]),
    'BACKSPACE': bytes([0, 0, HID.CODE.BACKSPACE, *[0] * 5]),
    '\t': bytes([0, 0, HID.CODE.TAB, *[0] * 5]),
    ' ': bytes([0, 0, HID.CODE.SPACE, *[0] * 5]),
    '-': bytes([0, 0, HID.CODE.KEY_MINUS, *[0] * 5]), '_': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_MINUS, *[0] * 5]),
    '=': bytes([0, 0, HID.CODE.KEY_EQUAL, *[0] * 5]), '+': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.KEY_EQUAL, *[0] * 5]),
    '[': bytes([0, 0, HID.CODE.OPEN_SQUARE_BRACKET, *[0] * 5]), '{': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.OPEN_SQUARE_BRACKET, *[0] * 5]),
    ']': bytes([0, 0, HID.CODE.CLOSE_SQUARE_BRACKET, *[0] * 5]), '}': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.CLOSE_SQUARE_BRACKET, *[0] * 5]),
    '\\': bytes([0, 0, HID.CODE.BACKSLASH, *[0] * 5]), '|': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.BACKSLASH, *[0] * 5]),
    ';': bytes([0, 0, HID.CODE.SEMICOLON, *[0] * 5]), ':': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.SEMICOLON, *[0] * 5]),
    '\'': bytes([0, 0, HID.CODE.SINGLE_QUOTE, *[0] * 5]), '"': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.SINGLE_QUOTE, *[0] * 5]),
    '`': bytes([0, 0, HID.CODE.BACKTICK, *[0] * 5]), '~': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.BACKTICK, *[0] * 5]),
    ',': bytes([0, 0, HID.CODE.COMMA, *[0] * 5]), '<': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.COMMA, *[0] * 5]),
    '.': bytes([0, 0, HID.CODE.DOT, *[0] * 5]), '>': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.DOT, *[0] * 5]),
    '/': bytes([0, 0, HID.CODE.SLASH, *[0] * 5]), '?': bytes([HID.CODE.LEFT_SHIFT, 0, HID.CODE.SLASH, *[0] * 5]),

    'F1': bytes([0, 0, HID.CODE.F1, *[0] * 5]),
    'F2': bytes([0, 0, HID.CODE.F2, *[0] * 5]),
    'F3': bytes([0, 0, HID.CODE.F3, *[0] * 5]),
    'F4': bytes([0, 0, HID.CODE.F4, *[0] * 5]),
    'F5': bytes([0, 0, HID.CODE.F5, *[0] * 5]),
    'F6': bytes([0, 0, HID.CODE.F6, *[0] * 5]),
    'F7': bytes([0, 0, HID.CODE.F7, *[0] * 5]),
    'F8': bytes([0, 0, HID.CODE.F8, *[0] * 5]),
    'F9': bytes([0, 0, HID.CODE.F9, *[0] * 5]),
    'F10': bytes([0, 0, HID.CODE.F10, *[0] * 5]),
    'F11': bytes([0, 0, HID.CODE.F11, *[0] * 5]),
    'F12': bytes([0, 0, HID.CODE.F12, *[0] * 5]),
}
