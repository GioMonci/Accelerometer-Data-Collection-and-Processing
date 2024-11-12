# Accelerometer-Data-Collection-and-Processing

This collection of scripts configures the Adafruit ISM330DHCX + LIS3MDL FeatherWing to capture accelerometer data, 
logs it via serial communication into a CSV file, and visualizes the data in graphs for further analysis.

## Table of Contents
1. [What is this for?](#what-is-this-for)
2. [How to use it?](#how-to-use-it)
3. [Prerequisites](#prerequisites)
4. [Notes](#notes)
5. [Troubleshooting](#troubleshooting)
6. [Disclaimer](#disclaimer)
7. [License](#license)

## What is this for?

This project is part of a bridge monitoring system, where accelerometer data is used to assess the structural health 
of small to medium-sized bridges. By capturing and analyzing vibration data, this system aids in early detection of 
potential issues. The scripts provided here are used to collect raw data from the ISM330D sensor, save it to a CSV file, 
and plot it for analysis.

## How to use it?

1. **Compile and upload** the ISM330DHCX/Graphing files to the ESP32 to start data collection from the ISM330D.
   - Connect ESP32 or Arduino to ISM330DHCX Accelerometer
   - Get Ardunio IDE
   - Download LIS3MDL & LSM6DS and realted libraries on the IDE
   - Note: before running my code run some example code to make sure ESP32 or Ardunio connects to accelerometer
2. **Run** `SerialToCsv.py` to save the serial data into a CSV file.
   - This script should create the csv file in the same dir
   - Make sure that you close Arduino IDE or any application that monitors the serial port before running this script
   - Make sure that you have the correct ports and baud rate at what your using.
4. **Visualize** the data using `CsvToGraph.py` to generate graphs for insight into the collected data.
   - AAAAAA

## Prerequisites

- **Hardware**:
  - Adafruit ESP32 Feather Board
  - Adafruit ISM330DHCX + LIS3MDL FeatherWing
- **Software**:
  - Python 3.x
  - Required libraries:
    ```bash
    pip install csv pyserial matplotlib
    ```
  - Ardunio IDE
  - Required libraries: LIS3MDL & LSM6DS by Adafruit

## Notes

- Read the instructions thoroughly before starting data collection.
- Ensure the ESP32 and accelerometer are connected properly for data accuracy.

## Troubleshooting

- **No data in CSV**: Ensure the serial connection is configured correctly and that the ESP32 is outputting data.
- **Graphing issues**: Confirm that SerialToCsv.py has correctly formatted the data before running CsvToGraph.py.
- **Python import errors**: Verify that all required libraries are installed.

## Disclaimer

Use this program at your own risk. The author is not responsible for any potential damage to your system.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
