import serial
import csv
import time


def read_serial_data(port='COM5', baudrate=115200, duration=125, output_file='sensor_data.csv'):
    try:
        with serial.Serial(port, baudrate, timeout=1) as ser, open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["AccelX", "AccelY", "AccelZ"])

            start_time = time.time()

            while time.time() - start_time < duration:
                if ser.in_waiting:
                    try:
                        raw_data = ser.readline().strip().decode('ascii')
                        values = [float(v) for v in raw_data.split(',')]

                        if len(values) == 3:  # Expecting 3-axis data
                            writer.writerow(values)
                    except (ValueError, UnicodeDecodeError) as e:
                        print(f"Invalid data: {e}")
    except serial.SerialException as e:
        print(f"Failed to open serial port: {e}")

if __name__ == "__main__":
    read_serial_data()
