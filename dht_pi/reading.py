import time, enum
from . import Raspberry_Pi_Driver as driver
from typing import NamedTuple
from .sensors import SensorType


class Reading(NamedTuple):
    humidity: float | None
    temperature: float | None


class DHTResult(enum.Enum):
    DHT_SUCCESS        =  0
    DHT_ERROR_TIMEOUT  = -1
    DHT_ERROR_CHECKSUM = -2
    DHT_ERROR_ARGUMENT = -3
    DHT_ERROR_GPIO     = -4


def read(sensor: int, pin: int) -> Reading:
    """Functional implementation of Sensor.read (contains actual implementation)"""
    # Get a reading from C driver code.
    result, humidity, temp = driver.read(sensor, pin)

    # Technically unncessary
    if result not in DHTResult: 
        raise RuntimeError('Error calling DHT test driver read, UNKNOWN ERROR CODE: {0}'.format(result))

    match DHTResult(result):
        case DHTResult.DHT_SUCCESS:
            return Reading(humidity, temp)
        case DHTResult.DHT_ERROR_CHECKSUM | DHTResult.DHT_ERROR_TIMEOUT:
            # Transient Errros: Signal no result could be obtained, but the caller can retry.
            return Reading(None, None)
        case DHTResult.DHT_ERROR_GPIO:
            raise RuntimeError(
            'Error accessing GPIO. If `/dev/gpiomem` does not exist '
            'run this program as root or sudo.')
        case _:
            # Some kind of error occured.
            raise RuntimeError('Error calling DHT test driver read: {0}'.format(result))

def read_retry(sensor: SensorType, pin: int, retries: int=15, delay_seconds: float|int=2) -> Reading:
    """Functional implementation of Sensor.read_retry  (contains actual implementation)"""

    sensor_value = sensor.value
    if pin is None or int(pin) < 0 or int(pin) > 31:
        raise ValueError('Pin must be a valid GPIO number 0 to 31.')
    pin_value = int(pin)
    

    humidity, temperature = read(sensor_value, pin_value)

    while((humidity is None or temperature is None) and retries>=0):
        time.sleep(delay_seconds)
        humidity, temperature = read(sensor_value, pin_value)
        retries -= 1

    return humidity, temperature

