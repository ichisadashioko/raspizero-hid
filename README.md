# Turn Raspberry Pi Zero into HID device

## Enabling Modules and Drivers

- Add line `dtoverlay=dwc2` to `/boot/config.txt`
- Add line `dwc2` to `/etc/modules`
- Add line `libcomposite` to `/etc/modules`

## Configuring the Gadget

### Create the config script

- Create a config file `raspizero_hid` in `/usr/bin` and make it executable.

```
sudo touch /usr/bin/raspizero_hid
sudo chmod +x /usr/bin/raspizero_hid
```

- Add `/usr/bin/raspizero_hid` to `/etc/rc.local` before `exit 0`

## Create the gadget

- Open `/usr/bin/raspizero_hid` and add

```
#!/bin/bash
cd /sys/kernel/config/usb_gadget/
mkdir -p raspizero_hid
cd raspizero_hid
echo 0x1d6b > idVendor # Linux Foundation
echo 0x0104 > idProduct # Multifunction Composite Gadget
echo 0x0100 > bcdDevice # v1.0.0
echo 0x0200 > bcdUSB # USB2
mkdir -p strings/0x409
echo "fedcba9876543210" > strings/0x409/serialnumber
echo "X Inc" > strings/0x409/manufacturer
echo "X USB Device" > strings/0x409/product
mkdir -p configs/c.1/strings/0x409
echo "Config 1: ECM network" > configs/c.1/strings/0x409/configuration
echo 250 > configs/c.1/MaxPower

# Add functions here
mkdir -p functions/hid.usb0
echo 1 > functions/hid.usb0/protocol
echo 1 > functions/hid.usb0/subclass
echo 8 > functions/hid.usb0/report_length
echo -ne \\x05\\x01\\x09\\x06\\xa1\\x01\\x05\\x07\\x19\\xe0\\x29\\xe7\\x15\\x00\\x25\\x01\\x75\\x01\\x95\\x08\\x81\\x02\\x95\\x01\\x75\\x08\\x81\\x03\\x95\\x05\\x75\\x01\\x05\\x08\\x19\\x01\\x29\\x05\\x91\\x02\\x95\\x01\\x75\\x03\\x91\\x03\\x95\\x06\\x75\\x08\\x15\\x00\\x25\\x65\\x05\\x07\\x19\\x00\\x29\\x65\\x81\\x00\\xc0 > functions/hid.usb0/report_desc
ln -s functions/hid.usb0 configs/c.1/
# End functions

ls /sys/class/udc > UDC
```

## Python Script

```python
#!/usr/bin/env python3

def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

if __name__ == '__main__':
    NULL_CHAR = chr(0)
    # press a
    write_report(NULL_CHAR*2 + chr(4) + NULL_CHAR*5) # '\x00\x00\x04\x00\x00\x00\x00\x00'

    # release keys
    write_report(NULL_CHAR*8)

    # press shift + a (A)
    write_report(chr(32) + NULL_CHAR + chr(4) + NULL_CHAR*5) # ' \x00\x04\x00\x00\x00\x00\x00'

    # b
    write_report(NULL_CHAR*2 + chr(5) + NULL_CHAR*5) # '\x00\x00\x05\x00\x00\x00\x00\x00'

```