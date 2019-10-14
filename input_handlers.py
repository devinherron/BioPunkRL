import tcod

from game_states import GameStates


move_north_char = ['k']
move_north_keys = [tcod.KEY_UP, tcod.KEY_KP8]
move_south_char = ['j']
move_south_keys = [tcod.KEY_DOWN, tcod.KEY_KP2]
move_west_char = ['h']
move_west_keys = [tcod.KEY_LEFT, tcod.KEY_KP4]
move_east_char = ['l']
move_east_keys = [tcod.KEY_RIGHT, tcod.KEY_KP6]
move_northwest_char = ['y']
move_northwest_keys = [tcod.KEY_KP7]
move_northeast_char = ['u']
move_northeast_keys = [tcod.KEY_KP9]
move_southwest_char = ['b']
move_southwest_keys = [tcod.KEY_KP1]
move_southeast_char = ['n']
move_southeast_keys = [tcod.KEY_KP3]
wait_char = ['.']
wait_keys = [tcod.KEY_KP5]


def handle_keys(key, game_state):
    if game_state == GameStates.PLAYERS_TURN:
        return handle_player_turn_keys(key)
    elif game_state == GameStates.PLAYER_DEAD:
        return handle_player_dead_keys(key)
    elif game_state == GameStates.TARGETING:
        return handle_targeting_keys(key)
    elif game_state in (GameStates.SHOW_INVENTORY, GameStates.DROP_INVENTORY):
        return handle_inventory_keys(key)

    return {}


def handle_player_turn_keys(key):
    key_char = chr(key.c)

    # Movement keys
    if key.vk in move_north_keys or key_char in move_north_char:
        return {'move': (0, -1)}
    elif key.vk in move_south_keys or key_char in move_south_char:
        return {'move': (0, 1)}
    elif key.vk in move_west_keys or key_char in move_west_char:
        return {'move': (-1, 0)}
    elif key.vk in move_east_keys or key_char in move_east_char:
        return {'move': (1, 0)}
    elif key.vk in move_northwest_keys or key_char in move_northwest_char:
        return {'move': (-1, -1)}
    elif key.vk in move_northeast_keys or key_char in move_northeast_char:
        return {'move': (1, -1)}
    elif key.vk in move_southwest_keys or key_char in move_southwest_char:
        return {'move': (-1, 1)}
    elif key.vk in move_southeast_keys or key_char in move_southeast_char:
        return {'move': (1, 1)}
    elif key.vk in wait_keys or key_char in wait_char:
        return {'wait': True}

    if key_char == 'g':
        return {'pickup': True}
    elif key_char == 'i':
        return {'show_inventory': True}
    elif key_char == 'd':
        return {'drop_inventory': True}

    if key.vk == tcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}

    elif key.vk == tcod.KEY_ESCAPE:
        # Exit the game
        return {'exit': True}

    # No key was pressed
    return {}


def handle_targeting_keys(key):
    if key.vk == tcod.KEY_ESCAPE:
        return {'exit': True}

    return {}


def handle_player_dead_keys(key):
    key_char = chr(key.c)

    if key_char == 'i':
        return {'show_inventory': True}

    if key.vk == tcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}
    elif key.vk == tcod.KEY_ESCAPE:
        # Exit the menu
        return {'exit': True}

    return {}


def handle_inventory_keys(key):
    index = key.c - ord('a')

    if index >= 0:
        return {'inventory_index': index}

    if key.vk == tcod.KEY_ENTER and key.lalt:
        return {'fullscreen': True}
    elif key.vk == tcod.KEY_ESCAPE:
        return {'exit': True}

    return {}


def handle_main_menu(key):
    key_char = chr(key.c)

    if key_char == 'a':
        return {'new_game': True}
    elif key_char == 'b':
        return {'load_game': True}
    elif key_char == 'c' or key.vk == tcod.KEY_ESCAPE:
        return {'exit': True}

    return {}


def handle_mouse(mouse):
    (x, y) = (mouse.cx, mouse.cy)

    if mouse.lbutton_pressed:
        return {'left_click': (x, y)}
    elif mouse.rbutton_pressed:
        return {'right_click': (x, y)}

    return {}
