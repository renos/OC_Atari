from termcolor import colored
from .boxing import _detect_objects_boxing_raw, _detect_objects_boxing_revised, _init_objects_boxing_ram
from .bowling import _detect_objects_bowling_raw, _detect_objects_bowling_revised
from .breakout import _detect_objects_breakout_raw, _detect_objects_breakout_revised
from .freeway import _detect_objects_freeway_raw, _detect_objects_freeway_revised
from .pong import _detect_objects_pong_raw, _detect_objects_pong_revised, _init_objects_pong_ram
from .seaquest import _detect_objects_seaquest_raw, _detect_objects_seaquest_revised
from .skiing import _detect_objects_skiing_raw, _detect_objects_skiing_revised, _init_objects_skiing_ram
from .space_invaders import _detect_objects_space_invaders_raw, \
                            _detect_objects_space_invaders_revised
from .tennis import _detect_objects_tennis_raw, _detect_objects_tennis_revised


def init_objects(game_name, hud):
    """
    Initialize the object list for the correct game
    """
    if game_name.lower() == "boxing":
        return _init_objects_boxing_ram(hud)
    # elif game_name.lower() == "breakout":
    #     _detect_objects_breakout(objects, ram_state)
    # elif game_name.lower() == "freeway":
    #     _detect_objects_freeway(objects, ram_state)
    elif game_name.lower() == "pong":
        return _init_objects_pong_ram(hud)
    elif game_name.lower() == "skiing":
        return _init_objects_skiing_ram(hud)
    # elif game_name.lower() == "seaquest":
    #     _detect_objects_seaquest(objects, ram_state)
    # elif game_name.lower() == "spaceinvaders":
    #     _detect_objects_space_invaders(objects, ram_state)
    # elif game_name.lower() == "tennis":
    #     _detect_objects_tennis(objects, ram_state)
    else:
        print(colored("Uncovered game in revised mode", "red"))
        exit(1)


def detect_objects_raw(info, ram_state, game_name):
    """
    Augment the info dictionary with object centric information
    """
    if game_name.lower() == "boxing":
        _detect_objects_boxing_raw(info, ram_state)
    elif game_name.lower() == "breakout":
        _detect_objects_breakout_raw(info, ram_state)
    elif game_name.lower() == "freeway":
        _detect_objects_freeway_raw(info, ram_state)
    elif game_name.lower() == "pong":
        _detect_objects_pong_raw(info, ram_state)
    elif game_name.lower() == "skiing":
        _detect_objects_skiing_raw(info, ram_state)
    elif game_name.lower() == "seaquest":
        _detect_objects_seaquest_raw(info, ram_state)
    elif game_name.lower() == "spaceinvaders":
        _detect_objects_space_invaders_raw(info, ram_state)
    elif game_name.lower() == "tennis":
        _detect_objects_tennis_raw(info, ram_state)
    elif game_name.lower() == "bowling":
        _detect_objects_bowling_raw(info, ram_state)
    else:
        print(colored("Uncovered game in raw mode", "red"))
        exit(1)


def detect_objects_revised(info, ram_state, game_name, hud):
    """
    Augment the info dictionary with object centric information
    """
    if game_name.lower() == "boxing":
        _detect_objects_boxing_revised(info, ram_state, hud)
    elif game_name.lower() == "breakout":
        _detect_objects_breakout_revised(info, ram_state, hud)
    elif game_name.lower() == "freeway":
        _detect_objects_freeway_revised(info, ram_state, hud)
    elif game_name.lower() == "pong":
        _detect_objects_pong_revised(info, ram_state, hud)
    elif game_name.lower() == "skiing":
        _detect_objects_skiing_revised(info, ram_state, hud)
    elif game_name.lower() == "seaquest":
        _detect_objects_seaquest_revised(info, ram_state, hud)
    elif game_name.lower() == "spaceinvaders":
        _detect_objects_space_invaders_revised(info, ram_state, hud)
    elif game_name.lower() == "tennis":
        _detect_objects_tennis_revised(info, ram_state, hud)
    elif game_name.lower() == "bowling":
        _detect_objects_bowling_revised(info, ram_state, hud)
    else:
        print(colored("Uncovered game in revised mode", "red"))
        exit(1)
