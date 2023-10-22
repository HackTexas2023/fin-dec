import matplotlib.pyplot as plt

def federal_tax_amount(total_income: float, filing: int) -> float:

    baseline_taxes = [0.0, 1100.0, 4046.88, 11142.78, 20813.76, 15727.68, 121405.9]
    break_point = [0.0, 11000.0,44725.0, 95375.0,182100.0, 231250.0, 578125.0, float('inf')]
    rates = [0.0, .10, .12, .22, .24,.32, .35, .37]
    
    for i, val in enumerate(break_point):
        if(total_income < val):
            remaining_income = total_income - break_point[i-1]
            total_taxed = sum(baseline_taxes[0:i]) + (remaining_income*rates[i]) + (total_income * 0.0765)
            return total_taxed/12.0            
    
    return 0.0


def roth_ira(contribution_size: float, current_age: int, retirement_age: int, retirement_spending: float)->[float]:
    money_amount = [0]
    retirement_spending = max(retirement_spending, 4381.25)

    for i in range(current_age, retirement_age):
        for j in range(12):
            curr_money = (money_amount[-1] + contribution_size) * 1.0085
            money_amount.append(curr_money)

    years_contributing = retirement_age - current_age

    for i in range(60 - max(retirement_age, 60)):
        for j in range(12):
            if i < years_contributing:
                cost_of_living = (max((retirement_spending- contribution_size), 0) * 1.10) + contribution_size
            else:
                cost_of_living = retirement_spending * 1.10 

            curr_money = money_amount[-1] - cost_of_living
            curr_money = curr_money*1.0085
            money_amount.append(curr_money)

    for i in range(30):
        for j in range(12):
            curr_money = money_amount[-1] - retirement_spending
            curr_money = curr_money* 1.0085
            money_amount.append(curr_money)

    return money_amount


account_balance = roth_ira(500, 18, 60, 4381.25)
plt.plot([i for i in range(len(account_balance))], account_balance)
plt.show()



    
    
    
    