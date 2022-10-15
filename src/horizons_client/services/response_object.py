import logging
from typing import Any, Dict

from dateutil.parser import ParserError, parse

from horizons_client.entities.enums import ResponseOptions

logger = logging.getLogger(__name__)

DATETIME_PARSE_MESSAGE = "Deserialization of date value {} failed"


class ResponseObject:
    def __init__(self, response_dict: Dict[str, Any]):
        try:
            logger.debug("Response dictionary", response_dict)
            self.date = parse(response_dict.get(ResponseOptions.DATE))
        except (ParserError, ValueError, TypeError):
            logger.error(
                DATETIME_PARSE_MESSAGE.format(response_dict.get(ResponseOptions.DATE)),
                extra=response_dict,
            )
            raise
        self.ra_icrf = response_dict.get(ResponseOptions.RA_ICRF)
        self.ra_a_app = response_dict.get(ResponseOptions.RA_A_APP)
        self.dec_icrf = response_dict.get(ResponseOptions.DEC_ICRF)
        self.dec_a_app = response_dict.get(ResponseOptions.DEC_A_APP)
        self.d_ra = response_dict.get(ResponseOptions.D_RA)
        self.ap_mag = response_dict.get(ResponseOptions.AP_MAG)
        self.s_brt = response_dict.get(ResponseOptions.S_BRT)
        self.delta = response_dict.get(ResponseOptions.DELTA)
        self.deldot = response_dict.get(ResponseOptions.DELDOT)
