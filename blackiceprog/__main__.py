import sys
import serial


def send_data(devname, filename):

    try:
        # -- Open the serial port and configure its baudrate
        with serial.Serial(devname) as port:
            port.baudrate = 115200

            # -- Open the bitstream as a binary file, read the bytes and
            # -- write them to the serial port
            with open(filename, 'rb') as bstream:
                data = bstream.read()
                port.write(data)

        # -- Report the sent bytes
        print ("Wrote {} bytes".format(len(data)))

    # -- Error managment. Something went wrong
    except IOError as e:
        errno, strerror = e.args
        print("I/O error({0}): {1}".format(errno, strerror))

    except serial.SerialException as e:
        print("Serial error({}): ".format(e.args))

    except:
        print("Unexpected error:", sys.exc_info()[0])


def main():
    if len(sys.argv) != 3:
        print ("Usage: {} serial_device bitstream_file".format(sys.argv[0]))
        sys.exit(1)

    send_data(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
