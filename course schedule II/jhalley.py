class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        requires = {}
        courses_prereq_counts = {}
        courses_no_prereqs = []
        course_order = []
        
        for i in range(numCourses):
            requires[i] = set()
            courses_prereq_counts[i] = 0
        for req in prerequisites:
            requires[req[1]].add(req[0])
            courses_prereq_counts[req[0]] += 1
        courses_no_prereqs = [i[0] for i in filter(lambda (k, v): v == 0, courses_prereq_counts.items())]
        
        while len(courses_prereq_counts) != 0:
            if not (courses_no_prereqs):
                return []
            curr_course = courses_no_prereqs.pop()
            courses_prereq_counts.pop(curr_course)
            course_order.append(curr_course)
            
            for course in requires[curr_course]:
                courses_prereq_counts[course] -= 1
                if courses_prereq_counts[course] == 0:
                    courses_no_prereqs.append(course)
            
        return course_order 
