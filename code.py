from keyboard import *


keyboard = Keyboard()

___ = TRANSPARENT
L1 = LAYER_TAP(1)
LSFT2 = LAYER_MODS(2, MODS(LSHIFT))
RSFT2 = LAYER_MODS(2, MODS(RSHIFT))

keyboard.keymap = (
    # layer 0
    (
        ESC,   1,   2,   3,   4,   5,   6,   7,   8,   9,   0, '-', '=', BACKSPACE,
        TAB,   Q,   W,   E,   R,   T,   Y,   U,   I,   O,   P, '[', ']', '|',
        L1,    A,   S,   D,   F,   G,   H,   J,   K,   L,  ';','"',    ENTER,
        LSFT2, Z,   X,   C,   V,   B,   N,   M, ',', '.', '/',         RSFT2,
        LCTRL, LALT, LGUI,          SPACE,            LEFT, DOWN, UP , RIGHT
    ),

    # layer 1
    (
        '`',  F1,  F2,  F3,  F4,  F5,  F6,  F7,  F8,  F9, F10, F11, F12, DEL,
        ___,RGB_MOD,RGB_VAL,___,___,___,___,___,___, ___,PRTSCN,___,___, INSERT,
        ___,HUE_RGB,VAL_RGB,RGB_HUE,___,___,LEFT,DOWN, UP,RIGHT,___,___,    ___,
        RSFT2, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,         CAPS,
        RCTRL, RALT, RGUI,                 ___,      HOME, PGDN, PGUP,  END
    ),

    # layer 2
    (
        '~', ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,
        ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,
        ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,      ___,
        ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,           ___,
        ___, ___, ___,                ___,               ___, ___, ___,  ___
    ),
)

# Backlight modes
# off: 0
# mono: 1
# gradient: 2
# spectrum: 3
# spectrum_x: 4
# spectrum_y: 5
# elapse: 6
# broadcast: 7
# blackhole: 8
# pinwheel: 9
# beacon: 10
# beacon2: 11

keyboard.backlight.set_mode(1)
keyboard.backlight.hue = 224
keyboard.backlight.val = 8
keyboard.backlight.enabled = True

keyboard.verbose = False
keyboard.run()
