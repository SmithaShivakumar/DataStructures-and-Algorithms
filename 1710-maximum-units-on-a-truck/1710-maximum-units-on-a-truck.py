class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        boxTypes.sort(key=lambda a:-a[1])
        max_units = 0
        for box in boxTypes:
            if truckSize < 0 : break
            max_units += min(truckSize, box[0]) * box[1]
            print('max_units', max_units)
            truckSize -= box[0]
        print('final units', max_units)
        return max_units
        
        
'''        freq, max_units = [0]*1001, 0
        for box in boxTypes:
            freq[box[1]] += box[0]
        for units in range(1000,0,-1):
            if truckSize < 0: break
            max_units += min(truckSize, freq[units]) * units
            print('max_units', max_units)
            truckSize -= freq[units]
        print('final units', max_units)
        return max_units'''