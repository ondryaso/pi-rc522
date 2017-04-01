__version__ = "2.2.0"

try:
    from . import rfid
    from . import util
except RuntimeError:
    print("Must be used on Raspberry Pi")
