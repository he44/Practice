#  Problem 1311

#  Run BFS to get friends at level k
#  Use a ordered dictionary to store the video? 
class Solution:
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        #  BFS to get shortest path from id
        dist = [-1 for x in range(len(friends))]
        visited = []
        to_explore = [id]
        dist[id] = 0
        while len(to_explore) != 0:
            cur = to_explore.pop(0)
            visited.append(cur)
            for friend in friends[cur]:
                if friend not in visited and friend not in to_explore:
                    to_explore.append(friend)
                    dist[friend] = dist[cur] + 1
        print(dist)
        #  Just do it the dumb way
        #  manually sorting them...
        videos_at_level_k = {}
        for person in range(len(watchedVideos)):
            #  check each person to see if they are level k
            if dist[person] != level:
                continue
            #  append its video
            for video in watchedVideos[person]:
                if video not in videos_at_level_k:
                    videos_at_level_k[video] = 1
                else:
                    videos_at_level_k[video] += 1

        print("Videos at level k %s"%videos_at_level_k)
        #  Now we have to sort this dictionary, first by frequency, then alphabatically
        #  this stack overflow post solved these two problems:
        #  https://stackoverflow.com/questions/44076269/sort-counter-by-frequency-then-alphabetically-in-python
        sorted_videos_at_level_k = sorted(videos_at_level_k.items(), key = lambda item: (item[1], item[0]))
        videos = [x[0] for x in sorted_videos_at_level_k]
        return videos
                


                
            
        

def main():
    s = Solution()
    watchedVideos = [["A","B"],["C"],["B","C"],["D"]]
    friends = [[1,2],[0,3],[0,3],[1,2]]
    id = 0
    level = 2
    output = s.watchedVideosByFriends(watchedVideos, friends, id, level)
    print(output)

    watchedVideos = [["xk","qvgjjsp","sbphxzm"],["rwyvxl","ov"]]
    friends = [[1],[0]]
    id = 0
    level = 1
    output = s.watchedVideosByFriends(watchedVideos, friends, id, level)
    print(output)

    watchedVideos = [
        ["bjwtssmu"],
        ["aygr","mqls"],
        ["vrtxa","zxqzeqy","nbpl","qnpl"],
        ["r","otazhu","rsf"],
        ["bvcca","ayyihidz","ljc","fiq","viu"]
    ]
    friends = [[3,2,1,4],[0,4],[4,0],[0,4],[2,3,1,0]]
    id = 3
    level = 1
    output = s.watchedVideosByFriends(watchedVideos, friends, id, level)
    print(output)


if __name__ == "__main__":
    main()
                
            
        
