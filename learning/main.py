"""
protocol or ABC
"""
from typing import Protocol
import datetime
from enum import Enum
# from abc import ABC, abstractmethod


class Device(Protocol):
    def status(self) -> bool:
        ...

    def started_at(self)  -> datetime.datetime:
        ...

    def total_consumtion(self) -> int:
        ...


class DeviceStatus(Enum):
    ON = "ON"
    OFF = "OFF"


# class Device(ABC):
#     @abstractmethod
#     def status(self) -> bool:
#         pass

#     @abstractmethod
#     def started_at(self) -> datetime.datetime:
#         pass

#     @abstractmethod
#     def total_consumtion(self) -> int:
#         pass


def check_status(device: Device) -> DeviceStatus:
    if device.status:
        return DeviceStatus.ON
    return DeviceStatus.OFF


class LAMP:
    def status(self) -> bool:
        return True

    def started_at(self) -> datetime.datetime:
        return datetime.datetime.today() - datetime.timedelta(hours=3)

    def total_consumtion(self) -> int:
        return 120


lamp = LAMP()
result = check_status(lamp)
print(result.value)


"""

"""