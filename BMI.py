#BMI counter

weight = input("Podaj swoją wagę w Kg:")
height = input("Podaj swoją wysokość w m.cm:")

weightInt = (float(weight))
heightInt = (float(height))
BMI = weightInt / (heightInt * heightInt)
BMIoutput = (str(BMI))

print("Twoje BMI to:" + BMIprint)