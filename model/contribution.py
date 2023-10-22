from model import base_models
import matplotlib.pylab as plt


def contributions(
    income: float,
    account: str,
    contribution_size: float,
    current_age: int,
    retirement_age: int,
    retirement_spending: float,
):
    """
    The contributions function takes in the following parameters:
        income - The amount of money you make per year.
        account - The type of retirement account you are contributing to.  Options include: roth_ira, traditional_ira, roth_401k, and traditional 401k.
        contribution_size - How much money you are putting into your retirement account each month (in dollars).
        current age - Your current age (in years).
        retirement age - When do you plan on retiring? (in years)


    :param income: float: Calculate the taxes that are paid on the contributions to each account
    :param account: str: Determine which account type to use
    :param contribution_size: float: Determine the amount of money that is contributed to the account each month
    :param current_age: int: Determine the starting age of the model
    :param retirement_age: int: Determine when the user will retire
    :param retirement_spending: float: Calculate the amount of money you will need to withdraw from your account each month
    :param : Determine the amount of money that is contributed to the account each month
    :return: Two lists
    """
    if account == "roth_ira":
        taxes = base_models.federal_tax_amount(income, 1) / 12
        account_balance, total_taxes = base_models.roth_ira(
            contribution_size, current_age, retirement_age, retirement_spending
        )
        running_tax = [
            (taxes * (i + 1)) for i in range((retirement_age - current_age) * 12)
        ] + [0 for i in range(len(total_taxes) - (retirement_age - current_age) * 12)]
        total_taxes = [tax + running_tax[i] for i, tax in enumerate(total_taxes)]
    elif account == "traditional_ira":
        taxes = base_models.federal_tax_amount(income - contribution_size * 12, 1) / 12
        account_balance, total_taxes = base_models.traditional_ira(
            contribution_size, current_age, retirement_age, retirement_spending
        )
        running_tax = [
            (taxes * (i + 1)) for i in range((retirement_age - current_age) * 12)
        ] + [0 for i in range(len(total_taxes) - (retirement_age - current_age) * 12)]
        total_taxes = [tax + running_tax[i] for i, tax in enumerate(total_taxes)]
    elif account == "roth_401k":
        taxes = base_models.federal_tax_amount(income, 1) / 12
        account_balance, total_taxes = base_models.roth_401k(
            contribution_size, current_age, retirement_age, retirement_spending
        )
        running_tax = [
            (taxes * (i + 1)) for i in range((retirement_age - current_age) * 12)
        ] + [0 for i in range(len(total_taxes) - (retirement_age - current_age) * 12)]
        total_taxes = [tax + running_tax[i] for i, tax in enumerate(total_taxes)]
    elif account == "traditional_401k":
        taxes = base_models.federal_tax_amount(income - contribution_size * 12, 1) / 12
        account_balance, total_taxes = base_models.traditional_401k(
            contribution_size, current_age, retirement_age, retirement_spending
        )
        running_tax = [
            (taxes * (i + 1)) for i in range((retirement_age - current_age) * 12)
        ] + [0 for i in range(len(total_taxes) - (retirement_age - current_age) * 12)]
        total_taxes = [tax + running_tax[i] for i, tax in enumerate(total_taxes)]
    else:
        account_balance, total_taxes = [], []

    return account_balance, total_taxes


# age=60
# account_balance1, tax_balance1 = contributions(100000.0, "traditional_ira",400.0, 20, age, 4381.25)
# account_balance2, tax_balance2 = contributions(100000.0, "roth_ira",400.0, 20, age, 4381.25)
# account_balance3, tax_balance3 = contributions(100000.0, "roth_401k",1200.0, 20, age, 4381.25)
# account_balance4, tax_balance4 = contributions(100000.0, "traditional_401k",1200.0, 20, age, 4381.25)
# plt.title("temp")
# plt.plot([i for i in range(len(tax_balance1))], [a_i - b_i for a_i, b_i in zip(account_balance1, tax_balance1)],label = "traditional_ira 1", linestyle="-")
# plt.plot([i for i in range(len(tax_balance2))], [a_i - b_i for a_i, b_i in zip(account_balance2, tax_balance2)],label = "roth_ira", linestyle="-.")
# plt.plot([i for i in range(len(tax_balance3))], [a_i - b_i for a_i, b_i in zip(account_balance3, tax_balance3)],label = "roth_401k", linestyle="--")
# plt.plot([i for i in range(len(tax_balance4))], [a_i - b_i for a_i, b_i in zip(account_balance4, tax_balance4)],label = "traditional_401k")
# plt.legend()

# plt.show()
