#BMI counter © pfrmn

weight = input("Podaj swoją wagę w Kg:")
height = input("Podaj swoją wysokość w m.cm:")

weightInt = (float(weight))
heightInt = (float(height))
BMI = weightInt / (heightInt * heightInt)
BMIround = (round(BMI, 2))
BMIoutput = (str(BMIround))

if BMI >= 40:
    print("Otyłość III stopnia, BMI wynosi: " + BMIoutput)
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
    print("Wygłodzenie, BMI wynosi" + BMIoutput)
