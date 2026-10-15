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


# Introduction to Sets
def average(array):
    distinct = set(array)

    total = sum(distinct)
    how_many = len(distinct)
    result = total / how_many

    return round(result, 3)


# No Idea!
def no_idea():
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))

    happiness = 0

    for number in array:
        if number in A:
            happiness = happiness + 1
        elif number in B:
            happiness = happiness - 1

    print(happiness)


# Symmetric Difference
def symmetric_difference():
    m = int(input())
    a = set(map(int, input().split()))
    n = int(input())
    b = set(map(int, input().split()))

    result = a.symmetric_difference(b)
    result = sorted(result)

    for number in result:
        print(number)


# Set .add()
def set_add():
    n = int(input())

    countries = set()

    for i in range(n):
        name = input()
        countries.add(name)

    print(len(countries))


# Set .discard(), .remove() & .pop()
def set_discard_remove_pop():
    n = int(input())
    s = set(map(int, input().split()))

    num_commands = int(input())

    for i in range(num_commands):
        line = input().split()
        command = line[0]

        if command == "pop":
            s.pop()
        elif command == "remove":
            value = int(line[1])
            s.remove(value)
        elif command == "discard":
            value = int(line[1])
            s.discard(value)

    print(sum(s))


# Set .union() Operation
def set_union():
    n = int(input())
    english = set(map(int, input().split()))

    b = int(input())
    french = set(map(int, input().split()))

    all_students = english.union(french)

    print(len(all_students))


# Set .intersection() Operation
def set_intersection():
    n = int(input())
    english = set(map(int, input().split()))

    b = int(input())
    french = set(map(int, input().split()))

    both = english.intersection(french)

    print(len(both))


# Set .difference() Operation
def set_difference():
    n = int(input())
    english = set(map(int, input().split()))

    b = int(input())
    french = set(map(int, input().split()))

    only_english = english.difference(french)

    print(len(only_english))


# Set .symmetric_difference() Operation
def set_symmetric_difference():
    n = int(input())
    english = set(map(int, input().split()))

    b = int(input())
    french = set(map(int, input().split()))

    one_only = english.symmetric_difference(french)

    print(len(one_only))


# Set Mutations
def set_mutations():
    a_size = int(input())
    A = set(map(int, input().split()))

    n = int(input())

    for i in range(n):
        line = input().split()
        command = line[0]

        other = set(map(int, input().split()))

        if command == "update":
            A.update(other)
        elif command == "intersection_update":
            A.intersection_update(other)
        elif command == "difference_update":
            A.difference_update(other)
        elif command == "symmetric_difference_update":
            A.symmetric_difference_update(other)

    print(sum(A))


# The Captain's Room
def captains_room():
    k = int(input())
    rooms = input().split()

    counts = {}

    for room in rooms:
        if room in counts:
            counts[room] = counts[room] + 1
        else:
            counts[room] = 1

    for room in counts:
        if counts[room] == 1:
            print(room)


# Check Subset
def check_subset():
    t = int(input())

    for i in range(t):
        size_a = int(input())
        A = set(input().split())

        size_b = int(input())
        B = set(input().split())

        print(A.issubset(B))


# Check Strict Superset
def check_strict_superset():
    A = set(input().split())
    n = int(input())

    result = True

    for i in range(n):
        other = set(input().split())

        if not A > other:
            result = False

    print(result)


# collections.Counter()
def collections_counter():
    from collections import Counter

    x = int(input())
    sizes = list(map(int, input().split()))
    n = int(input())

    shoes = Counter(sizes)

    money = 0

    for i in range(n):
        size, price = map(int, input().split())

        if shoes[size] > 0:
            money = money + price
            shoes[size] = shoes[size] - 1

    print(money)


# DefaultDict Tutorial
def defaultdict_tutorial():
    from collections import defaultdict

    n, m = map(int, input().split())

    positions = defaultdict(list)

    for i in range(1, n + 1):
        word = input()
        positions[word].append(i)

    for j in range(m):
        word = input()

        if word in positions:
            result = ""
            for p in positions[word]:
                result = result + str(p) + " "
            print(result.strip())
        else:
            print(-1)


# Collections.namedtuple()
def collections_namedtuple():
    from collections import namedtuple

    n = int(input())
    columns = input().split()

    Student = namedtuple("Student", columns)

    total = 0

    for i in range(n):
        values = input().split()
        student = Student(*values)
        total = total + int(student.MARKS)

    average = total / n

    print("%.2f" % average)


# Collections.OrderedDict()
def collections_ordereddict():
    from collections import OrderedDict

    n = int(input())

    items = OrderedDict()

    for i in range(n):
        parts = input().split()
        price = int(parts[-1])
        name = " ".join(parts[:-1])

        if name in items:
            items[name] = items[name] + price
        else:
            items[name] = price

    for name in items:
        print(name, items[name])


# Collections.deque()
def collections_deque():
    from collections import deque

    n = int(input())

    d = deque()

    for i in range(n):
        line = input().split()
        command = line[0]

        if command == "append":
            d.append(int(line[1]))
        elif command == "appendleft":
            d.appendleft(int(line[1]))
        elif command == "pop":
            d.pop()
        elif command == "popleft":
            d.popleft()

    print(" ".join(map(str, d)))


# Time Delta
def time_delta(t1, t2):
    from datetime import datetime

    form = "%a %d %b %Y %H:%M:%S %z"

    time1 = datetime.strptime(t1, form)
    time2 = datetime.strptime(t2, form)

    difference = abs(time1 - time2)
    seconds = int(difference.total_seconds())

    return str(seconds)


# Calendar Module
def calendar_module():
    import calendar

    month, day, year = map(int, input().split())

    number = calendar.weekday(year, month, day)

    days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

    print(days[number])


# Zipped!
def zipped():
    n, x = map(int, input().split())

    marks = []

    for i in range(x):
        subject = list(map(float, input().split()))
        marks.append(subject)

    for student in zip(*marks):
        average = sum(student) / x
        print("%.1f" % average)


# Athlete Sort
def athlete_sort():
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    def get_attribute(row):
        return row[k]

    arr.sort(key=get_attribute)

    for row in arr:
        print(" ".join(map(str, row)))


# ginortS
def ginorts():
    s = input()

    lower = []
    upper = []
    odd = []
    even = []

    for c in s:
        if c.islower():
            lower.append(c)
        elif c.isupper():
            upper.append(c)
        elif int(c) % 2 == 1:
            odd.append(c)
        else:
            even.append(c)

    lower.sort()
    upper.sort()
    odd.sort()
    even.sort()

    print("".join(lower + upper + odd + even))


# Map and Lambda Function
cube = lambda x: x ** 3


def fibonacci(n):
    numbers = []

    a = 0
    b = 1

    for i in range(n):
        numbers.append(a)
        a, b = b, a + b

    return numbers


def map_and_lambda():
    n = int(input())
    print(list(map(cube, fibonacci(n))))


# Detect Floating Point Number
def detect_floating_point_number():
    import re

    t = int(input())

    for i in range(t):
        s = input()

        if re.match(r"^[+-]?[0-9]*\.[0-9]+$", s):
            print(True)
        else:
            print(False)


# Re.split()
def re_split():
    import re

    regex_pattern = r"[,.]"

    print("\n".join(re.split(regex_pattern, input())))


# Group(), Groups() & Groupdict()
def group_groups_groupdict():
    import re

    s = input()

    match = re.search(r"([a-zA-Z0-9])\1", s)

    if match:
        print(match.group(1))
    else:
        print(-1)


# Re.findall() & Re.finditer()
def re_findall_finditer():
    import re

    s = input()

    vowels = "aeiouAEIOU"
    consonants = "qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM"

    pattern = "(?<=[" + consonants + "])([" + vowels + "]{2,})(?=[" + consonants + "])"

    found = re.findall(pattern, s)

    if len(found) > 0:
        for word in found:
            print(word)
    else:
        print(-1)


# Re.start() & Re.end()
def re_start_end():
    import re

    s = input()
    k = input()

    matches = list(re.finditer("(?=(" + k + "))", s))

    if len(matches) == 0:
        print((-1, -1))
    else:
        for m in matches:
            start = m.start(1)
            end = m.end(1) - 1
            print((start, end))


# Regex Substitution
def regex_substitution():
    import re

    n = int(input())

    for i in range(n):
        line = input()

        line = re.sub(r"(?<= )&&(?= )", "and", line)
        line = re.sub(r"(?<= )\|\|(?= )", "or", line)

        print(line)


# Validating Roman Numerals
def validating_roman_numerals():
    import re

    regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

    print(str(bool(re.match(regex_pattern, input()))))


# Validating phone numbers
def validating_phone_numbers():
    import re

    n = int(input())

    for i in range(n):
        number = input()

        if re.match(r"^[789][0-9]{9}$", number):
            print("YES")
        else:
            print("NO")


# Validating and Parsing Email Addresses
def validating_email_addresses():
    import re
    import email.utils

    n = int(input())

    for i in range(n):
        line = input()

        name, address = email.utils.parseaddr(line)

        if re.match(r"^[A-Za-z][A-Za-z0-9._-]*@[A-Za-z]+\.[A-Za-z]{1,3}$", address):
            print(email.utils.formataddr((name, address)))


# Hex Color Code
def hex_color_code():
    import re

    n = int(input())

    depth = 0

    for i in range(n):
        line = input()

        if depth > 0:
            text = line
        elif "{" in line:
            text = line.split("{", 1)[1]
        else:
            text = ""

        colors = re.findall(r"#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3})(?!\w)", text)

        for color in colors:
            print(color)

        depth = depth + line.count("{") - line.count("}")


# XML 1 - Find the Score
def get_attr_number(node):
    total = len(node.attrib)

    for child in node:
        total = total + get_attr_number(child)

    return total


# XML2 - Find the Maximum Depth
maxdepth = 0


def depth(elem, level):
    global maxdepth
    level = level + 1

    if level > maxdepth:
        maxdepth = level

    for child in elem:
        depth(child, level)
