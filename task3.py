"""Create a grading system: Take input marks (0-100) and display grades like A, B, C, D, or Fail based on defined ranges."""
marks = int(input("enter your marks : "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "Fail"

print(f"You scored {marks}, and your grade is {grade}.")
