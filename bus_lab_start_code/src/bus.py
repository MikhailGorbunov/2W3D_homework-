class Bus:
    def __init__(self, route_number, destination) -> None:
        self.route_number = route_number
        self.destination = destination
        self.passengers = []

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self, passenger):
        self.passengers.append(passenger)

    def drop_off(self, passenger):
        self.passengers.remove(passenger)

    def empty(self):
        self.passengers.clear()
        # for pass in self.passangers:
        #     self.drop_off(passanger)

    def pick_up_from_stop(self, bus_stop):
        for p in bus_stop.queue:
            # print(p)
            # self.pick_up(p)
            # bus_stop.remove_pass(p)
                while bus_stop.queue:
                 self.pick_up(bus_stop.queue[0])
                 bus_stop.queue.remove(bus_stop.queue[0])
    #    bus_stop.queue.remove(p)
            
