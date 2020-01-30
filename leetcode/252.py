# Given an array of meeting time intervals consisting of start and end times
# [[s1,e1],[s2,e2],...] (si < ei),
# determine if a person could attend all meetings.
class Solution:
    def canAttendMeetings(self, intervals):
        #  sorting the intervals based on starting time
        def get_start(x):
            if x is not None:
                return x[0]
        sorted_intervals = sorted(intervals, key=get_start)
        #  go through meeting by start time, make sure the prev finished
        for i in range(1, len(intervals)):
            if sorted_intervals[i][0] < sorted_intervals[i-1][1]:
                return False
        return True
            


def main():
    s = Solution()
    inputs = [
        [[0,30],[5,10],[15,20]],
        [[7,10],[2,4]]
    ]
    for input_f in inputs:
        can = s.canAttendMeetings(input_f)
        print(can)



if __name__ == "__main__":
    main()


        
