## Sorry I don't have Chinese input on Linux

---

### Usage
- Install opencv (Ubuntu): `sudo apt install python3-opencv`
- Connect camera
- Check for camera: `sudo lshw | less -p cam`  
should have:
```
*-usb:1
                      description: Video
                      product: Webcam C310
                      vendor: Logitech, Inc.
                      physical id: 3
                      bus info: usb@1:2.3
                      version: 0.12
                      serial: 87BD0FA0
                      capabilities: usb-2.00
                      configuration: driver=snd-usb-audio maxpower=500mA speed=4
```
- supply `python3 stream.py`
- If error, see `stream.py` line 3
- 'q' to exit
- should have `0.frames`
- supply `python3 read_chunk.py`

### Description
- 500 frames max. per buffer file
- buffer file maximun size ~470MB
