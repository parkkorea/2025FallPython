# Dohyeong Park
# module2_lab_caseStudy
# This app is for module 2 Lab, Using if...else and while. Test if the student qualifies for either the Dean's List or the Honor Roll

while True:
    last_name = input("Enter last name (if you want to quit enter ZZZ): ")
    if last_name == 'ZZZ':
        break

    first_name = input("Enter first name: ")
    gpa = float(input("Enter GPA: "))

    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")
