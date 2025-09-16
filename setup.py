from setuptools import setup, find_packages, Extension
from pathlib import Path

# Compile the C extensions for the Raspberry Pi and Raspberry Pi 2+
ext_modules = [
    Extension(
        "Adafruit_DHT.Raspberry_Pi_Driver",
        sources=[
            "source/_Raspberry_Pi_2_Driver.c",
            "source/common_dht_read.c",
            "source/Raspberry_Pi_2/pi_2_dht_read.c",
            "source/Raspberry_Pi_2/pi_2_mmio.c",
        ],
        libraries=["rt"],
        extra_compile_args=["-std=gnu99"],
    ),
]

classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

# Call setuptools setup function to install package.
setup(
    name              = 'dht_pi',
    version           = '0.1.0',
    author            = 'Emir Karamehmetoglu',
    author_email      = 'ek2660@gmail.com',
    description       = 'DHT11, DHT22, and AM2302 tempreature and humidity sensor reading library for Raspberry Pi',
    long_description  = Path('README.md').read_text(),
    license           = 'MIT',
    classifiers       = classifiers,
    url               = 'https://github.com/emirmo/Adafruit_Python_DHT/',
    packages          = find_packages(),
    ext_modules       = ext_modules,
)
