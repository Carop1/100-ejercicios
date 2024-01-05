r = float(input("Radio: "))
h = float(input("Altura: "))
pi = 3.1415
a = round(2*pi*r*(h+r),3)
v = round(pi*(r*r)*h,3)
print(f"Area total del cilindro: {a} cm2")
print(f"Volumen del cilindro: {v} cm3")