from dataclasses import dataclass
from .sensors import SensorType
from .reading import Reading, read, read_retry


@dataclass
class Sensor:
    sensor: SensorType
    pin: int

    def __post_init__(self):
        self._validate_sensor_pin()

    def _validate_sensor_pin(self):
        """validate sensor and pin, helping typing noobs"""
        if self.pin is None or int(self.pin) < 0 or int(self.pin) > 31:
            raise ValueError('Pin must be a valid GPIO number 0 to 31.')
        # Help typing noobs:
        self.pin = int(self.pin) 
        self.sensor = SensorType(self.sensor)

    def read(self) -> Reading:
        """Read DHT sensor of specified sensor type (DHT11, DHT22, or AM2302) on
        specified pin and return a tuple of humidity (as a floating point value
        in percent) and temperature (as a floating point value in Celsius). Note that
        because the sensor requires strict timing to read and Linux is not a real
        time OS, a result is not guaranteed to be returned!  In some cases this will
        return the tuple (None, None) which indicates the function should be retried.
        Note: the DHT sensor cannot be read faster than about once every 2 seconds.
        """
        return read(self.sensor.value, self.pin)

    def read_retry(self, retries: int=15, delay_seconds: float|int = 2) -> Reading:
        """Read DHT sensor of specified sensor type (DHT11, DHT22, or AM2302) on
        specified pin and return a tuple of humidity (as a floating point value
        in percent) and temperature (as a floating point value in Celsius).
        Unlike the read function, this read_retry function will attempt to read
        multiple times (up to the specified max retries) until a good reading can be
        found. If a good reading cannot be found after the amount of retries, a tuple
        of (None, None) is returned. The delay between retries is by default 2
        seconds, but can be overridden. 
        Note: the DHT sensor cannot be read faster than about once every 2 seconds.
        """
        if delay_seconds < 2:
            raise ValueError("DHT sensor cannot be read more than every 2 seconds!")
        read_retry(sensor=self.sensor, pin=self.pin, retries=retries, delay_seconds=delay_seconds)
