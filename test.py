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
        # print(newLines)
        return ret_msg
    def DeleteReservation(self):
        f = open('demo.txt', 'r')
        Lines = f.readlines()

        ret_msg = "Already Reserved"
        count = 0
        newLines = []
        # Strips the newline character
        for line in Lines:
            if int(line[2:]) == bookid:
                if int(line[0]) == 0:
                    print("IN")
                    entry = "1 " + line[2:]
                    newLines.append(entry)
                    ret_msg = "Reserved"
                else:
                    newLines.append(line)
            else:
                newLines.append(line)

        f.close()
        self.writeLines(newLines)
        # print(newLines)
        return ret_msg

solution = Database()
print(solution.makeReservation(bookid=101))