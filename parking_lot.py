class Space:
    def __init__(self, name=None):
        self.name = name
        self.time_left = None
        self.driver = None
        self.debt = None
        self.next = None

class Driver:
    def __init__(self, name=None, age=None, phone=None, ID=None):
        self.name = name
        self.age = age
        self.phone = phone
        self.ID = ID


class Lot():
    def __init__(self):
        self.number = 10
        self.max_number = 10
        self.head = None

    def generate(self):
        for i in range(self.number):
            if self.head == None:
                self.head = Space("space"+str(i))
            else:
                space = Space("space"+str(i))
                space.next = self.head
                self.head = space

    def allow_parking(self, temp_driver):
        if self.number == 0:
            print "Sorry, there is no parking space available."
        else:
            time = input("Parking slot is available, please insert how much time (hours) would you like to park your car")
            debt = time*500
            answer = raw_input("Your debt is: " + str(debt) + " AMD. would you like to pay now or not?")
            if answer.lower() == "yes":
                if temp_driver.ID > debt:
                    temp_driver.ID -= debt
                    debt = 0
                    print "Payment accepted. Current balance: " + str(temp_driver.ID)
                    self.insert_car(time, temp_driver, debt)
                else:
                    print "Not enough money on ID. "
            else:
                print "Pay online during 24 hours"
                self.insert_car(time, temp_driver, debt)

    def insert_car(self, time, temp_driver=None, debt=None):
        temp = self.head
        while temp.driver != None:
            temp = temp.next
        temp.driver = temp_driver
        temp.debt = debt
        temp.time_left = time
        self.number -= 1
        print "Your parking space is: " + temp.name

    def check_time(self):
        temp = self.head
        for i in range(self.max_number):
            print temp.name + "      " + str(temp.time_left)
            temp = temp.next




def main():
    parking_lot = Lot()
    parking_lot.generate()
    x = Driver(None, None, None, 1000)
    parking_lot.allow_parking(x)
    parking_lot.check_time()
    print "End"


main()
