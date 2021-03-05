from project.customer import Customer
from project.trainer import Trainer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        result = []
        for i in range(len(self.subscriptions)):
            if self.subscriptions[i].id == subscription_id:
                result.append(repr(self.subscriptions[i]))
                for j in range(len(self.customers)):
                    if self.customers[j].id == self.subscriptions[i].customer_id:
                        result.append(repr(self.customers[j]))
                trainer_id = self.subscriptions[i].trainer_id
                for j in range(len(self.trainers)):
                    if self.trainers[j].id == trainer_id:
                        result.append(repr(self.trainers[j]))
                for j in range(len(self.plans)):
                    if self.plans[j].trainer_id == trainer_id:
                        result.append(repr(self.plans[j]))
                        for k in range(len(self.equipment)):
                            if self.plans[j].equipment_id == self.equipment[k].id:
                                result.append(repr(self.equipment[k]))
                                result[-1], result[-2] = result[-2], result[-1]
        return  '\n'.join(result)
