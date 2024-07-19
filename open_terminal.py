import os
import sys

import serial.tools.miniterm


def open_terminal(reset, port, baudrate='115200'):
    control_signal = '0' if reset else '1'
    control_signal_b = not reset
    # For using the terminal with MaixPy the 'filter' option must be set to 'direct'
    # because some control characters are emited
    print(f'cmd:\n{sys.executable} terminal {port} {baudrate}')
    sys.argv = [sys.argv[0], port, baudrate, '--dtr=' + control_signal, '--rts=' + control_signal,
                '--filter=direct', '--eol=LF']
    serial.tools.miniterm.main(default_port=port, default_baudrate=int(baudrate) or 115200, default_dtr=control_signal_b,
                               default_rts=control_signal_b)

if __name__ == '__main__':
    try:
        open_terminal(True, sys.argv[1])
    except Exception as e:
        pass