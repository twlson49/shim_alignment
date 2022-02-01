#
#where
#A = payment Amount per period
#P = initial Principal (loan amount)
#r = interest rate per period
#n = total number of payments or periods
#Example: What would the monthly payment be on a 5-year, $20,000 car loan with a nominal 7.5% annual interest rate? We'll assume that the original price was $21,000 and that you've made a $1,000 down payment.

def amort(P,r,n):
    
    A = (P*(r*(1+r)**n))/((1+r)**n-1)
    return A
P=72000
r=.0069 #r = 8.235% per year / 12 months = 0.0069% per period (this is entered as 0.00625 in the calculator)
n=360  # = 5 * 12
print(amort(P,r,n))