How to run the code:
Click ‘Run’ and select ‘Start Debugging. The terminal will open and output the server listening
Split the terminal in half and type Python TCPClient.py
Follow the prompt and provide the command

1. When the user types MSGGET, the socketClient will send this as a message to the socketServer.
   The socketServer will respond to the message with 200 OK  and send message_of_the_day. The socketClient receives the response and prints it.
2. When the user types MSGSTORE, the socketClient will send this as a message to the socketServer.
   The socketServer will respond to the message with 200 OK. Prompt the user to enter the new message that like to be stored, and socketClient will send it to socketServer.
   The socketServer will retrieve the message and assign it to the message_of_the_day. Both the client and server will print the updated message.
4. When the user types QUIT, the socketClient will send this as a message to the socketServer.
   The socketServer will respond to the message with 200 OK  and close the thread. The socketClient receives the response 200 OK and prints it, and closes the socket.
   (The loop is break, but the socketServer remains listening)
6. When the user types SHUTDOWN, the socketClient will send this as a message to the socketServer.
   The socketServer will respond to the message with 300 PASSWORD REQUIRED  and retrieve the password from socketClient.
   The socketClient receives the response and needs to input the password. If the password is correct, socketServer will send 200 OK and shutdowns. (Both parties close the socket).
   If the password is wrong, socketServer will send 301 WRONG PASSWORD, and socketClient will print it. (Both socket is still open and remain in the loop). The user will be asked to input the new command.
