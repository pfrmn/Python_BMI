#BMI counter © pfrmn
print("BMI Calculator")
language = input("Language: PL/DE:")
weight = input("Podaj swoją wagę w Kg:")
heightcmString = input("Podaj swoją wysokość w cm:")
heightcm = (float(heightcmString))

height = heightcm / 100

weightInt = (float(weight))
heightInt = (float(height))
BMI = weightInt / (heightInt * heightInt)
BMIround = (round(BMI, 2))
BMIoutput = (str(BMIround))

if BMI >= 40:
    print(BMIoutput)
if language == "PL":
            print:("Otyłość III stopnia")
elif language == "DE":
    print("Extreme Adipositas")
else 35 <= BMI < 40:
if language == "PL":
            print:("Otyłość II stopnia")
else language == "DE":
    print("Starke Adipositas")