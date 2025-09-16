from setuptools import setup, Extension


# Compile the C extensions for the Raspberry Pi 2+ (works on Pi 2, 3, 4, etc.)
ext_modules = [
    Extension(
        "dht_pi.Raspberry_Pi_Driver",
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


setup(ext_modules=ext_modules)

