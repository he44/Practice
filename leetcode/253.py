# Given an array of meeting time intervals consisting of start and end times
# [[s1,e1],[s2,e2],...] (si < ei),
# find the minimum number of conference rooms required.

class Solution:
    def minMeetingRooms(self, intervals):
        def get_start(key):
            return key[0]
        def get_end(key):
            return key[1]
        #  sort the intervals based on start time
        intervals_ss = sorted(intervals, key = get_start)
        intervals_se = sorted(intervals, key = get_end)
        print(intervals_ss)
        print(intervals_se)
        size = len(intervals)
        #  log the number of rooms
        si = 0
        ei = 0
        available_rooms = 0
        need_rooms = 0
        while si < size and ei < size:
            #  a room needs to be added
            if intervals_ss[si][0] < intervals_se[ei][1]:
                si += 1
                if available_rooms == 0:
                    need_rooms += 1
                else:
                    available_rooms -= 1
            else:
                ei += 1
                available_rooms += 1
        return need_rooms



def main():
    s = Solution()
    inputs = [
        [[0, 30],[5, 10],[15, 20]],
        [[7,10],[2,4]]
    ]
    for input_f in inputs:
        num_rooms = s.minMeetingRooms(input_f)
        print(num_rooms)


if __name__ == "__main__":
    main()
