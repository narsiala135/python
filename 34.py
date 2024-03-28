def count_special_characters(statement):
    special_characters = "!@#$%^&*()-_+=[]{}|;:,.<>?/"
    count = 0
    for char in statement:
        if char in special_characters:
            count += 1
    return count
given_statement = input("Enter the statement: ")
num_special_characters = count_special_characters(given_statement)
print("Number of special Characters:", num_special_characters)
