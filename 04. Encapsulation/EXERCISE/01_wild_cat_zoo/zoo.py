class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.__budget = budget
        self.name = name
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price:
            if self.__animal_capacity > len(self.animals):
                self.__budget -= price
                self.animals.append(animal)
                return f'{animal.name} the {animal.__class__.__name__} added to the zoo'
            else:
                return 'Not enough space for animal'
        else:
            return 'Not enough budget'

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f'{worker.name} the {worker.__class__.__name__} hired successfully'
        else:
            return 'Not enough space for worker'

    def fire_worker(self, worker_name):
        for i in range(len(self.workers)):
            if self.workers[i].name == worker_name:
                self.workers.remove(self.workers[i])
                return f'{worker_name} fired successfully'
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        salaries = sum([worker.salary for worker in self.workers])
        if self.__budget >= salaries:
            self.__budget -= salaries
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        else:
            return 'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        tends = sum([animal.get_needs() for animal in self.animals])
        if self.__budget >= tends:
            self.__budget -= tends
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'
        else:
            return 'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        return f'You have {len(self.animals)} animals' + f'\n----- {len([animal for animal in self.animals if animal.__class__.__name__ == "Lion"])} Lions:\n' + '\n'.join(
            [repr(animal) for animal in self.animals if
             animal.__class__.__name__ == "Lion"]) + f'\n----- {len([animal for animal in self.animals if animal.__class__.__name__ == "Tiger"])} Tigers:\n' + '\n'.join(
            [repr(animal) for animal in self.animals if
             animal.__class__.__name__ == "Tiger"]) + f'\n----- {len([animal for animal in self.animals if animal.__class__.__name__ == "Cheetah"])} Cheetahs:\n' + '\n'.join(
            [repr(animal) for animal in self.animals if animal.__class__.__name__ == "Cheetah"])

    def workers_status(self):
        return f'You have {len(self.workers)} workers' + f'\n----- {len([worker for worker in self.workers if worker.__class__.__name__ == "Keeper"])} Keepers:\n' + '\n'.join(
            [repr(worker) for worker in self.workers if
             worker.__class__.__name__ == "Keeper"]) + f'\n----- {len([worker for worker in self.workers if worker.__class__.__name__ == "Caretaker"])} Caretakers:\n' + '\n'.join(
            [repr(worker) for worker in self.workers if
             worker.__class__.__name__ == "Caretaker"]) + f'\n----- {len([worker for worker in self.workers if worker.__class__.__name__ == "Vet"])} Vets:\n' + '\n'.join(
            [repr(worker) for worker in self.workers if worker.__class__.__name__ == "Vet"])
