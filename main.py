import pyshark
import requests

url = 'http://www.ynet.co.il'

capture = pyshark.LiveCapture(interface='Wi-Fi')
capture.sniff(timeout=1)

with requests.get(url) as requests:
    for packet in capture:
        print(packet)

capture.close()

