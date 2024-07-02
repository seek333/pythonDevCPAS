'''
Created on 23 nov. 2017
@mention passer en obj
@author: sek
'''


if __name__ == '__main__':
    
    import socket

    # address du serveur
    host = "10.102.124.241"
    # port du serveur
    port = 7753
    # ouverture du socket
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connection au serveur
    s.connect((host, port))
    
    # envois d'un message code
    msg = "tmp"
    s.send(msg.encode('utf-8'))
    
    # reception des données
    data=s.recv(128)
    print(data.decode('utf-8'))
    s.close()
