import time

class TrafficLightAgent:
    def __init__(self):
        self.green_light_duration_ns = 30  # Duration of green light for North-South road (in seconds)
        self.green_light_duration_ew = 20  # Duration of green light for East-West road (in seconds)
        self.cycle_duration = self.green_light_duration_ns + self.green_light_duration_ew
    
    def run_traffic_light(self):
        while True:
            self.turn_on_green_ns()
            time.sleep(self.green_light_duration_ns)
            print("30 sec")
            
            self.turn_on_green_ew()
            time.sleep(self.green_light_duration_ew)
            print("30sec")
    
    def turn_on_green_ns(self):
        print("North-South Road: Green Light ON")
        print("East-West Road: Red Light ON")
    
    def turn_on_green_ew(self):
        print("North-South Road: Red Light ON")
        print("East-West Road: Green Light ON")

if __name__ == "__main__":
    agent = TrafficLightAgent()
    agent.run_traffic_light()
