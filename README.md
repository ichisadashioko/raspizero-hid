# Raspberry Pi Zero as HID keyboard device

The following instructions will turn *Raspberry Pi Zero* into a HID keyboard to perform keystroke injection.

*Note*: `Zero` model only, not the `3B+`, `3B`, `3A`, etc.

## Instructions

- Add the following line to `/boot/config.txt`

```
dtoverlay=dwc2
```

- Add the following lines to `/etc/modules/`

```
dwc2
libcomposite
```

- Create a config file `raspizero_hid` in `/usr/bin` and make it executable.

- Copy `raspizero_hid` to `/usr/bin/`

```
sudo cp raspizero_hid /usr/bin/
sudo chmod +x /usr/bin/raspizero_hid
```

- Add the line `/usr/bin/raspizero_hid` to `/etc/rc.local` before `exit 0`

- Reboot the Pi

```
sudo reboot
```