n = int(input("Enter any number: "))
mod = int(input("What mod you want to use?\n"))

def congruence_modulo():
    remainder = n%mod
    result = f'{n} ≡ {remainder} mod({mod})' #WE CAN ALSO USE THIS PIECE OF CODE TO GENERATE TRIGRAM SYMBOL '\u2630'
    return result
    
Result = congruence_modulo()
print(Result)
