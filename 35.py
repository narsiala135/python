def calculate_grade(aggregate):
    if aggregate > 75:
        return "DISTINCTION"
    elif 60 <= aggregate < 75:
        return "First Division"
    elif 50 <= aggregate < 60:
        return "Second Division"
    elif 40 <= aggregate < 50:
        return "Third Division"
    else:
        return "Fail"
marks = []
subjects = ["Python", "C Programming", "Mathematics", "Physics"]
for subject in subjects:
    mark = float(input(f"Enter the marks in {subject}: "))
    marks.append(mark)
total = sum(marks)
aggregate = total / len(marks)

# Display total and aggregate
print("Total =", total)
print("Aggregate =", aggregate)

# Determine and display the grade
print(calculate_grade(aggregate))
