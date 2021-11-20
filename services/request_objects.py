from typing import Union, Any

from entities.enums import Planets, Moons, Observers


class BaseRequestObject(object):
    name: str = ""
    value: Any = ""

    def __init__(self, value):
        if not self.name:
            raise NotImplementedError("Class needs a 'name' value before use")
        self.value = value

    def generate_request_param(self) -> str:
        return f"{self.name.upper()}={self.value}"


class BaseTimeRequest(BaseRequestObject):

    def generate_request_param(self) -> str:
        formatted_time =


class CommandRequestObject(BaseRequestObject):

    name = "command"

    def __init__(self, value: Union[Planets, Moons]):
        super().__init__(value)


class CenterRequestObject(BaseRequestObject):

    name = "center"

    def __init__(self, value: Observers):
        super().__init__(value)


