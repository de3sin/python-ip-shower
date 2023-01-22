# These are our libraries
import requests
import subprocess
import socket

# These are variables 
http = requests.get("https://api.ipify.org").text
host = socket.gethostname()
ipaddr = socket.gethostbyname(host)

# This is the final part
print("[*] Your system name : " + host)
print("[+] Your public Ip : " + http)
print("[+] Your private Ip : " + ipaddr)
