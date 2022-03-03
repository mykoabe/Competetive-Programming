"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee_dict = {employee.id : employee for employee in employees}
        def dfs(id):
            return employee_dict[id].importance + sum(dfs(id) for id in employee_dict[id].subordinates)
        return dfs(id)