from dataclasses import dataclass


def input_as_int_tuple():
    return (int(x) for x in input().split())


@dataclass
class Hitchhiker:
    pos: int
    dest: int
    gas: int
    food: int


@dataclass
class Possibility:
    food: int
    gas: int


def main():
    POSTS_NUMBER, HITCH_NUMBERS, INITIAL_GAS = input_as_int_tuple()
    hitch = []
    for i in range(HITCH_NUMBERS):
        hitch.append(Hitchhiker(*input_as_int_tuple()))
    possibilities = {0: Possibility(INITIAL_GAS, 0)}
    for i in range(1, POSTS_NUMBER):
        possibilities[i] = Possibility(0, -1)
        for j, (pos, dest, gas, food) in enumerate(hitch):
            if dest == i + 1:
                if possibilities[pos - 1].gas == -1:
                    continue
                gas_cost = dest - pos
                gas_refill = possibilities[pos - 1].gas - gas_cost + gas
                food_refill = possibilities[pos - 1].food + food
                if gas_refill >= 0 and food_refill >= possibilities[i].food:
                    possibilities[i].gas = gas_refill
                    possibilities[i].food = food_refill
        if possibilities[i].gas == -1 and possibilities[i-1].gas > 0 or possibilities[i-1].gas > 0 and possibilities[i-1].food > possibilities[i].food:
            possibilities[i].gas = possibilities[i-1].gas - 1
            possibilities[i].food = possibilities[i - 1].food
    if possibilities[n - 1].gas < 0:
        print("Impossible")
    else:
        print(possibilities[POSTS_NUMBER-1].food)


def main():
    n, m, init_fuel = map(int, input().split())
    hikers = []
    for i in range(m):
        hikers.append(list(map(int, input().split())))
    choices = []
    for i in range(n):
        choices.append([0, 0])
    choices[0][0] = init_fuel
    for i in range(1, n):
        choices[i][0] = -1
        for j in range(m):
            if hikers[j][1] == i + 1:
                if choices[hikers[j][0] - 1][0] == -1:
                    continue
                fuel_cost = hikers[j][1] - hikers[j][0]
                new_fuel = choices[hikers[j][0] - 1][0] - fuel_cost + hikers[j][3]
                new_food = choices[hikers[j][0] - 1][1] + hikers[j][2]
                if new_fuel >= 0 and new_food >= choices[i][1]:
                    choices[i][0] = new_fuel
                    choices[i][1] = new_food
        if (choices[i][0] == -1 and choices[i - 1][0] > 0) or (
                choices[i - 1][0] > 0 and choices[i - 1][1] > choices[i][1]):
            choices[i][0] = choices[i - 1][0] - 1
            choices[i][1] = choices[i - 1][1]
    if choices[n - 1][0] < 0:
        print("Impossible")
        return
    print(choices[n - 1][1])


if __name__ == '__main__':
    main()
