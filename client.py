#!/usr/bin/env python  
  
import socket;  
  
if "__main__" == __name__:  
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);  
    sock.connect(('localhost', 8001));  
    sock.send('1');  
  
    szBuf = sock.recv(1024);  
    print("recv " + szBuf);  
    sock.close();  
    print("end of connect"); 
