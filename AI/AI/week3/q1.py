


def __init__(self):
    self.colors = ['Red', 'Green']
    self.roads = ['North', 'South', 'East', 'West']
    self.signal_state = {road: 'Red' for road in self.roads}
def update_signal(self, road, color):
    self.signal_state[road] = color
    
def display(self):
    for road, color in self.signal_state.items():
        print(road,color)
update_signal()
display()
    