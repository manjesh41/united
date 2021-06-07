'''price of a house is one  million
if buyers has good credit,
they need to put down 10%
otherwise
they need to put down 20%
print the down payment'''
price=1000000
has_good_credit=True

if has_good_credit:
   down_payemnt=0.1*price
else:
   down_paymet=0.2*price
print(f"Down_payment: ${down_payemnt}")

