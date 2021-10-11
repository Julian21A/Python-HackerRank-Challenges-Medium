import math as m

ab=float(input())
bc=float(input())
mc=(m.hypot(bc,ab))/2
bc2=bc/2

out=(round(m.degrees(m.acos(bc2/(mc)))))
out=str(out)

print(out+chr(176))

