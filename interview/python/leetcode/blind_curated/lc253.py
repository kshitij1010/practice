# https://leetcode.com/problems/meeting-rooms-ii/      
        

from heapq import heapify, heappop, heappush

def minMeetingRooms(intervals):
    if intervals is None:
        return None
    
    if len(intervals) <=1:
        return len(intervals)
    
    intervals.sort(key = lambda x : (x[0], x[1]))
    
    h = [intervals[0][1]]
    heapify(h)
    
    
    for inter in intervals[1:]:
        start, end = inter
        prev_end = h[0]
        
        if start >= prev_end:
            heappop(h)
        
        heappush(h, end)

        
    return len(h)
