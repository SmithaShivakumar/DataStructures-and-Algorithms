'''class ParkingSystem:
     
    def __init__(self, big, medium, small):
        self.A = [big, medium, small]

    def addCar(self, carType):
        self.A[carType - 1] -= 1
        return self.A[carType - 1] >= 0
        '''
        
class ParkingSystem:
    __slots__ = ['_parking']
	
    def __init__(self, big: int, medium: int, small: int):
        self._parking = {
            1: big, 
            2: medium, 
            3: small
        }

    def addCar(self, carType: int) -> bool:
        available_spots = self._parking[carType]
        print("available_spots", available_spots)
        if available_spots:
            self._parking[carType] = available_spots - 1
            print("parking", self._parking[carType])
            return True
        
# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)