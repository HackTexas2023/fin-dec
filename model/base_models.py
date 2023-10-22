def federal_tax_amount(total_income: float, filing: int) -> float:
    amt = 0
    baseline_taxes = [0.0, 1100.0, 4046.88, 11142.78, 20813.76, 15727.68, 121405.9]
    break_point = [0.0, 11000.0,44725.0, 95375.0,182100.0, 231250.0, 578125.0, float('inf')]
    rates = [0.0, .10, .12, .22, .24,.32, .35, .37]
    
    for i, val in enumerate(break_point):
        if(total_income < val):
            remaining_income = total_income - break_point[i-1]
            total_taxed = sum(baseline_taxes[0:i]) + (remaining_income*rates[i]) + (total_income * 0.0765)
            return total_taxed/12.0
            break
            
    
    return 0.0

def Roth_ira(contribution_size: float, years_till_retirement: int)->None:
    money_amount = [0]

    for i in range(20, years_till_retirement):
        for i in range(12):
            curr_money = (money_amount[-1] + contribution_size) * 1.0085
            money_amount.append(curr_money)

    for i in range(60 - years_till_retirement):
        for i in range(12):
            cost_of_living = (contribution_size + (max((4381.25 - contribution_size),)) * 1.10 )
            curr_money = money_amount[-1] - cost_of_living - federal_tax_amount(cost_of_living, 0)
            curr_money = curr_money*1.0085
            money_amount.append(curr_money)
    
    
print(federal_tax_amount(60000.0, 1))
