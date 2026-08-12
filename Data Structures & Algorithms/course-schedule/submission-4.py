class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_map = defaultdict(list)
        visited = set()

        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)
        
        def dfs(course):
            if course in visited:
                return False
            
            if prereq_map[course] == []:
                return True

            visited.add(course)
            
            for prereq in prereq_map[course]:
                if not dfs(prereq):
                    return False
            
            prereq_map[course] = []
            visited.remove(course)
            return True

        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
