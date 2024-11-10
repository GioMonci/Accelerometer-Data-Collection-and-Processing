import serial
import csv
import time

ser = serial.Serial('COM5', 115200, timeout=1)

with open('sensor_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Time", "AccelX", "AccelY", "AccelZ"])

    start_time = time.time()
    while time.time() - start_time < 10:
        if ser.is_open:
            inputData = ser.readline().strip().decode('ascii')
            values = inputData.split(',')
            elapsed_time = time.time() - start_time
            values = [float(v) for v in values]
            writer.writerow([elapsed_time] + values)
