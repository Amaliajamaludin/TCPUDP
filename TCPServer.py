#echo server.py
import socket

#server port and hoss number
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 4915

#default message and password
message_of_the_day = "An apple a day keeps the doctor away."
password = "123!abc"

#socket
socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketServer.bind((SERVER_HOST, SERVER_PORT))
socketServer.listen(1)
print(f"Server listening on port {SERVER_PORT}")


while True:
    connThread, address = socketServer.accept()
    with connThread:
        print(f"Connected by {address}") # server is connected to the client
        while True:
            data = connThread.recv(1024).decode()
            if data == "MSGGET\n":
                connThread.sendall(f"200 OK\n{message_of_the_day}".encode()) #server sends the message of the day to client
            elif data == "MSGSTORE\n":
                connThread.send("200 0K\n".encode())
                new_message = connThread.recv(1024).decode() #server receives the new message
                message_of_the_day = new_message #assign new message to the message of the day
                print(f"Update message of the day: {message_of_the_day}")
            elif data == "QUIT\n": 
                connThread.sendall("200 OK\n".encode())
                connThread.close() #server ends the connection with the client
                break
            elif data == "SHUTDOWN\n":
                connThread.sendall("300 PASSWORD REQUIRED\n".encode())
                received_password = connThread.recv(1024).decode() #server receive the password from client
            
                if received_password == password:
                    connThread.sendall("200 OK\n".encode()) 
                    connThread.close() #close the connection with client
                    socketServer.close() #close the server
                    exit()
                else:
                    connThread.sendall("301 WRONG PASSWORD\n".encode()) #wrong password, remain the connection
    connThread.close()
    
        