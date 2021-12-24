class APIEnum(object):

    @classmethod
    def to_list(cls):
        return [key for key in cls.__dict__.keys() if not key.startswith("_")]


class Planets(APIEnum):
    MERCURY = 199
    VENUS = 299
    EARTH = 399
    MARS = 499
    JUPITER = 599
    SATURN = 699
    URANUS = 799
    NEPTUNE = 899


class Observers(APIEnum):
    SUN = "@10"
    EARTH = f"@{Planets.EARTH}"


class Moons(APIEnum):
    LUNA = 301


class AngleFormat(APIEnum):
    HMS = "HMS"
    DEG = "DEG"


class StepSize(APIEnum):
    DAY = "day"
    MINUTE = "min"
    HOUR = "hour"


class EphemerideOptions(APIEnum):
    APPARENT_RA_AND_DEC = 1
    TRUE_ANOMALY = 41