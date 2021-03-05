from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @classmethod
    def dvd_capacity(cls):
        return cls.DVD_CAPACITY

    @classmethod
    def customer_capacity(cls):
        return cls.CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.CUSTOMER_CAPACITY:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.DVD_CAPACITY:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        dvd_ind = None
        for i in range(len(self.dvds)):
            if self.dvds[i].id == dvd_id:
                dvd_ind = i
        for i in range(len(self.customers)):
            if self.customers[i].id == customer_id:
                if self.dvds[dvd_ind] in self.customers[i].rented_dvds:
                    return f'{self.customers[i].name} has already rented {self.dvds[dvd_ind].name}'
                elif self.dvds[dvd_ind].is_rented:
                    return f'DVD is already rented'
                elif self.customers[i].age < self.dvds[dvd_ind].age_restriction:
                    return f'{self.customers[i].name} should be at least {self.dvds[dvd_ind].age_restriction} to rent this movie'
                else:
                    self.dvds[dvd_ind].is_rented = True
                    self.customers[i].rented_dvds.append(self.dvds[dvd_ind])
                    return f'{self.customers[i].name} has successfully rented {self.dvds[dvd_ind].name}'

    def return_dvd(self, customer_id, dvd_id):
        dvd_ind = None
        for i in range(len(self.dvds)):
            if self.dvds[i].id == dvd_id:
                dvd_ind = i
        for i in range(len(self.customers)):
            if self.customers[i].id == customer_id:
                if self.dvds[dvd_ind] in self.customers[i].rented_dvds:
                    self.customers[i].rented_dvds.remove(self.dvds[dvd_ind])
                    self.dvds[dvd_ind].is_rented = False
                    return f'{self.customers[i].name} has successfully returned {self.dvds[i].name}'
                else:
                    return f'{self.customers[i].name} does not have that DVD'

    def __repr__(self):
        return '\n'.join([repr(customer) for customer in self.customers]) + '\n' + '\n'.join([repr(dvd) for dvd in self.dvds])
