def loose_change(cents):
    resultado = {}
    cuenta_quarters = 0
    cuenta_nickels = 0
    cuenta_dimes = 0
    cuenta_pennies = 0
    nickels = 5
    pennies = 1
    dimes = 10
    quarters =25  
    while cents >= quarters:
        cents -= quarters
        cuenta_quarters += 1
    while cents >= dimes:
        cents -= dimes
        cuenta_dimes += 1
    while cents >= nickels:
        cents -= nickels
        cuenta_nickels += 1
    while cents >= pennies:
        cents -= pennies
        cuenta_pennies += 1
    resultado["Quarters"] = cuenta_quarters
    resultado["Dimes"] = cuenta_dimes
    resultado["Pennies"] = cuenta_pennies
    resultado["Nickels"] = cuenta_nickels
    return resultado
