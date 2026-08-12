class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_map = defaultdict(list)
        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)

        visited, cycle = set(), set()
        res = []

        def dfs(course):
            if course in cycle:
                return False
            
            if course in visited:
                return True
            
            cycle.add(course)

            for prereq in prereq_map[course]:
                if dfs(prereq) == False:
                    return False
            
            cycle.remove(course)
            visited.add(course)
            res.append(course)
            return True
        
        for course in range(numCourses):
            if dfs(course) == False:
                return []
        
        return res


        #     0 -> 1 -> 2
        #      ^       / 
        #       \------
        
        # 0 -> 1 -> 2
        # | \       |
        # v   \     v
        # 3     - > 4

        # possible output: 4 2 1 3 0