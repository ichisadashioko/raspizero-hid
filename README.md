# Raspberry Pi Zero as HID keyboard device

The following instructions will turn *Raspberry Pi Zero* into a HID keyboard to perform keystroke injection.

*Note*: 

- This will only work on `Zero` or `Zero W` model only, not the `3B+`, `3B`, etc.

## How this works

I don't really understand about modifying system files in the setup part. However, it helps us to turn Raspberry Pi Zero into a keyboard when we connect the OTG port on Raspberry Pi Zero with our PC USB port.

In order to send key pressed or released commands, we only need to write HID report to `/dev/hidg0`.

HID report is a 8-byte package. Please read more about HID report format.

- The first byte contains bit flags for some key like `Right-Ctrl`, `Left-Ctrl`, `Right-Shift`, `Left-Shift`, etc. If you want to press `Ctrl+Shift`, you need to add them together (`LEFT_CTRL+LEFT_SHIFT`) and put the value in to the first byte then write the 8-byte package to `/dev/hidg0`.

- The second byte is not used.

- To release a key write a 8-byte full of zeros package to `/dev/hidg0`

- The last 4 bytes are used to put your non-control keys. Theoretically, you can press 4 non-control keys with a 8-byte HID record. However, there is no guarantee all 4 keys will be pressed or pressed sequentially so just pack one key in one HID record, send it, and send a release record (full zeros record) to make sure a key is pressed and released properly.

- "control keys" here are refered to `Ctrl`, `Shift`, and `GUI` (Start key on Windows).

- I did compose most keycode in [`./HID/CODE/__init__.py`](./HID/CODE/__init__.py)

## Instructions

- Install `git`, `pip`

```bash
sudo apt update
sudo apt install git
sudo apt install python3 python3-pip
```

- Clone this repo

```bash
git clone https://github.com/ichisadashioko/raspizero-hid
cd raspizero-hid
```

- Install `requirements.txt`

```bash
sudo pip3 install -r requirements.txt
```

- Add `dtoverlay=dwc2` to `/boot/config.txt`

```
echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
```

- Add `dwc2` and `libcomposite` to `/etc/modules`

```
echo "dwc2" | sudo tee -a /etc/modules
echo "libcomposite" | sudo tee -a /etc/modules
```

- Copy `raspizero_hid` to `/usr/bin/` and make it executable.

```
sudo cp raspizero_hid /usr/bin/
sudo chmod +x /usr/bin/raspizero_hid
```

- Open `/etc/rc.local` with `nano` or `vim` and add the line `/usr/bin/raspizero_hid` to `/etc/rc.local` before `exit 0`

Example `/etc/rc.local` content

```
#!/bin/sh -e
#
# rc.local
#
# This script is executed at the end of each multiuser runlevel.
# Make sure that the script will "exit 0" on success or any other
# value on error.
#
# In order to enable or disable this script just change the execution
# bits.
#
# By default this script does nothing.

# Print the IP address
_IP=$(hostname -I) || true
if [ "$_IP" ]; then
  printf "My IP address is %s\n" "$_IP"
fi

# for raspizero-hid
/usr/bin/raspizero_hid

exit 0
```

- Reboot the Pi

```
sudo reboot
```

## Demo

```
bash wallpaper.sh
```

When the command is too long (e.g. `argparse`), you can put it in a text file and run it by using `bash [command-text-file]`.
