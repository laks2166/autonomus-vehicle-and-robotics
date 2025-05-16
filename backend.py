import time

class AutonomousVehicle:
    def __init__(self, speed=0, direction=0):
        self.speed = speed
        self.direction = direction

    def accelerate(self, amount):
        self.speed += amount
        print(f"Accelerating to {self.speed} km/h")

    def brake(self, amount):
        self.speed -= amount
        if self.speed < 0:
            self.speed = 0
        print(f"Braking to {self.speed} km/h")

    def steer(self, direction):
        self.direction = direction
        print(f"Steering to {self.direction} degrees")

    def move(self):
        print(f"Moving at {self.speed} km/h, direction: {self.direction} degrees")


# Create an instance of the AutonomousVehicle class
vehicle = AutonomousVehicle()

# Simulate vehicle movement
print("Autonomous Vehicle Simulation")
print("------------------------------")

vehicle.accelerate(50)
vehicle.steer(30)
vehicle.move()
print()

time.sleep(1)  # Simulate time passing

vehicle.brake(20)
vehicle.steer(0)
vehicle.move()
print()

vehicle.accelerate(30)
vehicle.steer(-20)
vehicle.move()
