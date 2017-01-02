#!/usr/bin/env python

import signal
import time

from pirc522 import RFID

run = True
rdr = RFID()
util = rdr.util()
util.debug = True

def end_read(signal,frame):
    global run
    print("\nCtrl+C captured, ending read.")
    run = False
    rdr.cleanup()

signal.signal(signal.SIGINT, end_read)

print("Starting")
while run:
    rdr.wait_for_tag()

    (error, data) = rdr.request()
    if not error:
        print("\nDetected: " + format(data, "02x"))

    (error, uid) = rdr.anticoll()
    if not error:
        print("Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))

        print("Setting tag")
        util.set_tag(uid)
        print("\nAuthorizing")
        util.auth(rdr.auth_a, [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF])
        print("\nWriting modified bytes")
        util.rewrite(4, [None, None, 0x69, 0x24, 0x40])
        util.read_out(4)
        """
        print("\nWriting zero bytes")
        util.rewrite(2, [None, None, 0, 0, 0])
        util.read_out(2)
        print("\nDeauthorizing")
        util.deauth()
        """

        util.write_trailer(1, (0x12, 0x34, 0x56, 0x78, 0x96, 0x92), (0x0F, 0x07, 0x8F), 105, (0x74, 0x00, 0x52, 0x35, 0x00, 0xFF))
        util.deauth()

        time.sleep(1)
