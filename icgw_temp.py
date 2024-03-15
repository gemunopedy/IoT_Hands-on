#!/usr/bin/env python3
# Source: https://github.com/sunfounder/raphael-kit/blob/master/python/2.2.2_Thermistor.py

import datetime
import math
import random
import socket
import time

import RPi.GPIO as GPIO
import requests

import ADC0834


def init():
    ADC0834.setup()
    print("Checking connection to ICGW... ", end="")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(3)
        try:
            s.connect(("an1.icgw.ntt.com", 8080))
        except:
            is_connected = False
            print("[NG]")
            print("Warning: Data not sent to ICGW")
        else:
            is_connected = True
            print("[OK]")
    return is_connected


def loop(interval, is_connected):
    while True:
        analogVal = ADC0834.getResult()
        Vr = 5 * float(analogVal) / 255
        try:
            Rt = 10000 * Vr / (5 - Vr)
            temp = 1/(((math.log(Rt / 10000)) / 3950) + (1 / (273.15+25)))
        except:
            Cel = random.uniform(20, 25)
            is_random = True
        else:
            Cel = temp - 273.15
            is_random = False
        now = datetime.datetime.now(datetime.timezone.utc)
        print(f"time: {now}, temp: {round(Cel, 2)}\N{DEGREE SIGN}C"
              + (" (random)" if is_random else ""))
        if is_connected:
            requests.post("http://an1.icgw.ntt.com:8080", timeout=3,
                          json={"time": int(now.timestamp() * 1000000),
                                "temp": round(Cel, 2)})
        time.sleep(interval)


if __name__ == '__main__':
    is_connected = init()
    try:
        loop(2, is_connected)
    except KeyboardInterrupt:
        ADC0834.destroy()
