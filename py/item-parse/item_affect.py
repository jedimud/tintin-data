from enum import Enum, unique


@unique
class ItemAffect(Enum):

    CON = "CON"
    STR = "STR"
    INT = "INT"
    WIS = "WIS"
    DEX = "DEX"
    CHARISMA = "CHARISMA"

    ARMOR = "ARMOR"

    AGE = "AGE"
    HEIGHT = "HEIGHT"

    HITROLL = "HITROLL"
    DAMROLL = "DAMROLL"

    MANA = "MANA"
    MANA_REGEN = "MANA_REGEN"

    HIT = "HIT"
    HIT_REGEN = "HIT_REGEN"

    MOV = "MOVE"
    MOVE_REGEN = "MOVE_REGEN"

    SAVE_SPELL = "SAVE_SPELL"