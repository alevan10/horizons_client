from datetime import datetime
from typing import Union, Any, Tuple

from entities.enums import Planets, Moons, Observers


class BaseRequestObject(object):
    name: str = ""
    value: Any = ""

    def __init__(self, value):
        if not self.name:
            raise NotImplementedError("Class needs a 'name' value before use")
        self.value = value

    def generate_request_param(self) -> Tuple[str, str]:
        return self.name.upper(), f"'{self.value}'"


class BaseTimeRequest(BaseRequestObject):

    time_format = "%Y-%b-%d %H:%M:%S.%f"

    def __init__(self, value):
        super().__init__(value)
        if not isinstance(self.value, datetime):
            raise ValueError("Value must be of type 'datetime'")

    def generate_request_param(self) -> Tuple[str, str]:
        formatted_time = self.value.strftime(self.time_format)
        return self.name.upper(), f"'{formatted_time}'"


class StartTimeRequest(BaseTimeRequest):

    name = "start_time"


class StopTimeRequest(BaseTimeRequest):

    name = "stop_time"


class CommandRequestObject(BaseRequestObject):

    name = "command"

    def __init__(self, value: Union[Planets, Moons]):
        super().__init__(value)


class CenterRequestObject(BaseRequestObject):

    name = "center"

    def __init__(self, value: Observers):
        super().__init__(value)


