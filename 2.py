import time

class TrafficLight:
    def __init__(self):
        self.__color = "red"

    def running(self):
        while True:
            if self.__color == "red":
                print("Red light. Duration: 7 seconds.")
                time.sleep(7)
                self.__color = "yellow"
            elif self.__color == "yellow":
                print("Yellow light. Duration: 2 seconds.")
                time.sleep(2)
                self.__color = "green"
            elif self.__color == "green":
                print("Green light. Duration: 5 seconds.")
                time.sleep(5)
                self.__color = "red"

# Пример использования:
traffic_light = TrafficLight()
traffic_light.running()
