class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> dict:
        
        sort_bt = sorted(boxTypes, key = lambda x: x[1], reverse= True)
        output = 0
        
        for box, items in sort_bt:
            if truckSize> box:
                output+= (box*items)
                truckSize-=box
            else:
                output+=(truckSize*items)
                break
        
        return output
