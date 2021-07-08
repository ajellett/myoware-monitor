'''
ArduinoService.py

Arduino Service manages the serial reading from Arduino.

'''

import serial
from SimulatedSignal import SimulatedSignal

class ArduinoService:
    port = 'COM3'
    baudrate = 9600
    
    def __init__(self, port='COM3', baudrate=9600):
    
        print("Attempting to connect to serial device on port " + port)
        try:
            self.ser = serial.Serial(port=port, baudrate=baudrate, timeout=0.1)
            print("SUCCESS: Serial device is connected.")
        except serial.serialutil.SerialException:
            print("Warning: Arduino not connected. Starting simulated signal...")
            self.simulator = SimulatedSignal()
            
    def read(self):
        self.ser = serial.Serial(ArduinoService.port, ArduinoService.baudrate, timeout=0.1)

        if self.ser.readline():
            return self.ser.readline()
        else:
            self.simulator.isRunning
            return self.simulator.read()

    
    def close(self):
        self.ser.close()
