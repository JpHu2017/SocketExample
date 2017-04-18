#!/usr/bin/env python
import socket

if "__main__" == __name__:  
  
    try:  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);  
        print("create socket succ!");  
          
        sock.bind(('localhost', 8001));  
        print("bind socket succ!");  
          
        sock.listen(5);  
        print("listen succ!");  
  
    except:  
        print("init socket err!");  
    a = {'Cheese': 0, 'Coconut': 1, 'Baguette': 0, 'Croissant': 0, 'Walnut': 0, 'PorkFloss': 0, 'Pineapple': 0}; 
    while True:  
        print("listen for client...");  
        conn, addr = sock.accept();  
        print("get client");  
        print(addr);  
              
        conn.settimeout(5);  
        szBuf = conn.recv(1024);  
        print("recv:" + szBuf);  
  
        if "0" == szBuf:  
            conn.send('exit');  
        else: 
            conn.send(repr(a));  
  
        conn.close();  
        print("end of sevice");  
