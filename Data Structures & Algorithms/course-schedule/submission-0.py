class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = defaultdict(list)

        for a, b in prerequisites:
            pre_map[b].append(a)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if pre_map[course] == []:
                return True
            
            visited.add(course)
            for prereq in pre_map[course]:
                if not dfs(prereq):
                    return False

            visited.remove(course)
            pre_map[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True