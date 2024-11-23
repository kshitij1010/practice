# https://leetcode.com/problems/merge-intervals/


def merge_intervals(intervals):
    if intervals is None or len(intervals) <= 1:
        return intervals

    intervals.sort(key=lambda x: x[0])

    merged_intervals = [(intervals[0][0], intervals[0][1])]

    for i in range(1, len(intervals)):
        prev_start = merged_intervals[-1][0]
        prev_end = merged_intervals[-1][1]
        
        curr_start = intervals[i][0]
        curr_end = intervals[i][1]
        
        if curr_start <= prev_end:
            merged_intervals[-1] = (min(prev_start, curr_start), max(prev_end, curr_end))
            
        else:
            merged_intervals.append((curr_start, curr_end))
            
            
    return merged_intervals
