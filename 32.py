def calculate_users(total_users, staff_users):

    student_users = total_users - staff_users

    non_teaching_staff_users = staff_users // 3

    return student_users, non_teaching_staff_users

def main():
    try:
        total_users = int(input("Total Users: "))
        staff_users = int(input("Staff Users: "))

        if total_users < 0 or staff_users < 0:
            print("Please enter positive numbers.")
        else:
            student_users, non_teaching_staff_users = calculate_users(total_users, staff_users)
            print("Student Users:", student_users)
            print("Non-teaching Staff Users:", non_teaching_staff_users)
    except ValueError:
        print("Please enter valid integer inputs.")

test_cases = [
    (0, 0),
    (-143, 0),
    (1026, 1026),
    (450, 540),
    (600, 450)
]

for idx, (total, staff) in enumerate(test_cases, start=1):
    print("\nTest Case", idx)
    print("Total User:", total)
    print("Staff User:", staff)
    main()
