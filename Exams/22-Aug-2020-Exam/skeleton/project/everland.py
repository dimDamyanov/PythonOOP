from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_expenses = sum([room.expenses + room.room_cost for room in self.rooms])
        return f'Monthly consumption: {total_expenses:.2f}$.'

    def pay(self):
        results = []
        for room in self.rooms:
            total_expense = room.expenses + room.room_cost
            if room.budget >= total_expense:
                new_budget = room.budget - total_expense
                results.append(f'{room.family_name} paid {total_expense:.2f}$ and have {new_budget:.2f}$ left.')
                room.budget = new_budget
            else:
                results.append(f'{room.family_name} does not have enough budget and must leave the hotel.')
                self.rooms.remove(room)

        return '\n'.join(results)

    def status(self):
        result = [f'Total population: {sum([room.members_count for room in self.rooms])}']
        for room in self.rooms:
            room_result = f'{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n'
            if room.children:
                for ind, child in enumerate(room.children):
                    room_result += f'--- Child {ind + 1} monthly cost: {child.get_monthly_expense():.2f}$\n'
            if room.appliances:
                room_result += f'--- Appliances monthly cost: {sum([appliance.get_monthly_expense() for appliance in room.appliances]):.2f}$'
            result.append(room_result)

        return '\n'.join(result)
