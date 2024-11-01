n = int(input("Enter any number: "))
mod = int(input("What mod you want to use?\n"))

def congruence_modulo():
    remainder = n%mod
    result = f'{n} ≡ {remainder} mod({mod})'
    return result
    
Result = congruence_modulo()
print(Result)
