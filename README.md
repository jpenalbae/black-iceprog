# black-iceprog
Multiplatform script to upload bitstream to BlackIce FPGAs from mystorm. This was done to be used with [apio](https://github.com/FPGAwars/apio) micro-ecosystem, but it can also be used as a standalone script.

## Installation
Using pip
```
pip install -U blackiceprog
```

Manual installation
```
$ git clone https://github.com/jpenalbae/black-iceprog.git
$ cd black-iceprog/
$ python setup.py build
$ sudo python setup.py install
```

## Usage

```
$ black-iceprog
Usage: black-iceprog serial_device bitstream_file
$ black-iceprog /dev/ttyACM0 hardware.bin
Wrote 135100 bytes
```