# задача
# Определите класс Task с атрибутами title и status (например, "в процессе" или "завершено") и методом display_info(), который выводит информацию о задаче.
# Создайте дочерний класс AssignedTask, который наследует от класса Task. Добавьте атрибут assignee (назначенный сотрудник) и метод assign_task(employee), который принимает объект сотрудника и назначает ему задачу.

class Task:
    def __init__(self, title, status):
        self.title = title
        self.status = status

    def display(self):
        print(f'задача: {self.title}')
        print(f'статус: {self.status}')


class AssignedTask(Task):
    def __init__(self, title, status, assignee=None):
        super().__init__(title, status)
        self.assignee = assignee

    def assigntask(self, employee):
        self.assignee = employee
        print(f'задача: {self.title}, назначено сотруднику: {self.assignee.name}')


class Employee:
    def __init__(self, name):
        self.name = name


employee1 = Employee('анатолий')
task1 = AssignedTask('придумать новый способ кладки кирпича', 'в процессе')
task1.assigntask(employee1)
task1.display()