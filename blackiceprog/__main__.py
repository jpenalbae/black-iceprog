import sys
import serial

def send_data(devname, filename):
    wrote = 0

    try:
        port = serial.Serial(devname)
        bstream = open(filename, 'r')

        while True:
            data = bstream.read(1024)
            if data == '':
                break
            wrote += port.write(data)

    except Exception as e:
        print 'Error uploading bitstream'
        print e
        sys.exit(1)

    port.close()
    bstream.close()
    print 'Wrote %d bytes' % wrote


def main():
    if len(sys.argv) != 3:
        print 'Usage: %s serial_device bitstream_file' % sys.argv[0]
        sys.exit(1)

    send_data(sys.argv[1], sys.argv[2])
