import libtcodpy as libtcod

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

libtcod.console_set_custom_font('terminal12x12_gs_ro.png',
                                libtcod.FONT_TYPE_GREYSCALE |
                                libtcod.FONT_LAYOUT_ASCII_INROW)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT,
                          'basicroguelike', False)

while not libtcod.console_is_window_closed():
    libtcod.console_set_default_foreground(0, libtcod.white)
    libtcod.console_put_char(0, 1, 1, '@', libtcod.BKGND_NONE)
    libtcod.console_flush()
