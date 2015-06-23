import socket
import os

host = "192.168.1.17"

socket_protocol = socket.IPPROTO_ICMP

sniffer = socket.socket(socket.AF_INET,socket.SOCK_RAW, socket_protocol)

sniffer.bind((host,0))

sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
print "ok"
print sniffer.recvfrom(65565)