class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        to_visit = {0}

        while to_visit:
            room = to_visit.pop()
            #print(room)
            visited.add(room)
            to_visit |= set(rooms[room])-visited
            #print('set(rooms[room])',set(rooms[room]))
            #print(to_visit)
                
        return len(visited) == len(rooms)