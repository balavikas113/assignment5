dict={'Bala':98,'Akash':82,'Alice':85,'Sathwika':40}
n=input("Enter the student's name:")

if (n in dict):
    print("Alice's marks:",dict[n])
else:
    print("Student not found")
