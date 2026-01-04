import pulp


def optimize_production(water_limit, sugar_limit, lemon_juice_limit, puree_limit):
    model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

    lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat='Integer')
    fruit_juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat='Integer')

    model += lemonade + fruit_juice

    model += 2 * lemonade + 1 * fruit_juice <= water_limit
    model += 1 * lemonade <= sugar_limit
    model += 1 * lemonade <= lemon_juice_limit
    model += 2 * fruit_juice <= puree_limit

    model.solve()

    return int(lemonade.varValue), int(fruit_juice.varValue)


l_count, f_count = optimize_production(100, 50, 30, 40)

print(f"Лимонад: {l_count}")
print(f"Фруктовий сік: {f_count}")
print(f"Всього: {l_count + f_count}")
