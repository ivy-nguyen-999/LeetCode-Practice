class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        
        #add to preMap
        for course, prereq in prerequisites:
            preMap[course].append(prereq)
        
        #keep track of course visited
        visit = set()
        
        def dfs(course):
            #base cases:
            if course in visit:
                return False
            if preMap[course] == []:
                return True
            
            #recursive cases
            visit.add(course)
            
            #check if all the prereq met
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False
            
            #if all the prereq met
            visit.remove(course)
            preMap[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True