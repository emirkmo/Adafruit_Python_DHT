# DHT_PI 
=======================

Simplified & Modernized fork of Adafruit's Deprecated Python DHT Sensor Library, limited to
currently supported versions of Raspberry PI (Pi 2+, but create an issue if you want a Pi 1 port).
Provides a simple, safe, and typed reading of temperature and humidity
from [DHT11, DHT22, AND AM2302 sensors](https://www.adafruit.com/products/385) via GPIO pins.

For modern support by Adafruit, see their [CircuitPython libraries](https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/python-setup).

However, this simple library following modern python packaging was created because
`CircuitPython` is a convoluted Kitchen sink that is difficult to use. 
I wouldn't recommend it.

This fork is not affiliated with Adafruit in any way. All copyrights belong to them except
for heavily modified or new code.

## Installation

You can install from Pypi using your favorite package manager (such as `pip` or `uv`).
I recommend using [uv]()

```sh
uv add dht_pi
# pip install dht_pi
```

Designed for Python 3.11+. Create an issue or PR if you want support/port for earlier 3.X versions.
We don't even build for them.

## Usage

There is a safe class-based endpoint and a slightly less safe functional endpoint.

```Python
from dht_pi import Sensor, DHT11 # or DHT22, AM2302 or #SensorType and do SensorType.DHT11

GPIO_PIN = 12 # Or whichever GPIO PIN you used for the data link

sensor = Sensor(sensor_type=DHT11, pin=GPIO_PIN) 
reading = sensor.read_retry() 
# Better to use `sensor.read_retry` instead of `sensor.read`, which gives `None` readings much more readily.
print(reading.humidity, reading.temperature)

# Equivalent, but easy to mix up the order:
humidity, temperature = sensor.read_retry()
print(humidity, temperature)
```

Functional endpoint:
```Python
from dht_pi import SensorType, read_retry, read

GPIO_PIN = 12 # Or whichever GPIO PIN you used for the data link
reading = read_retry(sensor=SensorType.DHT22, pin=GPIO_PIN)

# Most dangerous:
humidity, temperature = read(sensor=SensorType.DHT22.value, pin=GPIO_PIN)
```

## Running directly on a Raspberry Pi

Ensure that your Pi can compile and download Python extensions (such as with `pip`).
Modern Raspbian ships with Python 3.11 and `pip`.
I would still recommend [uv](https://docs.astral.sh/uv/getting-started/installation/)
(Technically, you can even install `uv` via `pip`).
Then simply run:

Upcoming:
- Shell scripts.

Note: Below is from the original repo

## Original Author

Adafruit invests time and resources providing this open source code, please
support Adafruit and open-source hardware by purchasing products from Adafruit!

Written by Tony DiCola for Adafruit Industries.

MIT license, all text above must be included in any redistribution
(?: The license doesn't mention this, but I left this part in here as well as links to Adafruit)
