# Exercise 1
class Statistics:
    def __init__(self, data=[0]):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return sum(self.data)

    def mean(self):
        mean = 0
        for num in self.data:
            mean += num
        mean /= len(self.data)
        return mean

    def median(self):
        self.data.sort()
        mid = len(self.data) // 2
        median = (self.data[mid] + self.data[~mid]) / 2
        return median

    def mode(self):
        mode = max(set(self.data), key=self.data.count)
        return mode

    def range(self):
        self.data.sort()
        range = self.data[-1] - self.data[0]
        return range

    def var(self):
        mean = self.mean()
        variance = 0
        for xi in self.data:
            variance += (xi - mean)**2 / len(self.data)
        return variance

    def std(self):
        std = self.var()**(1/2)
        return std

    def freq_dist(self):
        return [(x, self.data.count(x)) for x in set(self.data)]


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24,
        32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)

print('Count:', data.count())  # 25
print('Sum: ', data.sum())  # 744
print('Min: ', data.min())  # 24
print('Max: ', data.max())  # 38
print('Range: ', data.range())  # 14
print('Mean: ', data.mean())  # 30
print('Median: ', data.median())  # 29
print('Mode: ', data.mode())  # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std())  # 4.2
print('Variance: ', data.var())  # 17.5
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]

# Exercise 2:
class PersonAccount:
    def __init__(self, firstname='Firstname', lastname='Lastname',
                incomes=set(), expenses_properties=set()):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses_properties = expenses_properties
    
    def total_income(self):
        inc = 0
        for i in self.incomes:
            inc += i[1]
        return inc

    def total_expense(self):
        exp = 0
        for e in self.expenses_properties:
            exp += e[1]
        return exp

    def account_info(self):
        return f'''{self.firstname} {self.lastname}:
        Incomes: {self.incomes}
        Expenses: {self.expenses_properties}'''

    def add_income(self, income):
        self.incomes.add(income)

    def add_expense(self, expense):
        self.expenses_properties.add(expense)

    def account_balance(self):
        return self.total_income() - self.total_expense()

inc = {("job", 2000), ("errand", 20)}
exp = {("food", 100), ("activity", 50)}
pablo = PersonAccount('Pablo', 'Olivares', inc, exp)

pablo.add_income(('', 80))
pablo.add_expense(('',50))
print(pablo.total_income())
print(pablo.total_expense())
print(pablo.account_balance())
print(pablo.account_info())