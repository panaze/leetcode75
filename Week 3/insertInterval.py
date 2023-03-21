#You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
#Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
#Return intervals after the insertion.

#Example 1:
#Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
#Output: [[1,5],[6,9]]
#Explanation: We insert [2,5] into the [1,3],[6,9] in between 1 and 3 and 6 and 9, merging them into [1,5],[6,9].

#Example 2:
#Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
#Output: [[1,2],[3,10],[12,16]]
#Explanation: We insert [4,8] into the [3,5],[6,7],[8,10],[12,16] in between 3 and 5, 6 and 7, 8 and 10, and 12 and 16, merging them into [3,10],[12,16].


def insert(intervals,newInterval):
        results = []
        for interval in intervals:
            #inteval does not intefere with new interval (new intevals min is greater)
            if  newInterval[0] > interval[1]:
                results.append(interval)
             # the new interval's range is before the other, so we can add the new interval and update it to the current one
            elif newInterval[1] < interval[0]:
                results.append(newInterval)
                newInterval = interval
             # the new interval is in the range of the other interval, we have an overlap, so we must choose the min for start and max for end of interval 
            elif newInterval[0] <= interval[1] or newInterval[1] >= interval[0]:
                newInterval[0] = min(newInterval[0],interval[0])
                newInterval[1] = max(newInterval[1],interval[1])
            
        results.append(newInterval)
        return results

def main():
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    print(insert(intervals,newInterval))
    
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    print(insert(intervals,newInterval))

if __name__ == "__main__":
    main()