from random import randint

class Train:

    def __init__ (slf, trainNo):
        slf.trainNo = trainNo

    def book (rakibul, fro, to):
        print(f"Train is booked, train no: {rakibul.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no {self.trainNo} is running on time")   

    def getFare(self, fro, to):
        print(f"Train no: {self.trainNo} from {fro} to {to} is {randint(222, 6565)}")

t = Train (1255)
t.book ("Rangpur", "Dhaka")
t.getStatus()
t.getFare("Rangpur", "Dhaka")