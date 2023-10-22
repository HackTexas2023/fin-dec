import matplotlib.pyplot as plt

def federal_tax_amount(total_income: float, filing: int) -> float:

    baseline_taxes = [0.0, 1100.0, 4046.88, 11142.78, 20813.76, 15727.68, 121405.9]
    break_point = [0.0, 11000.0,44725.0, 95375.0,182100.0, 231250.0, 578125.0, float('inf')]
    rates = [0.0, .10, .12, .22, .24,.32, .35, .37]
    
    for i, val in enumerate(break_point):
        if(total_income < val):
            remaining_income = total_income - break_point[i-1]
            total_taxed = sum(baseline_taxes[0:i]) + (remaining_income*rates[i]) + (total_income * 0.0765)
            return total_taxed        
    
    return 0.0


def roth_ira(contribution_size: float, current_age: int, retirement_age: int, retirement_spending: float)->[float]:
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
                monthly_taxes = (max((retirement_spending- contribution_size), 0) * 0.10)
                cost_of_living = (max((retirement_spending- contribution_size), 0) * 1.10) + contribution_size
            else:
                monthly_taxes = (retirement_spending * 0.10)
                cost_of_living = retirement_spending * 1.10 

            curr_money = money_amount[-1] - cost_of_living
            curr_money = curr_money*1.0085
            money_amount.append(curr_money)
            taxes_paid.append(taxes_paid[-1] + monthly_taxes)

    for i in range(30):
        for j in range(12):
            curr_money = money_amount[-1] - retirement_spending
            curr_money = curr_money* 1.0085
            money_amount.append(curr_money)

    return money_amount, taxes_paid


def traditional_ira(contribution_size: float, current_age: int, retirement_age: int, retirement_spending: float)->[float]:
    money_amount = [0]
    retirement_spending = max(retirement_spending, 4381.25)
    federal_tax = federal_tax_amount(retirement_spending*12, 1)/12
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
            curr_money = curr_money*1.0085
            money_amount.append(curr_money)
            taxes_paid.append(taxes_paid[-1] + monthly_taxes)

    for i in range(30):
        for j in range(12):
            curr_money = money_amount[-1] - (retirement_spending  + federal_tax)
            curr_money = curr_money* 1.0085
            money_amount.append(curr_money)
            taxes_paid.append(taxes_paid[-1] + federal_tax)

    return money_amount, taxes_paid


# can be the same as roth_ira because employer matching and contribution limits are encoded in contribution_size
def roth_401k(contribution_size: float, current_age: int, retirement_age: int, retirement_spending: float)->[float]:

    money_amount = [0]
    taxes_paid = [0]
    retirement_spending = max(retirement_spending, 4381.25)

    for i in range(current_age, retirement_age):
        for j in range(12):
            curr_money = (money_amount[-1] + contribution_size) * 1.0085
            money_amount.append(curr_money)

    years_contributing = retirement_age - current_age

    for i in range(60 - max(retirement_age, 60)):
        for j in range(12):
            if i < years_contributing:
                monthly_taxes = (max((retirement_spending- contribution_size), 0) * 0.10)
                cost_of_living = (max((retirement_spending- contribution_size), 0) * 1.10) + contribution_size
            else:
                monthly_taxes = (retirement_spending * 0.10)
                cost_of_living = retirement_spending * 1.10 

            curr_money = money_amount[-1] - cost_of_living
            curr_money = curr_money*1.0085
            money_amount.append(curr_money)
            taxes_paid.append(taxes_paid[-1] + monthly_taxes)

    for i in range(30):
        for j in range(12):
            curr_money = money_amount[-1] - retirement_spending
            curr_money = curr_money* 1.0085
            money_amount.append(curr_money)

    return money_amount, taxes_paid


def traditional_401k(contribution_size: float, current_age: int, retirement_age: int, retirement_spending: float)->[float]:

    money_amount = [0]
    retirement_spending = max(retirement_spending, 4381.25)
    federal_tax = federal_tax_amount(retirement_spending*12, 1)/12
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
            curr_money = curr_money*1.0085
            money_amount.append(curr_money)
            taxes_paid.append(taxes_paid[-1] + monthly_taxes)

    for i in range(12):
        for j in range(12):
            curr_money = money_amount[-1] - (retirement_spending  + federal_tax)
            curr_money = curr_money* 1.0085
            money_amount.append(curr_money)
            taxes_paid.append(taxes_paid[-1] + federal_tax)

    rmd = [27.4, 26.5, 25.6 ,24.7, 23.8, 22.9, 22.0, 21.2, 20.3,19.5, 18.7,17.9,17.1, 16.3, 15.5,14.8,14.1, 13.4, 12.7, 12.0,  11.4]
    for i in range(18):
        for j in range(12):
            
            withdrawal = money_amount[-1]*(rmd[i]/100)/12
            federal_tax = federal_tax_amount(withdrawal*12, 1)/12
            curr_money = money_amount[-1] - withdrawal - federal_tax
            curr_money = curr_money* 1.0085
            money_amount.append(curr_money)
            taxes_paid.append(taxes_paid[-1] + federal_tax)

    return money_amount, taxes_paid


account_balance, tax_balance = traditional_401k(500, 20, 60, 4381.25)
print(account_balance[40*12])
plt.plot([i for i in range(len(tax_balance))], tax_balance)
plt.show()



    
    
    
    