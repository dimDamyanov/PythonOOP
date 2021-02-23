from .task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f'Task {new_task.details()} is added to the section'
        return f'Task is already in the section {self.name}'

    def complete_task(self, task_name: str):
        for i in range(len(self.tasks)):
            if self.tasks[i].name == task_name:
                self.tasks[i].completed = True
                return f'Completed task {task_name}'
        return f'Could not find task with the name {task_name}'

    def clean_section(self):
        not_completed = [task for task in self.tasks if not task.completed]
        removed_tasks_count = len(self.tasks) - len(not_completed)
        self.tasks = not_completed
        return f'Cleared {removed_tasks_count} tasks.'

    def view_section(self):
        return f'Section {self.name}:\n' + '\n'.join([task.details() for task in self.tasks])
