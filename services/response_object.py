from datetime import datetime
from typing import List

import pandas as pd

class ResponseObject(object):

    def __init__(self, response_df: pd.DataFrame):
        self.date: List[datetime] = response_df.