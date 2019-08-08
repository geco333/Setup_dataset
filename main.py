import pyshark
import requests

url = 'http://www.ynet.co.il'

capture = pyshark.LiveCapture(interface='Wi-Fi')
capture.sniff(timeout=3)
request = requests.get(url)

for i in range(len(capture)):
    packet = capture.__getitem__(i)

    if 'ip' in packet:
        print(packet.ip.src)

request.close()
capture.close()

