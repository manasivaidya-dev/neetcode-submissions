class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_to_preq = {}
        visited = set()
        for i in range(0, numCourses):
            course_to_preq[i] = []
        for course, preq in prerequisites:
            course_to_preq[course].append(preq)
        
        def dfs(course):
            if course in visited:
                return False
            if course_to_preq[course] == []:
                return True
            visited.add(course)
            for preq in course_to_preq[course]:
                if dfs(preq) == False:
                    return False
            visited.remove(course)
            course_to_preq[course] = []
            return True
        for i in range(0, numCourses):
            if dfs(i) == False:
                return False
        return True
            

        