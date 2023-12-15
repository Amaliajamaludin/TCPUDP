import socket

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 4915

def main():
    socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketClient.connect((SERVER_HOST, SERVER_PORT))

    while True:
        command = input("Enter command (MSGGET, MSGSTORE, QUIT, SHUTDOWN): ").strip() #ask user and (exclude(the space front and back)

        if command == "MSGGET":
            socketClient.sendall("MSGGET\n".encode()) #send MSGGET to server
            response = socketClient.recv(1024).decode() #receive the message
            print(response) #print the message
        elif command == "MSGSTORE":
            socketClient.sendall("MSGSTORE\n".encode()) #send MSGSTORE to server
            new_message = input("Enter the new message of the day: ").strip() #user enter new message
            socketClient.sendall(new_message.encode()) #send new message to server
            response = socketClient.recv(1024).decode() #receive the message
            print(response) #print the message
        elif command == "QUIT":
            socketClient.sendall("QUIT\n".encode()) #send QUIT to server
            response = socketClient.recv(1024).decode() #receive the message
            print(response) #print the message
            socketClient.close() #close the socket
            break
        elif command == "SHUTDOWN":
            socketClient.sendall("SHUTDOWN\n".encode()) #send SHUTDOWN to server
            response = socketClient.recv(1024).decode() #receive the message
            print(response)
            if response == "300 PASSWORD REQUIRED\n": #right response
                password = input("Enter the password: ").strip() #enter the password
                socketClient.sendall(password.encode()) #send the password
                response = socketClient.recv(1024).decode() #receive the message
                print(response) #print the message
                if response == "200 OK\n": #right response
                    socketClient.close() #close the socket
                    break
                elif response == "301 WRONG PASSWORD\n": #false response
                    print("Wrong password. SHUTDOWN failed.") #print the message
            else:
                print("SHUTDOWN failed.") #Error-connection or etc, print the message
        else:
            print("Invalid command. Please enter MSGGET, MSGSTORE, QUIT, or SHUTDOWN.") #invalid command

if __name__ == "__main__":
    main() #call main
