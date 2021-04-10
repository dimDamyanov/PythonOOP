class Room:
    def __init__(self, family_name: str, budget: float, members_count: int):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = None

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value and value < 0:
            raise ValueError('Expenses cannot be negative')
        self.__expenses = value

    def calculate_expenses(self, *args):
        self.expenses = sum([sum(el.get_monthly_expense() for el in ll) for ll in args])
