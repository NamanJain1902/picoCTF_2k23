import base64
import os
import socket
ip = 'picoctf.org'
response = os.system("ping -c 1 " + ip)
print(response)
#saving ping details to a variable
host_info = socket.gethostbyaddr(ip)
print()
print()
print(host_info)
print()
print()
#getting IP from a domaine
host_info_to_str = str(host_info[2])
host_info = base64.b64encode(host_info_to_str.encode('ascii'))
print("Hello, this is a part of information gathering",'Host: ', host_info)
