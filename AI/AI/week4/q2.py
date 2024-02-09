import random

class Elevator:
    def __init__(self, elevator_id, total_floors):
        self.elevator_id = elevator_id
        self.total_floors = total_floors
        self.current_floor = 1
        self.direction = 1  # 1 for going up, -1 for going down
        self.destination_floors = []

    def move(self):
        if self.destination_floors:
            next_floor = self.destination_floors[0]
            if next_floor > self.current_floor:
                self.current_floor += 1
            elif next_floor < self.current_floor:
                self.current_floor -= 1
            else:
                self.destination_floors.pop(0)

class ElevatorController:
    def __init__(self, num_elevators, total_floors):
        self.elevators = [Elevator(i, total_floors) for i in range(1, num_elevators + 1)]

    def request_elevator(self, requested_floor):
        nearest_elevator = min(self.elevators, key=lambda elevator: abs(elevator.current_floor - requested_floor))
        nearest_elevator.destination_floors.append(requested_floor)

    def run(self):
        while True:
            for elevator in self.elevators:
                elevator.move()
                # You can add more logic for performance measures, energy efficiency, etc.
            # Simulate user requests (for demonstration purposes)
            requested_floor = random.randint(1, self.elevators[0].total_floors)
            self.request_elevator(requested_floor)

if __name__ == "__main__":
    num_elevators = 4
    total_floors = 20
    controller = ElevatorController(num_elevators, total_floors)
    controller.run()
    print(controller)
