class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = defaultdict(list)
        for course,prereq in prerequisites:
                adjlist[course].append(prereq)
        safe = set()

        def noCycle(node: int, path: set):
            if node in safe:
                return True
            path.add(node)
            for neigh in adjlist[node]:
                if neigh in path:
                    return False
                elif not noCycle(neigh,path):
                    return False
            path.remove(node)
            safe.add(node)
            return True

        for i in range(numCourses):
            if i not in safe:
                path = set()
                if noCycle(i, path) == False:
                    return False

            
        return True
                    
        