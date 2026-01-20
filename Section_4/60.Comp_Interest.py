"""
Docstring for 60.Comp_Interest:

            Calculate compound interest.

            principal : initial amount (P)
            rate      : annual interest rate in decimal (e.g. 0.05 for 5%)
            time      : number of years (t)
            n         : times interest is compounded per year (default = 12)

            Returns: final amount (A) and interest earned
        
            Efficiency : Time complexity: O(logt)
                         Space complexity: O(1)

"""
# Method - 1
p, r, t = map(float,input("Enter the Principal Amt, ROI, Time (in yrs): ").split())
n = int(input("Enter the compounding periods: "))

def ci(principal, rate:float, time, n=1):
    rate/=1
    amount = principal * (1 + rate/n)**(n*time)
    interest = amount - principal
    return round(amount, 2), round(interest, 2)

A, CI = ci(p,r,t,n)
print(f"Final Amount: {A}\nInterest Earned: {CI}""")

# Method - 2
def cI_s():
    p, r, n, t = map(float, input("Enter P r n t: ").split())
    print(round(p * (1 + r / n)**(n * t), 2))
cI_s()
# Method - 3
def ci_m():
    p = float(input("Enter Principal (P): "))
    r = float(input("Enter Annual Interest Rate as decimal (r): "))
    n = int(input("Enter compounding periods per year (n): "))
    t = float(input("Enter total years (t): "))

    amount = p * (1 + r / n)**(n * t) 
    print(f"Output: {amount:.2f}")

ci_m()