from collections import OrderedDict
from enum import IntEnum
from functools import partialmethod, lru_cache

from spherov2.commands.api_and_shell import ApiAndShell
from spherov2.commands.connection import Connection
from spherov2.commands.drive import Drive
from spherov2.commands.firmware import Firmware
from spherov2.commands.io import IO
from spherov2.commands.power import Power
from spherov2.commands.sensor import Sensor
from spherov2.commands.system_info import SystemInfo
from spherov2.controls.v2 import AnimationControl, DriveControl, LedControl, SensorControl, StatsControl, Processors
from spherov2.toy import ToyV2, Toy, ToySensor
from spherov2.toy.bolt import BOLT
from spherov2.types import ToyType


class BOLT_PLUS(BOLT):
    toy_type = ToyType('Sphero BOLT Plus', 'BP-', 'BP', .075)
