#!/usr/bin/env python

import pirc522

if __name__ == '__main__':

    try:
        reader = pirc522.RFID(pin_irq = None, antenna_gain = 3)
        while True:
            uid = reader.read_id(True)
            if uid is not None:
                print(f'UID: {uid:X}')

    except KeyboardInterrupt:
        pass

    finally:
        reader.cleanup()
