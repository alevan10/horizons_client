from enum import Enum


class Planets(str, Enum):
    MERCURY = 199
    VENUS = 299
    EARTH = 399
    MARS = 499
    JUPITER = 599
    SATURN = 699
    URANUS = 799
    NEPTUNE = 899


class Observers(str, Enum):
    SUN = "@10"
    EARTH = f"@{Planets.EARTH}"


class Moons(str, Enum):
    LUNA = 301


class AngleFormat(str, Enum):
    HMS = "HMS"
    DEG = "DEG"


class StepSize(str, Enum):
    DAY = "day"
    MINUTE = "min"
    HOUR = "hour"


class EphemerideOptions(str, Enum):
    APPARENT_RA_AND_DEC = 1
    TRUE_ANOMALY = 41


class ResponseOptions(str, Enum):
    DATE = "Date__(UT)__HR:MN:SC.fff"
    RA_ICRF = "R.A._(ICRF)"
    RA_A_APP = "R.A._(a-app)"
    DEC_ICRF = "DEC_(ICRF)"
    DEC_A_APP = "DEC_(a-app)"
    D_RA = "dRA"
    AP_MAG = "APmag"
    S_BRT = "S-brt"
    DELTA = "delta"
    DELDOT = "deldot"
