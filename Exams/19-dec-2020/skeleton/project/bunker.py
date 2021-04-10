class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        result = [supply for supply in self.supplies if supply.__class__.__name__ == 'FoodSupply']
        if not result:
            raise IndexError('There are no food supplies left!')
        return result

    @property
    def water(self):
        result = [supply for supply in self.supplies if supply.__class__.__name__ == 'WaterSupply']
        if not result:
            raise IndexError('There are no water supplies left!')
        return result

    @property
    def painkillers(self):
        result = [medicine for medicine in self.medicine if medicine.__class__.__name__ == 'Painkiller']
        if not result:
            raise IndexError('There are no painkillers left!')
        return result

    @property
    def salves(self):
        result = [medicine for medicine in self.medicine if medicine.__class__.__name__ == 'Salve']
        if not result:
            raise IndexError('There are no salves left!')
        return result

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f'Survivor with name {survivor.name} already exists.')
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type: str):
        if survivor.needs_healing:
            medicine = None
            if medicine_type == "Painkiller":
                medicine = self.painkillers[-1]
                medicine.apply(survivor)
            elif medicine_type == "Salve":
                medicine = self.salves[-1]
                medicine.apply(survivor)
            self.medicine.remove(medicine)
            return f'{survivor.name} healed successfully with {medicine_type}'

    def sustain(self, survivor, sustenance_type: str):
        if survivor.needs_sustenance:
            supply = None
            if sustenance_type == 'FoodSupply':
                supply = self.food[-1]
                supply.apply(survivor)
            elif sustenance_type == 'WaterSupply':
                supply = self.water[-1]
                supply.apply(survivor)
            self.supplies.remove(supply)
            return f'{survivor.name} sustained successfully with {sustenance_type}'

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2
            self.sustain(survivor, 'FoodSupply')
            self.sustain(survivor, 'WaterSupply')
