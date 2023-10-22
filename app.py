from flask import Flask
from flask import render_template, json
import matplotlib.pylab as plt
from model import contribution

app = Flask(__name__)


@app.route("/")
def chart(
    # income: float,
    # contribution_size: float,
    # current_age: int,
    # retirement_age: int,
    # retirement_spending: float,
):
    legend = "Monthly Data"
    # labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    # values = [10, 9, 8, 7, 6, 4, 7, 8]

    accounts = ["roth_ira", 
                "traditional_ira", 
                "roth_401k",
                "traditional_401k"
                ]
    acount_balances = []
    for account in accounts:
        account_balance, tax_balance = contribution.contributions(
            income=100000.0,
            account=account,
            contribution_size=400.0,
            current_age=20,
            retirement_age=60,
            retirement_spending=4381.25,
        )
        print(account_balance)
        acount_balances.append(account_balance[-1])
        
    max_account_balance = max(acount_balances)
    max_account_balance_index = acount_balances.index(max_account_balance)
    
    account_balances, tax_balance = contribution.contributions(
        income=100000.0,
        account=accounts[max_account_balance_index],
        contribution_size=400.0,
        current_age=20,
        retirement_age=60,
        retirement_spending=4381.25,
    )
    
    values = account_balances
    labels = [i for i in range(len(account_balances))]
    return render_template("index.html", values=values, labels=labels, legend=legend)

@app.route("/")
def chart1(
    # income: float,
    # contribution_size: float,
    # current_age: int,
    # retirement_age: int,
    # retirement_spending: float,
):
    legend = "Data"
    # labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    # values = [10, 9, 8, 7, 6, 4, 7, 8]

    accounts = ["roth_ira", 
                "traditional_ira", 
                "roth_401k",
                "traditional_401k"
                ]
    acount_balances = []
    for account in accounts:
        account_balance, tax_balance = contribution.contributions(
            income=103000.0,
            account=account,
            contribution_size=4030.0,
            current_age=22,
            retirement_age=90,
            retirement_spending=43321.25,
        )
        print(account_balance)
        acount_balances.append(account_balance[-1])
        
    max_account_balance = max(acount_balances)
    max_account_balance_index = acount_balances.index(max_account_balance)
    
    account_balances, tax_balance = contribution.contributions(
        income=50000.0,
        account=accounts[max_account_balance_index],
        contribution_size=4030.0,
        current_age=19,
        retirement_age=60,
        retirement_spending=4381.25,
    )
    
    values = account_balances
    labels = [i for i in range(len(account_balances))]
    return render_template("index.html", values=values, labels=labels, legend=legend)

@app.route("/")
def chart2(
    # income: float,
    # contribution_size: float,
    # current_age: int,
    # retirement_age: int,
    # retirement_spending: float,
):
    legend = "Yearly Data"
    # labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    # values = [10, 9, 8, 7, 6, 4, 7, 8]

    accounts = ["roth_ira", 
                "traditional_ira", 
                "roth_401k",
                "traditional_401k"
                ]
    acount_balances = []
    for account in accounts:
        account_balance, tax_balance = contribution.contributions(
            income=1000300.0,
            account=account,
            contribution_size=4030.0,
            current_age=17,
            retirement_age=30,
            retirement_spending=4321.25,
        )
        print(account_balance)
        acount_balances.append(account_balance[-1])
        
    max_account_balance = max(acount_balances)
    max_account_balance_index = acount_balances.index(max_account_balance)
    
    account_balances, tax_balance = contribution.contributions(
        income=10032000.0,
        account=accounts[max_account_balance_index],
        contribution_size=43200.0,
        current_age=20,
        retirement_age=80,
        retirement_spending=43831.25,
    )
    
    values = account_balances
    labels = [i for i in range(len(account_balances)/3)]
    return render_template("index.html", values=values, labels=labels, legend=legend)


@app.route("/survey/fin_dec_survey.html")
def survey():
    return render_template("fin_dec_survey.html")


@app.route("/templates/index.html")
def back():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
