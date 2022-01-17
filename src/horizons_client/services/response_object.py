from typing import List, Dict, Any

from horizons_client.entities.enums import ResponseOptions


class ResponseObject(object):

    def __init__(self, response_dict: Dict[str, List[Any]]):
        self.date = response_dict.get(ResponseOptions.DATE)
        self.ra_icrf = response_dict.get(ResponseOptions.RA_ICRF)
        self.ra_a_app = response_dict.get(ResponseOptions.RA_A_APP)
        self.dec_icrf = response_dict.get(ResponseOptions.DEC_ICRF)
        self.dev_a_app = response_dict.get(ResponseOptions.DEC_A_APP)
        self.d_ra = response_dict.get(ResponseOptions.D_RA)
        self.ap_mag = response_dict.get(ResponseOptions.AP_MAG)
        self.s_brt = response_dict.get(ResponseOptions.S_BRT)
        self.delta = response_dict.get(ResponseOptions.DELTA)
        self.deldot = response_dict.get(ResponseOptions.DELDOT)

