# Python If-Else
def python_if_else():
    n = int(input().strip())

    if n % 2 == 1:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")


# Loops
def loops():
    n = int(input())
    for i in range(n):
        print(i ** 2)


# Write a function
def is_leap(year):
    leap = False

    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True

    return leap


# Print Function
def print_function():
    n = int(input())
    for i in range(1, n + 1):
        print(i, end="")
    print()


# List Comprehensions
def list_comprehensions():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    result = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    print(result)


# Find the Runner-Up Score!
def runner_up_score():
    n = int(input())
    arr = map(int, input().split())

    scores = list(arr)
    no_duplicates = list(set(scores))
    no_duplicates.sort()

    print(no_duplicates[-2])


# Nested Lists
def nested_lists():
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    grades = []
    for s in students:
        grades.append(s[1])

    unique_grades = list(set(grades))
    unique_grades.sort()
    second_lowest = unique_grades[1]

    names = []
    for s in students:
        if s[1] == second_lowest:
            names.append(s[0])

    names.sort()

    for name in names:
        print(name)


# Finding the percentage
def finding_the_percentage():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    marks = student_marks[query_name]
    total = sum(marks)
    how_many = len(marks)
    average = total / how_many

    print("%.2f" % average)


# Lists
def lists():
    N = int(input())

    my_list = []

    for _ in range(N):
        line = input().split()
        command = line[0]

        if command == "insert":
            position = int(line[1])
            number = int(line[2])
            my_list.insert(position, number)
        elif command == "print":
            print(my_list)
        elif command == "remove":
            number = int(line[1])
            my_list.remove(number)
        elif command == "append":
            number = int(line[1])
            my_list.append(number)
        elif command == "sort":
            my_list.sort()
        elif command == "pop":
            my_list.pop()
        elif command == "reverse":
            my_list.reverse()


# Tuples
def tuples():
    n = int(input())
    numbers = input().split()

    my_list = []
    for x in numbers:
        my_list.append(int(x))

    t = tuple(my_list)

    print(hash(t))


# sWAP cASE
def swap_case(s):
    result = ""

    for c in s:
        if c.islower():
            result = result + c.upper()
        elif c.isupper():
            result = result + c.lower()
        else:
            result = result + c

    return result


# String Split and Join
def split_and_join(line):
    words = line.split(" ")
    result = "-".join(words)
    return result


# What's Your Name?
def print_full_name(first, last):
    print("Hello " + first + " " + last + "! You just delved into python.")


# Mutations
def mutate_string(string, position, character):
    letters = list(string)
    letters[position] = character
    new_string = "".join(letters)
    return new_string


# Find a string
def count_substring(string, sub_string):
    count = 0
    length = len(sub_string)

    for i in range(len(string) - length + 1):
        piece = string[i:i + length]
        if piece == sub_string:
            count = count + 1

    return count


# String Validators
def string_validators():
    s = input()

    has_alnum = False
    has_alpha = False
    has_digit = False
    has_lower = False
    has_upper = False

    for c in s:
        if c.isalnum():
            has_alnum = True
        if c.isalpha():
            has_alpha = True
        if c.isdigit():
            has_digit = True
        if c.islower():
            has_lower = True
        if c.isupper():
            has_upper = True

    print(has_alnum)
    print(has_alpha)
    print(has_digit)
    print(has_lower)
    print(has_upper)


# Text Alignment
def text_alignment():
    thickness = int(input())  # This must be an odd number
    c = 'H'

    for i in range(thickness):
        print((c*i).rjust(thickness-1) + c + (c*i).ljust(thickness-1))

    for i in range(thickness+1):
        print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

    for i in range((thickness+1)//2):
        print((c*thickness*5).center(thickness*6))

    for i in range(thickness+1):
        print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

    for i in range(thickness):
        print(((c*(thickness-i-1)).rjust(thickness) + c + (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


# Text Wrap
def wrap(string, max_width):
    result = ""

    for i in range(0, len(string), max_width):
        piece = string[i:i + max_width]
        result = result + piece + "\n"

    return result.strip()


# Designer Door Mat
def designer_door_mat():
    n, m = map(int, input().split())

    top_part = []

    for i in range(n // 2):
        pattern = ".|." * (2 * i + 1)
        row = pattern.center(m, "-")
        top_part.append(row)

    for row in top_part:
        print(row)

    print("WELCOME".center(m, "-"))

    for row in reversed(top_part):
        print(row)


# String Formatting
def print_formatted(number):
    width = len(bin(number)) - 2

    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]

        print(decimal.rjust(width), octal.rjust(width), hexadecimal.rjust(width), binary.rjust(width))


# Alphabet Rangoli
def print_rangoli(size):
    letters = "abcdefghijklmnopqrstuvwxyz"
    width = 4 * size - 3

    rows = []

    for i in range(size):
        left = []
        for j in range(size - 1, size - 2 - i, -1):
            left.append(letters[j])

        all_letters = left + left[-2::-1]

        row = "-".join(all_letters)
        row = row.center(width, "-")
        rows.append(row)

    for row in rows:
        print(row)

    for row in reversed(rows[:-1]):
        print(row)


# Capitalize!
def solve(s):
    words = s.split(" ")
    new_words = []

    for word in words:
        if len(word) > 0:
            new_word = word[0].upper() + word[1:]
        else:
            new_word = word
        new_words.append(new_word)

    result = " ".join(new_words)
    return result


# The Minion Game
def minion_game(string):
    vowels = "AEIOU"
    length = len(string)

    stuart_points = 0
    kevin_points = 0

    for i in range(length):
        if string[i] in vowels:
            kevin_points = kevin_points + (length - i)
        else:
            stuart_points = stuart_points + (length - i)

    if stuart_points > kevin_points:
        print("Stuart", stuart_points)
    elif kevin_points > stuart_points:
        print("Kevin", kevin_points)
    else:
        print("Draw")


# Merge the Tools!
def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        block = string[i:i + k]

        result = ""
        for letter in block:
            if letter not in result:
                result = result + letter

        print(result)
