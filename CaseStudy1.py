# Bhavana Sri 2600308 - Railway Reservation
class Train:
    def __init__(self, name, seats):
        self.name = name
        self.seats = seats
        self.booked = []
        self.waitlist = []
    def book_ticket(self, passenger_name):
        if len(self.booked) < self.seats:
            pnr = f"PNR{len(self.booked)+1001}"
            self.booked.append((pnr, passenger_name))
            print(f"Confirmed: {passenger_name}")
        else:
            self.waitlist.append(passenger_name)
            print(f"Waitlisted: {passenger_name}")
    def show_status(self):
        print(f"Train: {self.name}")
        print(f"Booked: {self.booked}")
        print(f"Waitlist: {self.waitlist}")

train = Train("Vijayawada Express", 3)
train.book_ticket("Bhavana Sri")
train.book_ticket("Ravi")
train.book_ticket("Anu")
train.book_ticket("Kiran")
train.show_status()
