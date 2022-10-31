def bmi(weight, height):
    b = weight / height ** 2
    print(['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)])
    print(b)

#     bmi = weight / height ** 2
#     if bmi <= 18.5:
#         return "Underweight"
#     elif bmi <= 25:
#         return "Normal"
#     elif bmi <= 30:
#         return "Overweight"
#     else:
#         return "Obese"

bmi(82, 1.82)