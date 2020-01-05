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
        import collections
        videos = collections.OrderedDict()

        #  Find all frineds at level k
        for friend in range(len(watchedVideos)):
            if dist[friend] == level:
                for video in watchedVideos[friend]:
                    if video not in videos:
                        videos[video] = 1
                    else:
                        videos[video] += 1
        print(videos)
        #  Sort out all the videos
        #  sorted_videos = {k: v for k, v in sorted(videos.items(), key=lambda item: item[1])}
        output = [k for k in videos]
        output = output[::-1]
        return output
        

def main():
    s = Solution()
    watchedVideos = [["A","B"],["C"],["B","C"],["D"]]
    friends = [[1,2],[0,3],[0,3],[1,2]]
    id = 0
    level = 2

    watchedVideos = [["xk","qvgjjsp","sbphxzm"],["rwyvxl","ov"]]
    friends = [[1],[0]]
    id = 0
    level = 1

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
                
            
        
