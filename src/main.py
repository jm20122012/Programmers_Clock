from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from datetime import datetime

# Custom Imports
from UI_Main import Ui_MainWindow
from Clock import Clock

# Global variable
ui = None
timer = None

def update_hex_clock():
    global ui
    hour_to_hex = hex(datetime.now().hour)
    minute_to_hex = hex(datetime.now().minute)

    print(f"Hour Dec: {datetime.now().hour} - Hour Hex: {hour_to_hex}")
    print(f"Minute Dec: {datetime.now().minute} - Minute Hex: {minute_to_hex}")

    ui.hex_clock_hours_label.setText(hour_to_hex)
    ui.hex_clock_minutes_label.setText(minute_to_hex)

def update_binary_clock():
    global ui
    hour_to_bin = bin(datetime.now().hour)
    minute_to_bin = bin(datetime.now().minute)

    print(f"Hour Dec: {datetime.now().hour} - Hour Hex: {hour_to_bin}")
    print(f"Minute Dec: {datetime.now().minute} - Minute Hex: {minute_to_bin}")

    ui.binary_clock_hours_label.setText(hour_to_bin)
    ui.binary_clock_minutes_label.setText(minute_to_bin)

def initialize():
    global timer
    vhbox_layout = QtWidgets.QVBoxLayout(ui.analog_clock_frame_contents)
    
    clock = Clock(ui.analog_clock_frame_contents)

    vhbox_layout.addWidget(clock)

    timer = QtCore.QTimer()
    timer.timeout.connect(clock.update_time)
    timer.timeout.connect(update_hex_clock)
    timer.timeout.connect(update_binary_clock)
    timer.start(1000)


def main():
    global ui
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    
    initialize()

    main_window.show()

    app.exec()

    timer.stop()

if __name__ == "__main__":
    main()