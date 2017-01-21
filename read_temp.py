import serial
import requests

#ser_port = '/dev/cu.usbmodem14111' # macbook ser port
ser_port = '/dev/ttyAMA1' # pi ser port
ser = serial.Serial(ser_port, 9600)

server_url = 'http://192.168.1.147:3000/temp_data'

num_reads = 0
totalC = 0
totalF = 0
while True:
    ser_data = ser.readline()
    num_reads = num_reads + 1
    values = ser_data.split('|')
    # first val is voltage
    # second is temp in C
    totalC = totalC + float(values[1])
    # third is temp in F
    totalF = totalF + float(values[2])
    if num_reads >= 60:
        avgC = totalC / num_reads
        avgF = totalF / num_reads
        body = {"avgF": int(round(avgF)), "avgC": int(round(avgC))}
        try:
            requests.post(server_url, data=body)
        except:
            print('Failed to send POST message')
        # print (body)
        num_reads = 0
        totalC = 0
        totalF = 0
