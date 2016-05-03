principal = 100000
interest_rate = 5
pay_per_month = 500
Balance = principal
month = 0
paid_amount = 0
while Balance > 0 :
    interest_charge = (float(principal)*interest_rate/100)/12
    Balance = principal - pay_per_month + interest_charge
    if principal < pay_per_month:
	pay_per_month = principal + interest_charge
	Balance = 0
    principal = Balance
    month = month + 1
    paid_amount = paid_amount + pay_per_month  
    print ("{0}   ${1:.2f}    ${2:.2f}    ${3:.2f}").format(month, pay_per_month,interest_charge, Balance)
 
years = month/12
months = month%12

print "You paid a total of {:.2f} over {} years and {} months".format(paid_amount,years,months)    
