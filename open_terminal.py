import sys

import serial.tools.miniterm


def open_terminal(reset, port):
    control_signal = '0' if reset else '1'
    control_signal_b = not reset
    # For using the terminal with MaixPy the 'filter' option must be set to 'direct'
    # because some control characters are emited
    sys.argv = [sys.argv[0], port, '115200', '--dtr=' + control_signal, '--rts=' + control_signal,
                '--filter=direct', '--eol=LF']
    # miniterm = serial.tools.miniterm.Miniterm(serial.Serial(port, 115200))
    # miniterm.exit_character = chr(0x1d)  # Ctrl+]
    # miniterm.menu_character = chr(0x14)  # Ctrl+T
    # miniterm.start()

    # import subprocess
    # subprocess.Popen([sys.executable, '-m', 'serial.tools.miniterm', port, "115200"])

    serial.tools.miniterm.main(default_port=port, default_baudrate=115200, default_dtr=control_signal_b,
                               default_rts=control_signal_b)

if __name__ == '__main__':
    print(f'sys.argv:{sys.argv}')
    open_terminal(True, sys.argv[1])