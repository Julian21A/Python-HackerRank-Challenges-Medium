import re

validator=re.compile(r"^"
r"(?!.*(\d)(-?\1){3})"
r"[456]"
r"\d{3}"
r"(?:-?\d{4}){3}"
r"$")

for i in range(int(input())):
    x=validator.search(str(input()))
    if x: print('Valid')  
    else: print('Invalid')    
