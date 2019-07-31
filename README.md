# Raspberry Pi Zero as HID keyboard device

The following instructions will turn *Raspberry Pi Zero* into a HID keyboard to perform keystroke injection.

*Note*: 

- This will only work on `Zero` or `Zero W` model only, not the `3B+`, `3B`, etc.
- `Raspberry Pi 4` may work with the `Type-C` port (not-tested).

## Instructions

- Install `git`, `pip`

```bash
sudo apt update
sudo apt install git
sudo apt install python-pip python3-pip
```

- Clone this repo

```bash
git clone https://github.com/kuroemon2509/raspizero-hid
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
