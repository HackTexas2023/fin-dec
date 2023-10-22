import matplotlib.pyplot as plt


def federal_tax_amount(total_income: float, filing: int) -> float:
    """
    The federal_tax_amount function takes in a total income and filing status,
    and returns the amount of federal taxes owed.


    :param total_income: float: Calculate the total income of a person
    :param filing: int: Determine the number of dependents
    :return: The total amount of taxes that you will owe for the year
    """
    baseline_taxes = [0.0, 1100.0, 4046.88, 11142.78, 20813.76, 15727.68, 121405.9]
    break_point = [
        0.0,
        11000.0,
        44725.0,
        95375.0,
        182100.0,
        231250.0,
        578125.0,
        float("inf"),
    ]
    rates = [0.0, 0.10, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37]

    for i, val in enumerate(break_point):
        if total_income < val:
            remaining_income = total_income - break_point[i - 1]
            total_taxed = (
                sum(baseline_taxes[0:i])
                + (remaining_income * rates[i])
                + (total_income * 0.0765)
            )
            return total_taxed

    return 0.0


def roth_ira(
    contribution_size: float,
    current_age: int,
    retirement_age: int,
    retirement_spending: float,
) -> [float]:
    """
    The roth_ira function takes in a contribution size, current age, retirement age and retirement spending.
    It then calculates the amount of money you will have at the end of each month for 30 years after your
    retirement date. It also calculates how much taxes you would pay during that time period.

    :param contribution_size: float: Determine how much money is contributed to the roth ira each month
    :param current_age: int: Determine the starting age of the individual
    :param retirement_age: int: Determine when the user will retire
    :param retirement_spending: float: Determine how much money you will be spending in retirement
    :param : Determine the amount of money that you will be contributing to your roth ira each month
    :return: A list of money amounts and a list of taxes paid
    """
    money_amount = [0]
    taxes_paid = [0]
    retirement_spending = max(retirement_spending, 4381.25)

    for i in range(current_age, retirement_age):
        for j in range(12):
            curr_money = (money_amount[-1] + contribution_size) * 1.0085
            money_amount.append(curr_money)
            taxes_paid.append(0)

    years_contributing = retirement_age - current_age

    for i in range(60 - max(retirement_age, 60)):
        for j in range(12):
            if i < years_contributing:
                monthly_taxes = max((retirement_spending - contribution_size), 0) * 0.10
                cost_of_living = (
                    max((retirement_spending - contribution_size), 0) * 1.10
                ) + contribution_size
            else:
                monthly_taxes = retirement_spending * 0.10
                cost_of_living = retirement_spending * 1.10

            curr_money = money_amount[-1] - cost_of_living
            curr_money = curr_money * 1.0085
            money_amount.append(curr_money)
            taxes_paid.append(taxes_paid[-1] + monthly_taxes)

    for i in range(30):
        for j in range(12):
            curr_money = money_amount[-1] - retirement_spending
            curr_money = curr_money * 1.0085
            money_amount.append(curr_money)
            taxes_paid.append(0)

    return money_amount, taxes_paid


def traditional_ira(
    contribution_size: float,
    current_age: int,
    retirement_age: int,
    retirement_spending: float,
) -> [float]:
    """
    The traditional_ira function takes in the following parameters:
        - contribution_size: The amount of money you contribute to your IRA each month.
        - current_age: Your age at the time of starting contributions.
        - retirement_age: The age at which you plan to retire and start withdrawing from your IRA.
        - retirement_spending: How much money you expect to spend per year during retirement (inflation adjusted).

    :param contribution_size: float: Determine how much money is contributed to the ira each month
    :param current_age: int: Set the current age of the user
    :param retirement_age: int: Determine when the user will retire
    :param retirement_spending: float: Determine how much money you will be spending each month in retirement
    :param : Determine the amount of money you will contribute to your ira account each month
    :return: A list of money amounts and a list of taxes paid
    """
    money_amount = [0]
    retirement_spending = max(retirement_spending, 4381.25)
    federal_tax = federal_tax_amount(retirement_spending * 12, 1) / 12
    taxes_paid = [0]

    for i in range(current_age, retirement_age):
        for j in range(12):
            curr_money = (money_amount[-1] + contribution_size) * 1.0085
            money_amount.append(curr_money)
            taxes_paid.append(0)

    years_contributing = retirement_age - current_age

    for i in range(60 - max(retirement_age, 60)):
        for j in range(12):
            if i < years_contributing:
                earnings = max((retirement_spending - contribution_size), 0)
                monthly_taxes = (earnings * 0.10) + federal_tax
                cost_of_living = (earnings * 1.10) + (contribution_size + federal_tax)
            else:
                monthly_taxes = (retirement_spending * 0.10) + federal_tax
                cost_of_living = (retirement_spending * 1.10) + federal_tax

            curr_money = money_amount[-1] - cost_of_living
            curr_money = curr_money * 1.0085
            money_amount.append(curr_money)
            taxes_paid.append(taxes_paid[-1] + monthly_taxes)

    for i in range(30):
        for j in range(12):
            curr_money = money_amount[-1] - (retirement_spending + federal_tax)
            curr_money = curr_money * 1.0085
            money_amount.append(curr_money)
            taxes_paid.append(taxes_paid[-1] + federal_tax)

    return money_amount, taxes_paid


# can be the same as roth_ira because employer matching and contribution limits are encoded in contribution_size
def roth_401k(
    contribution_size: float,
    current_age: int,
    retirement_age: int,
    retirement_spending: float,
) -> [float]:
    """
    The roth_401k function takes in a contribution size, current age, retirement age and retirement spending.
    It then calculates the amount of money you will have at each month for 30 years after your retirement.
    The function returns two lists: one with the amount of money you have at each month and another with how much taxes
    you paid that year.

    :param contribution_size: float: Determine how much money you are putting into your roth 401k each month
    :param current_age: int: Determine the age at which you start contributing to your roth 401k
    :param retirement_age: int: Determine when the user will retire
    :param retirement_spending: float: Determine how much money you will spend each month in retirement
    :param : Set the amount of money you want to contribute each month
    :return: A list of floats that represents the amount of money in your account at each month
    """
    money_amount = [0]
    taxes_paid = [0]
    retirement_spending = max(retirement_spending, 4381.25)

    for i in range(current_age, retirement_age):
        for j in range(12):
            curr_money = (money_amount[-1] + contribution_size) * 1.0085
            money_amount.append(curr_money)
            taxes_paid.append(0)

    years_contributing = retirement_age - current_age

    for i in range(60 - max(retirement_age, 60)):
        for j in range(12):
            if i < years_contributing:
                monthly_taxes = max((retirement_spending - contribution_size), 0) * 0.10
                cost_of_living = (
                    max((retirement_spending - contribution_size), 0) * 1.10
                ) + contribution_size
            else:
                monthly_taxes = retirement_spending * 0.10
                cost_of_living = retirement_spending * 1.10

            curr_money = money_amount[-1] - cost_of_living
            curr_money = curr_money * 1.0085
            money_amount.append(curr_money)
            taxes_paid.append(taxes_paid[-1] + monthly_taxes)

    for i in range(30):
        for j in range(12):
            curr_money = money_amount[-1] - retirement_spending
            curr_money = curr_money * 1.0085
            money_amount.append(curr_money)
            taxes_paid.append(0)

    return money_amount, taxes_paid


def traditional_401k(
    contribution_size: float,
    current_age: int,
    retirement_age: int,
    retirement_spending: float,
) -> [float]:
    """
    The traditional_401k function takes in the following parameters:
        contribution_size: The amount of money you contribute to your 401k each month.
        current_age: Your age at the time of starting this simulation.
        retirement_age: The age at which you plan on retiring and withdrawing from your 401k.
        retirement_spending: How much money you expect to spend per year during retirement (inflation adjusted).

    :param contribution_size: float: Specify the amount of money that is contributed to the 401k each month
    :param current_age: int: Determine the age at which you start contributing to your 401k
    :param retirement_age: int: Determine when the user will retire
    :param retirement_spending: float: Determine how much money you will spend per month in retirement
    :param : Calculate the federal tax amount
    :return: A list of money amounts and a list of taxes paid
    """
    money_amount = [0]
    retirement_spending = max(retirement_spending, 4381.25)
    federal_tax = federal_tax_amount(retirement_spending * 12, 1) / 12
    taxes_paid = [0]

    for i in range(current_age, retirement_age):
        for j in range(12):
            curr_money = (money_amount[-1] + contribution_size) * 1.0085
            money_amount.append(curr_money)
            taxes_paid.append(0)

    years_contributing = retirement_age - current_age

    for i in range(60 - max(retirement_age, 60)):
        for j in range(12):
            if i < years_contributing:
                earnings = max((retirement_spending - contribution_size), 0)
                monthly_taxes = (earnings * 0.10) + federal_tax
                cost_of_living = (earnings * 1.10) + (contribution_size + federal_tax)
            else:
                monthly_taxes = (retirement_spending * 0.10) + federal_tax
                cost_of_living = (retirement_spending * 1.10) + federal_tax

            curr_money = money_amount[-1] - cost_of_living
            curr_money = curr_money * 1.0085
            money_amount.append(curr_money)
            taxes_paid.append(taxes_paid[-1] + monthly_taxes)

    for i in range(12):
        for j in range(12):
            curr_money = money_amount[-1] - (retirement_spending + federal_tax)
            curr_money = curr_money * 1.0085
            money_amount.append(curr_money)
            taxes_paid.append(taxes_paid[-1] + federal_tax)

    rmd = [
        27.4,
        26.5,
        25.6,
        24.7,
        23.8,
        22.9,
        22.0,
        21.2,
        20.3,
        19.5,
        18.7,
        17.9,
        17.1,
        16.3,
        15.5,
        14.8,
        14.1,
        13.4,
        12.7,
        12.0,
        11.4,
    ]
    for i in range(18):
        for j in range(12):
            withdrawal = money_amount[-1] * (rmd[i] / 100) / 12
            federal_tax = federal_tax_amount(withdrawal * 12, 1) / 12
            curr_money = money_amount[-1] - withdrawal - federal_tax
            curr_money = curr_money * 1.0085
            money_amount.append(curr_money)
            taxes_paid.append(taxes_paid[-1] + federal_tax)

    return money_amount, taxes_paid


# account_balance, tax_balance = roth_401k(500.0, 20, 60, 4381.25)
# print(tax_balance)
# plt.title("temp")
# plt.plot([i for i in range(len(tax_balance))], tax_balance)
# plt.show()
