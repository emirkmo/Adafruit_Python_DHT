import enum

class SensorType(enum.Enum):
    """Sensor type constraints"""
    DHT11 = 11
    DHT22 = 22
    AM2302 = 22

# Helper defs for typing/enum noobs:
DHT11 = SensorType.DHT11
DHT22  = SensorType.DHT22
AM2302 = SensorType.AM2302
