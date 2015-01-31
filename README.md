# Python RC522 lib
pi-rc522 consist of two Python classes for controlling an SPI RFID module "RC522" using Raspberry Pi. You can get this on AliExpress for $3.

Based on [MFRC522-python](https://github.com/mxgxw/MFRC522-python/blob/master/README.md).

You'll need [**SPI-Py**](https://github.com/lthiery/SPI-Py).

[MIFARE datasheet](http://www.nxp.com/documents/data_sheet/MF1S503x.pdf) can be useful.

# Connecting
Connecting RC522 module to SPI is pretty easy. You can use [this neat website](http://pi.gadgetoid.com/pinout) for reference.

| Board pin name | Board pin | Physical RPi pin | RPi pin name |
|----------------|-----------|------------------|--------------|
| SDA            | 1         | 24               | GPIO8, CE0   |
| SCK            | 2         | 23               | GPIO11, SCKL |
| MOSI           | 3         | 19               | GPIO10, MOSI |
| MISO           | 4         | 21               | GPIO9, MISO  |
| GND            | 6         | 6, 9, 20, 25     | Ground       |
| RST            | 7         | 22               | GPIO25       |
| 3.3V           | 8         | 1                | 3V3          |

You can connect SDA pin also to CE1 (GPIO7, pin #26) and call the RFID constructor with *dev='/dev/spidev0.0'*
and you can connect RST pin to any other free GPIO pin and call the constructor with *pin_rst=__BOARD numbering pin__*.

## Usage
The library is split to two classes - **RFID** and **RFIDUtil**. You can use only RFID, RFIDUtil just makes life a little bit better. 
You basically want to start with *while True* loop and "poll" the tag state. That's done using *request* method. Most of the methods
return error state, which is simple boolean - True is error, False is not error. The *request* method returns True if tag is **not**
present. If request is successful, you should call *anticoll* method. It runs anti-collision alghoritms and returns used tag UID, which
you'll use for *select_tag* method. Now you can do whatever you want. Important methods are documented. You can also look to
Read and KeyChange modules for RFIDUtil usage example.

```python
rdr = RFID.RFID()
while True:
  (error, tag_type) = rdr.request()
  if not error:
    print "Tag detected"
    (error, uid) = rdr.anticoll()
    if not error:
      print "UID: " + str(uid)
      #Auth for block 10 (block 2 of sector 2) using default shipping key A
      if rdr.card_auth(rdr.auth_a, 10, [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF], uid):
        #This will print something like (False, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        print "Reading block 10: " + str(rdr.read(10))
        #Always stop crypto1 when done working
        rdr.stop_crypto()
      
      
#Calls GPIO cleanup
rdr.cleanup()
```
