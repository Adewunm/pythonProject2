print("welcome to Developers Games")

playing = input("Do u want to play? ")

if playing.lower() != "yes":
    quit()
print("okay let's play :)")
score = 0

answer = input("which ide is suitable for training model? ")
if answer.lower() == "jupyter":
    print("correct")
    score += 1
else:
    print("incorrect !")

answer = input("which module is suitable for graphics in python? ")
if answer.lower() == "turtle":
    print("correct")
    score += 1
else:
    print("incorrect !")

answer = input("which module is use Api? ")
if answer.lower() == "flask":
    print("correct")
    score += 1
else:
    print("incorrect !")


answer = input("which module is use for graphs in python? ")
if answer.lower() == "matplotlib":
    print("correct")
    score += 1
else:
    print("incorrect !")


print("you got " + str(score) + " question correct !")
print("you got " + str((score /4) * 100) + "%.")
