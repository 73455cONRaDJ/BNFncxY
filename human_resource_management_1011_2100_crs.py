# 代码生成时间: 2025-10-11 21:00:04
import numpy as np


class HumanResourceManager:
    """
    人力资源管理类，用于处理员工数据和相关操作。
    """

    def __init__(self):
        # 初始化员工列表，每个员工是一个字典
# 扩展功能模块
        self.employees = []

    def add_employee(self, employee_id, name, department, salary):
        """
        添加新员工
# 增强安全性
        :param employee_id: 员工ID
        :param name: 员工姓名
        :param department: 员工部门
        :param salary: 员工薪水
        """
# 添加错误处理
        if not isinstance(employee_id, int) or not isinstance(salary, (int, float)):
# 增强安全性
            raise ValueError("员工ID和薪水必须是数字类型")
        self.employees.append({
# 优化算法效率
            'id': employee_id,
            'name': name,
            'department': department,
            'salary': salary
        })

    def remove_employee(self, employee_id):
        """
        移除员工
# 添加错误处理
        :param employee_id: 要移除的员工ID
        """
        self.employees = [emp for emp in self.employees if emp['id'] != employee_id]

    def update_employee_salary(self, employee_id, new_salary):
# 扩展功能模块
        """
        更新员工薪水
        :param employee_id: 员工ID
# 优化算法效率
        :param new_salary: 新的薪水
# TODO: 优化性能
        """
        for emp in self.employees:
            if emp['id'] == employee_id:
                emp['salary'] = new_salary
                return
        raise ValueError("未找到ID为{}的员工".format(employee_id))

    def get_employee_info(self, employee_id):
        """
        获取员工信息
        :param employee_id: 员工ID
        :return: 员工信息字典
        """
        for emp in self.employees:
            if emp['id'] == employee_id:
                return emp
# 优化算法效率
        raise ValueError("未找到ID为{}的员工".format(employee_id))

    def get_department_salaries(self, department):
        """
        获取某个部门的员工薪水列表
# NOTE: 重要实现细节
        :param department: 部门名称
# NOTE: 重要实现细节
        :return: 薪水列表
        """
        department_salaries = [emp['salary'] for emp in self.employees if emp['department'] == department]
        return department_salaries

    def average_salary(self, department=None):
# 改进用户体验
        """
        计算平均薪水，可以是整个公司或特定部门的平均薪水
        :param department: 部门名称，如果为None，则计算全公司的平均薪水
        :return: 平均薪水
        """
        if department:
            salaries = self.get_department_salaries(department)
        else:
            salaries = [emp['salary'] for emp in self.employees]
        if not salaries:
            return 0
        return np.mean(salaries)

    def sort_employees_by_salary(self):
        """
        按薪水排序员工列表
        """
        self.employees.sort(key=lambda emp: emp['salary'])

# 示例用法
if __name__ == '__main__':
    hrm = HumanResourceManager()
    hrm.add_employee(1, 'John Doe', 'Marketing', 5000)
    hrm.add_employee(2, 'Jane Smith', 'IT', 6000)
    hrm.add_employee(3, 'Alice Johnson', 'Marketing', 5500)
    
    try:
        hrm.update_employee_salary(2, 6500)
    except ValueError as e:
        print(e)
    
    try:
        print(hrm.get_employee_info(2))
    except ValueError as e:
        print(e)
    
    department_salaries = hrm.get_department_salaries('IT')
    print('IT department salaries:', department_salaries)
    
    print('Average salary:', hrm.average_salary())
    print('Average salary in Marketing:', hrm.average_salary('Marketing'))
    
    hrm.sort_employees_by_salary()
    print('Employees sorted by salary:', hrm.employees)