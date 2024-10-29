class WaterPump:
    
    def __init__(self, power = 0, brand = "", water_flow = 0, num_field = 0, str_field = ""):
        
        self.__power = power
        self.__brand = brand
        self.__water_flow = water_flow
        
        self.num_field = num_field
        self.str_field = str_field

    def setData(self, power, brand, water_flow):
        self.__power = power
        self.__brand = brand
        self.__water_flow = water_flow
        
    def getBrand(self):
        return self.__brand
        
    def getPower(self):
        return self.__power

    def getWaterFlow(self):
        return self.__water_flow

    def __str__(self):
        return f"WaterPump (Brand: {self.__brand}, Power: {self.__power} W, Water Flow: {self.__water_flow} L/h)"

    def __repr__(self):
        return f"WaterPump (brand = {self.__brand}, power = {self.__power}, water_flow = {self.__water_flow})"

    def __del__(self):
        print(f"Object {self.__brand} is destroyed")

def main():
    pump1 = WaterPump(500, "Pumper", 200, 1, "Public String 1")
    pump2 = WaterPump(300, "GymPump", 150, 2, "Public String 2")
    pump3 = WaterPump(600, "MessiPump", 250, 3, "Public String 3")
    
    print(pump1)
    print(pump2)
    print(pump3)
    
    print("---------------------------------------------------------------")
    
    print(f"First pump | Brand: {pump1.getBrand()}, Power: {pump1.getPower()} W, Water Flow: {pump1.getWaterFlow()} L/h")
    print(f"Second pump | Brand: {pump2.getBrand()}, Power: {pump2.getPower()} W, Water Flow: {pump2.getWaterFlow()} L/h")
    print(f"Third pump | Brand: {pump3.getBrand()}, Power: {pump3.getPower()} W, Water Flow: {pump3.getWaterFlow()} L/h")
    
    print("---------------------------------------------------------------")
    
    print(f'Power: {pump1.getPower()} W')
    print(f"Номер: {pump1.num_field}")
    
main()