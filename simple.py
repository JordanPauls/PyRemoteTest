import datetime
import subprocess
import time

while True:
    try:
        ping = subprocess.call('ping -c 1 www.google.com')
    except:
        ping = "Error on raspberry pi side"
    print(str(datetime.datetime.now())+'\t'+str(ping))
    
    with open('/home/pi/Desktop/Connectivity.txt', 'a') as f:
        f.write(str(datetime.datetime.now()))
        f.write('\t')
        f.write(str(ping))
        f.write('\n')
    time.sleep(60)
