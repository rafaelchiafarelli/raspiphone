
import RPi.GPIO as GPIO
import serial
import time, sys
import datetime



#SERIAL_PORT = "/dev/ttyAMA0"  # Raspberry Pi 2
#SERIAL_PORT = "/dev/ttyS0"    # Raspberry Pi 3
def sendmessage():
    SERIAL_PORT = "/dev/ttyUSB0"  # usb to serial adapter
    ser = serial.Serial(SERIAL_PORT, baudrate = 9600, timeout = 2)
    print("serial write")
    ser.write("AT+CMGF=1".encode('utf-8')+ chr(13).encode('utf-8')) # set to text mode
    time.sleep(1)
    rsp = ser.read(ser.inWaiting())
    print(rsp)
    time.sleep(3)
    print("serial write")
    ser.write('AT+CMGDA="DEL ALL"'.encode('utf-8')) # delete all SMS
    time.sleep(3)
    reply = ser.read(ser.inWaiting()) # Clean buf
    print("Listening for incomming SMS...")
    print(reply)
    reply = ser.read(ser.inWaiting())
    print(reply)
    if reply != "":
        print('buff clear')
        ser.write("AT+CMGR=1\n".encode('utf-8')) 
        time.sleep(3)
        reply = ser.read(ser.inWaiting())
        print("SMS received. Content:")
        print(reply)
        if "getStatus".encode('utf-8') in reply:
            t = str(datetime.datetime.now())
            ser.write('AT+CMGS="991386776"\r'.encode('utf-8'))
            time.sleep(3)
            msg = ("Sending status at " + t + ":--" + state).encode('utf-8')
            print("Sending SMS with status info:" + msg)
            ser.write(msg + chr(26))
        time.sleep(3)
        ser.write('AT+CMGDA="DEL ALL"\r'.encode('utf-8')) # delete all
        time.sleep(3)
        ser.read(ser.inWaiting()) # Clear buf
    time.sleep(5)  

def get_encode():
    SERIAL_PORT = "/dev/ttyUSB0"  # usb to serial adapter
    ser = serial.Serial(SERIAL_PORT, baudrate = 9600, timeout = 2)
    print("serial write")
    ser.write("AT+CSCS?".encode('utf-8')+ chr(13).encode('utf-8')) # set to text mode
    time.sleep(1)
    rsp = ser.read(ser.inWaiting())
    print(rsp)    

def set_encode_GSM():
    SERIAL_PORT = "/dev/ttyUSB0"  # usb to serial adapter
    ser = serial.Serial(SERIAL_PORT, baudrate = 9600, timeout = 2)
    print("serial write")
    ser.write('AT+CSCS="GSM"'.encode('utf-8')+ chr(13).encode('utf-8')) # set to text mode
    time.sleep(1)
    rsp = ser.read(ser.inWaiting())
    print(rsp)    
    
def send_sms(phone_number, message):
    SERIAL_PORT = "/dev/ttyUSB0"  # usb to serial adapter
    ser = serial.Serial(SERIAL_PORT, baudrate = 9600, timeout = 2)
    ser.write(('AT+CMGS=\"'+phone_number+'\"\r').encode('utf-8'))
    time.sleep(3)
    msg = (message).encode('utf-8')+chr(26).encode('utf-8')
    print("uhuuu:" + msg.decode())
    ser.write(msg)
    
#telefone do otavio splice
#send_sms(phone_number = '015988038610',message = 'oi otavio!!!!.. rs')
