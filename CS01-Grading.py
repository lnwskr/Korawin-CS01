a = int(input("คะแนนเก็บ = "))
b = int(input("สอบกลางภาค = "))
c = int(input("สอบปลายภาค = "))

x = a + b + c
if (x >= 80 and x <= 100):
    print("A")
elif (x >= 75 and x < 80):
    print("B+")
elif (x >= 70 and x < 75):
    print("B")
elif (x >= 65 and x < 70):
    print("C+")
elif (x >= 60 and x < 65):
    print("C")
elif (x >= 55 and x < 60):
    print("D+")
elif (x >= 50 and x < 55):
    print("D")
elif (x >= 0 and x < 50):
    print("F")