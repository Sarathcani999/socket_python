import socket, threading
class Database :
    def writeLines(self , lines):
        # L = ["1 100\n", "0 101\n", "0 102\n"]

        # writing to file
        file1 = open('demo.txt', 'w')
        file1.writelines(lines)
        file1.close()

    def makeReservation(self,bookid):
        f = open('demo.txt', 'r')
        Lines = f.readlines()

        ret_msg = "Already Reserved"
        count = 0
        newLines = []
        # Strips the newline character
        for line in Lines:
            if int(line[2:]) == bookid :
                if int(line[0]) == 0 :
                    entry="1 " + line[2:]
                    newLines.append(entry)
                    ret_msg = "Reserved"
                else :
                    newLines.append(line)
            else:
                newLines.append(line)

        f.close()
        self.writeLines(newLines)
        return ret_msg

    def deleteReservation(self,bookid):
        f = open('demo.txt', 'r')
        Lines = f.readlines()
        ret_msg = "Not Reserved"
        count = 0
        newLines = []
        # Strips the newline character
        for line in Lines:
            if int(line[2:]) == bookid:
                if int(line[0]) == 1:
                    entry = "0 " + line[2:]
                    newLines.append(entry)
                    ret_msg = "res deleted"
                else:
                    newLines.append(line)
            else:
                newLines.append(line)

        f.close()
        self.writeLines(newLines)
        # print(newLines)
        return ret_msg

class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("New connection added: ", clientAddress)

    def run(self):
        print("Connection from : ", clientAddress)
        # self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        msg = ''
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()

            if int(msg[0]) == 2:
                break
            elif int(msg[0])==3 :
                msg="Conn Established"
                pass
            elif int(msg[0]) == 0 :
                # make reservation
                db=Database()
                msg=db.makeReservation(int(msg[2:]))
            else :
                # delete Reservations
                db=Database()
                msg=db.deleteReservation(int(msg[2:]))
            self.csocket.send(bytes(msg, 'UTF-8'))
        print("Client at ", clientAddress, " disconnected...")


LOCALHOST = "127.0.0.1"
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()
