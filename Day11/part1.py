
"""
OPERATIONS

"""
def operation_0(value):
    return value * 7

def operation_1(value):
    return value + 3

def operation_2(value):
    return value + 4

def operation_3(value):
    return value + 5

def operation_4(value):
    return value * 5

def operation_5(value):
    return value * value

def operation_6(value):
    return value + 8

def operation_7(value):
    return value + 1


"""
TESTS
"""

def test_0(value):
    return value % 2 == 0

def test_1(value):
    return value % 7 == 0

def test_2(value):
    return value % 13 == 0

def test_3(value):
    return value % 19 == 0

def test_4(value):
    return value % 11 == 0

def test_5(value):
    return value % 5 == 0

def test_6(value):
    return value % 3 == 0

def test_7(value):
    return value % 17 == 0


"""
BARREL OF MONKEYS
"""

monkey_0 = None
monkey_1 = None
monkey_2 = None
monkey_3 = None
monkey_4 = None
monkey_5 = None
monkey_6 = None
monkey_7 = None

class Monkey:

    def __init__(self, items, operation, test):
        self.items = items
        self.operation = operation
        self.test = test
        self.true = None
        self.false = None
        self.inspection = 0
    
    """
    def __repr__(self):
        return f"{self.items}\n {self.true}\n {self.false}\n"
    """

monkey_0 = Monkey(
    items = [62, 92, 50, 63, 62, 93, 73, 50],
    operation = operation_0,
    test = test_0,
    )

monkey_1 = Monkey(
    items=[51, 97, 74, 84, 99],
    operation=operation_1,
    test=test_1,
    )

monkey_2 = Monkey(
    items=[98, 86, 62, 76, 51, 81, 95],
    operation=operation_2,
    test=test_2,
    )

monkey_3 = Monkey(
    items=[53, 95, 50, 85, 83, 72],
    operation=operation_3,
    test=test_3,
    )

monkey_4 = Monkey(
    items=[59, 60, 63, 71],
    operation=operation_4,
    test=test_4,
    )

monkey_5 = Monkey(
    items=[92, 65],
    operation=operation_5,
    test=test_5,
    )

monkey_6 = Monkey(
    items=[78],
    operation=operation_6,
    test=test_6,
    )

monkey_7 = Monkey(
    items=[84, 93, 54],
    operation=operation_7,
    test=test_7,
    )


monkey_0.true = monkey_7
monkey_0.false = monkey_1

monkey_1.true = monkey_2
monkey_1.false = monkey_4

monkey_2.true = monkey_5
monkey_2.false = monkey_4

monkey_3.true = monkey_6
monkey_3.false = monkey_0

monkey_4.true = monkey_5
monkey_4.false = monkey_3

monkey_5.true = monkey_6
monkey_5.false = monkey_3

monkey_6.true = monkey_0
monkey_6.false = monkey_7

monkey_7.true = monkey_2
monkey_7.false = monkey_1

"""
How a round works:

- Monkey inspects first item that they are holding (monkey_inspection += 1)
- Execute mathematical operation on that item
- Divide item value by 3, rounding down to the nearest integer
- Do the test that each monkey has
- Goto next monkey
- After each monkey has gone, the round concludes.

After 20 rounds, multiple the two highest inspections
"""

"""
PROGRAM.EXE
"""

round = 20
monkeys = [monkey_0,monkey_1,monkey_2,monkey_3,monkey_4,monkey_5,monkey_6,monkey_7]

# do this 20 times, obtain result

count = 0
while count < 20:
    for monkey in monkeys:
        if len(monkey.items) > 0:
            for index in range(len(monkey.items)):
                monkey.inspection += 1
                monkey.items[index] = monkey.operation(monkey.items[index]) # operation
                monkey.items[index] = monkey.items[index] // 3              # div by 3
                test_result = monkey.test(monkey.items[index])
                if test_result:
                    monkey.true.items.append(monkey.items[index])
                else:
                    monkey.false.items.append(monkey.items[index])
            monkey.items = [] # pop the items from the list
    count +=1


inspections=[monkey.inspection for monkey in monkeys]
max_1 = max(inspections)
inspections.pop(inspections.index(max_1))
max_2 = max(inspections)

print(max_1*max_2)


