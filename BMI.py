#BMI counter © pfrmn
print("BMI Calculator")
language = input("Language: PL/DE:")
weight = input("Podaj swoją wagę w Kg:")
heightcmString = input("Podaj swoją wysokość w cm:")
height = heightcm / 100

weightInt: float = (float(weight))
heightInt = (float(height))
def BMI = weightInt / (heightInt * heightInt)
BMIround = (round(BMI, 2))
BMIoutput = (str(BMIround))

if BMI >= 40 and language == "PL":
    print("Otyłość III stopnia, BMI: " + BMIoutput)
elif BMI >= 40 and language == "DE":
    print("Extreme Adipositas, BMI: " + BMIoutput)
elif 35 <= BMI < 40:
    print("Otyłość II stopnia, BMI wynosi: " + BMIoutput)
elif 30 <= BMI < 35:
    print("Otyłość I stopnia, BMI wynosi: " + BMIoutput)
elif 27.5 <= BMI < 30:
    print("Nadwaga wysoki przedział, BMI wynosi: " + BMIoutput)
elif 25 <= BMI < 27.5:
    print("Nadwaga niski przedział, BMI wynosi: " + BMIoutput)
elif 23 <= BMI < 25:
    print("Norma wysoki przedział, BMI wynosi: " + BMIoutput)         
elif 18.50 <= BMI < 23:
    print("Norma niski przedział, BMI wynosi: " + BMIoutput)
elif 17 <= BMI < 18.50:
    print("Niedowaga, BMI wynosi: " + BMIoutput)
elif 16 <= BMI < 17:
    print("Wychudzenie, BMI wynosi: " + BMIoutput)                  
else:
    print("Wygłodzenie, BMI wynosi " + BMIoutput)
