class Elevator:
    def _init_(self):
        self.current_floor = 0
        self.destination_floors = []
        self.engaged = False
        self.door_open = False
    def move(self):
        if self.destination_floors:
            next_floor = self.destination_floors[0]
            if next_floor > self.current_floor:
                self.current_floor += 1
            elif next_floor < self.current_floor:
                self.current_floor -= 1
            else:
                self.destination_floors.pop(0)
    def add_destination(self, floor):
        if floor != self.current_floor:
            self.destination_floors.append(floor)
            self.destination_floors.sort()
    def open_door(self):
        self.door_open = True
    def close_door(self):
        self.door_open = False

class Building:
    def _init_(self):
        self.elevator_a = Elevator()
        self.elevator_b = Elevator()
    def request_elevator(self, floor):
        if not self.elevator_a.engaged:
            self.elevator_a.engaged = True
            self.elevator_a.add_destination(floor)
        else:
            self.elevator_b.add_destination(floor)
    def step(self):
        self.elevator_a.move()
        self.elevator_b.move()

if _name_ == "_main_":
    building = Building()

    while True:
        print("Elevator A is at floor:", building.elevator_a.current_floor)
        print("Elevator B is at floor:", building.elevator_b.current_floor)
        
        floor = int(input("Enter the floor you're at (0-4), or -1 to exit: "))
        if floor == -1:
            break
        if 0 <= floor <= 4:
            building.request_elevator(floor)
        
        action = input("Enter 'o' to open door, 'c' to close door, or any other key to continue: ")
        if action.lower() == 'o':
            building.elevator_a.open_door()
            building.elevator_b.open_door()
        elif action.lower() == 'c':
            building.elevator_a.close_door()
            building.elevator_b.close_door()

        building.step()