from datetime import datetime
from typing import Any, Optional, Tuple, Union

from horizons_client.entities.enums import AngleFormat, Moons, Observers, Planets
from horizons_client.entities.exceptions import RequestException


class BaseRequestObject:
    name: str = ""
    value: Any = ""

    def __init__(self, value: Optional[Any]):
        if not self.name:
            raise NotImplementedError("Class needs a 'name' value before use")
        if value:
            self.value = value
        if not value or not self.value:
            raise RequestException("Request object requires a value.")

    def generate_request_param(self) -> Tuple[str, str]:
        return self.name.upper(), f"'{self.value}'"


class BaseTimeRequest(BaseRequestObject):

    time_format = "%Y-%b-%d %H:%M:%S.%f"
    value: datetime = None

    def __init__(self, value: datetime):
        super().__init__(value)
        if not isinstance(self.value, datetime):
            raise RequestException("Value must be of type 'datetime'")

    def generate_request_param(self) -> Tuple[str, str]:
        formatted_time = self.value.strftime(self.time_format)
        return self.name.upper(), f"'{formatted_time}'"


class StartTimeRequest(BaseTimeRequest):

    name = "start_time"


class StopTimeRequest(BaseTimeRequest):

    name = "stop_time"


class CommandRequestObject(BaseRequestObject):

    name = "command"
    value: Union[Planets, Moons] = None

    def __init__(
        self, value: Union[Planets, Moons]
    ):  # pylint: disable=useless-super-delegation
        super().__init__(value)


class CenterRequestObject(BaseRequestObject):

    name = "center"
    value: Observers = None

    def __init__(self, value: Observers):  # pylint: disable=useless-super-delegation
        super().__init__(value)


class AngleFormatRequestObject(BaseRequestObject):

    name = "ang_format"
    value: str = AngleFormat.DEG
