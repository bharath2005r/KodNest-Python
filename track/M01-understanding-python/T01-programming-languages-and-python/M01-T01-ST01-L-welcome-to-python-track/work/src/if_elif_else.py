marks = int(input())
attendence = int(input())
project = input()
if (marks >= 60 and attendence >= 75):
    if project == "yes":
        print("Eligible")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")

