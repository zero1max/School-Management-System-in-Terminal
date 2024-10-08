users = {
    "students": {
        "1": {
            "fullname": "jack",
            "username": "jacks",
            "password": 1111,
            "grade": 4,
            "class": "10b23",
            "homeTask": "Decorators"
        },
        "2": {
            "fullname": "zero1max",
            "username": "zero",
            "password": 'zero',
            "grade": 4,
            "class": "10b23",
            "homeTask": "Decorators"
        },
    }
}

auth_menu = """
1. Login
2. Register
"""

menu = """
1. My profile
2. My lesson
3. My class
4. HomeTask
"""

is_logged_in = False
current_user = None 

def display_menu():
    print(menu)
    return int(input('Tanlang: '))

def show_profile(student):
    print(f"Fullname: {student['fullname']}")
    print(f"Grade: {student['grade']}")
    print(f"Class: {student['class']}")
    print(f"HomeTask: {student['homeTask']}")

def login():
    global is_logged_in, current_user
    inputusername = input('Username kiriting: ')
    inputpassword = input('Password kiriting: ')
    for student_id, student in users["students"].items():
        if student["username"] == inputusername and str(student["password"]) == str(inputpassword):
            print("Xush kelibsiz\n")
            is_logged_in = True  
            current_user = student  
            return True
    print("Username yoki password noto'g'ri!")
    return False

def register():
    inputfullname = input('Fullname kiriting: ')
    inputusername = input('Username kiriting: ')
    inputpassword = input('Password kiriting: ')
    inputgrade = int(input('Grade kiriting: '))
    inputclass = input('Class kiriting: ')
    inputhomeTask = input('HomeTask kiriting: ')

    new_id = str(len(users["students"]) + 1)
    users["students"][new_id] = {
        "fullname": inputfullname,
        "username": inputusername,
        "password": inputpassword,
        "grade": inputgrade,
        "class": inputclass,
        "homeTask": inputhomeTask
    }
    print("Foydalanuvchi muvaffaqiyatli ro'yxatdan o'tdi!")

while True:
    if not is_logged_in:
        print(auth_menu)
        inputauth = int(input('Tanlang: '))
        if inputauth == 1:
            if login():
                pass  
            else:
                continue  
        elif inputauth == 2:
            register()
        else:
            print('Bunday tanlov yo\'q')
    else:
        input_menu = display_menu()
        if input_menu == 1:
            show_profile(current_user)
        elif input_menu == 2:
            print(f"Grade: {current_user['grade']}")
        elif input_menu == 3:
            print(f"Class: {current_user['class']}")
        elif input_menu == 4:
            print(f"HomeTask: {current_user['homeTask']}")
        else:
            print("Noto'g'ri tanlov!")
