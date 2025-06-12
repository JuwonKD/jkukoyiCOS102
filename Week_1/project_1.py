P = float(input("Enter the Principal Amount: "))
R = float(input("Enter the Annual Interest Rate (in %): "))
T = float(input("Enter the Time Period (years): "))
n = int(input("Enter the Number of Compounding Periods per Year: "))
PMT = float(input("Enter the Periodic Payment for Annuity: "))

def simple_interest(P,R,T):
    A = P * (1 + (R / 100) * T)
    return A

def compound_interest(P,R,n,T):
    A = P * (1 + R / n) ** (n * T)
    return A

def annuity_plan(PMT,R,t,n):
    A = PMT *(((1 + R/n) **(n*t) -1) / (R/n))
    return A

simple_A = simple_interest(P,R,T)
compound_A = compound_interest(P,R/100,n,T)
annuity_A = annuity_plan(PMT,R/100,n,T)

print("\nResults: ")
print(f"Simple Interest Amount: {simple_A:.2f}")
print(f"Compound Interest Amount: {compound_A:.2f}")
print(f"Annuity Plan Amount: {annuity_A:.2f}")
