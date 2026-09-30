class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #create adj list
        course_to_preq = {}
        for i in range(numCourses):
            course_to_preq[i] = []
        for course, preq in prerequisites:
            course_to_preq[course].append(preq)
        #visited = set()
        path = set()
        #loop thru all vals
        #if adj for elem is empty -> return
        #if not add elems in it to stack - dont care abt all possible paths - only care if we can get to point of 0 courses
        def dfs(course):
            if course in path:
                return False #found cycle in path
            if course_to_preq[course] == []:
                return True #we have seen and cleared this node 
            path.add(course)
            for preq in course_to_preq[course]:
                if not dfs(preq):
                    return False
            path.remove(course)
            course_to_preq[course] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        
        


        