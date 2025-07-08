#  Currency to USD Calculator

# User Inputs
pesos = int(input("How many Mexican Pesos do you have? "))
soles = int(input("How many Peruvian Soles do you have? "))
reais = int(input("How many Brazilian Reais do you have? "))

# Conversion Rates (as of now, may change over time)
USD_PER_PESO = 0.00025
USD_PER_SOLE = 0.28
USD_PER_REAL = 0.18

# Calculations
usd_from_pesos = pesos * USD_PER_PESO
usd_from_soles = soles * USD_PER_SOLE
usd_from_reais = reais * USD_PER_REAL

total_usd = usd_from_pesos + usd_from_soles + usd_from_reais

# Output
print(f"\nYou have approximately ${total_usd:.2f} USD in total.")
