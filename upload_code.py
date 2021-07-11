import serial
from firebase import firebase
from time import sleep
from datetime import datetime
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
for port, desc, hwid in sorted(ports):
    print("{}: {} [{}]".format(port, desc, hwid))

ser = serial.Serial("COM2", 9600)
# print(ser.readline())

a = []
str1 = str(ser.readline())
a = str1.split(",")
Moisture = a[0]
Moisture = Moisture[12:]
Vibration = a[1]
Vibration = Vibration[12:-5]
# print(Vibration)

res = 1
i = 0
time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(time)

while res:
    cc = str(1234)
    print(cc)
    val = cc
    firebase1 = firebase.FirebaseApplication('https://iot-based-landslide-91085-default-rtdb.firebaseio.com/', None)

    for i in range(0, 4):
        # string1="123"
        # string1=str(ser.readline())
        # string1=string1[9:][:-6]
        data = {'date': datetime.now().strftime("%Y-%m-%d"),
                'reading': Moisture,
                'time': datetime.now().strftime("%H:%M")
                }
        result = firebase1.patch(
            'https://iot-based-landslide-91085-default-rtdb.firebaseio.com/' + '/Moisture_Data/' + str(i), data)
        print(result)

    for i in range(0, 4):
        # string2="123"
        # string1=str(ser.readline())
        # string1=string1[9:][:-6]
        data1 = {'date': datetime.now().strftime("%Y-%m-%d"),
                 'reading': Vibration,
                 'time': datetime.now().strftime("%H:%M")
                 }
        result1 = firebase1.patch(
            'https://iot-based-landslide-91085-default-rtdb.firebaseio.com/' + '/Vibration_data/' + str(i), data1)
        print(result1)
    res = 0