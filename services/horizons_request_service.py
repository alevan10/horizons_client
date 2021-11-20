import os

HORIZONS_BASE_URL = os.environ.get("HORIZONS_BASE_URL", "https://ssd.jpl.nasa.gov/api/horizons.api")


class HorizonsRequestService(object):
    base_url = f"{HORIZONS_BASE_URL}?format=json&MAKE_EPHEM='YES'&EPHEM_TYPE='OBSERVER'&ANG_FORMAT='DEG'"

