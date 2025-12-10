import socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Socket successfully created.")
    
    #sender.py me ip address humesha receiver ka hi aayega
    ip_add =  "192.168.8.110"
    port = 999
    complete_add = (ip_add, port)
    s.bind(complete_add)
    while True:
        message, sender_address = s.recvfrom(1024)  ## 1024 specifies limits of the messsage, 1024 is in general in bytes
        
        print("Raw message", message)
        print("Sender's address", sender_address)
        
        decoded_msg = message.decode("ascii")
        print("Message", decoded_msg)
        
except Exception as e:
    print("An error occured : ", e)