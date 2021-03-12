height = float(input("What's your height? m: "))
weight = float(input("What's your weight? kg: "))

imc = weight / (height ** 2)

status_imc = ""
if ( imc < 18.5):
    status_imc = "Under weight"
elif ( imc >= 18.5 and imc < 25 ):
    status_imc = "Ideal weight"
elif ( imc >= 25 and imc < 30 ):
    status_imc = "Overweight"
elif ( imc >= 30 and imc < 40):
    status_imc = "Obesity"
else:
    status_imc = "Morbid obesity"

print()
print("- " * 50)
print()

print("Your IMC is {:.2f} and you are {}".format(imc, status_imc))