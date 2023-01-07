
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

class Solution(object):

        def canFinish(self, numCourses, prerequisites):
            def dfs(crs, hashmap, visit):
                if crs in visit:
                    return False
        
                if not len(hashmap[crs]):
                    return True

                visit.add(crs)
                for pre in hashmap[crs]:
                    if not dfs(pre, hashmap, visit): return False
                visit.remove(crs)
                hashmap[crs] =[]
                return True
            hashmap = {i:[] for i in range(numCourses)}
            for crs, pre in prerequisites:
                hashmap[crs].append(pre)

            visit = set()
            for i in range(numCourses):
                if not dfs(i, hashmap, visit): return False
            return True
