# -*- coding:utf -8 -*-
import socket
def fanc1():
    print("~"*50)
    host = input("[+] " + "Host --> ")
    port = input("[+] " + "Port --> ")
    print("~"*50)

    scan = socket.socket()


    try:
        port=int(port)
        try:
            scan.connect((host, port))
        except socket.error:
            print("[!] "+ "Port -- ", port, " -- [CLOSED]")
        else:
            print("[!] " + "Port -- ", port, " -- [OPEN]")
    except:
        print("Error!")

def fanc2():

    host = input("[+] " + "Host --> ")
    print("\n")
    lists = []
    s = 0
    while s <= 1024:
        lists.append(s)
        s += 1
    # port=[1,80,443]
    file = open("result.txt", "w")
    file.write(f"Scan Result\n\nHost -->  {host}\n\n")
    file.close()
    for i in lists:
        try:
            scan = socket.socket()
            scan.settimeout(0.5)
            scan.connect((host, i))
        except socket.error:
            print("[!] " + "Port -- ", i, " -- [CLOSED]")
        else:
            print("[!] " + "Port -- ", i, " -- [OPEN]")
            file = open("result.txt", "a")
            file.write("Port -- "+ str(i) + " -- [OPEN]\n")
            file.close()
    # for ports in list:
    #     print(ports)

def fanc3():
    list = []
    ports=input("[+] " + "Port Range or Multiple Ports --> ")
    try:
        if '-' in ports:
            b = ports.split('-')
            b[0] = int(b[0])
            b[1] = int(b[1])
            b[1] = b[1] + 1
            l = range(b[0], b[1])
            for num in l:
                list.append(num)
            host = input("[+] " + "Host --> ")
            print("\n")
            file = open("result.txt", "w")
            file.write(f"Scan Result\n\nHost -->  {host}\n\n")
            file.close()
            for i in list:
                try:
                    scan = socket.socket()
                    scan.settimeout(0.5)
                    scan.connect((host, i))
                except socket.error:
                    print("[!] " + "Port -- ", i, " -- [CLOSED]")
                else:
                    print("[!] " + "Port -- ", i, " -- [OPEN]")
                    file = open("result.txt", "a")
                    file.write("Port -- " + str(i) + " -- [OPEN]\n")
                    file.close()
        elif ',' in ports:
            b = ports.split(',',1)
            for num in b:
                num = int(num)
                list.append(num)
            host = input("[+] " + "Host --> ")
            print("\n")
            file = open("result.txt", "w")
            file.write(f"Scan Result\n\nHost -->  {host}\n\n")
            file.close()
            for i in list:
                try:
                    scan = socket.socket()
                    scan.settimeout(0.5)
                    scan.connect((host, i))
                except socket.error:
                    print("[!] " + "Port -- ", i, " -- [CLOSED]")
                else:
                    print("[!] " + "Port -- ", i, " -- [OPEN]")
                    file = open("result.txt", "a")
                    file.write("Port -- " + str(i) + " -- [OPEN]\n")
                    file.close()


        else:
            print("Error!")
    except:
        print("Error!")


print("~"*50)

print("\t[1] --- Scan One Port")
print("\t[2] --- Scan 0-1024 Ports")
print("\t[3] --- Custom Range of Port or Multiple Ports")
print("~"*50, "\n")
text_a = input("[scan]--> ")

if text_a == "1":
    fanc1()
elif text_a == "2":
    fanc2()
elif text_a == "3":
    fanc3()
else:
    print("Error!")