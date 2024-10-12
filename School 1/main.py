from pdp import menu_students, menu_teachers, auth, users

is_logged_in = False
current_user = None
user_type = None

while True:
    if not is_logged_in:
        print(auth)
        inputauth = int(input('Tanlang: '))
 
        if inputauth == 1: 
            inputusername = input('username kiriting: ')
            inputpassword = input('password kiriting: ')
            tekshirish = False

            for teacher_id, teacher in users["teacher"].items():
                if teacher["username"] == inputusername and str(teacher["password"]) == str(inputpassword):
                    print("Xush kelibsiz\nSiz o'qituvchisiz!")
                    tekshirish = True
                    is_logged_in = True
                    current_user = teacher  
                    user_type = 'teacher'
                    break

            for student_id, student in users["students"].items():
                if student["username"] == inputusername and str(student["password"]) == str(inputpassword):
                    print("Xush kelibsiz\nSiz o'quvchisiz!")
                    tekshirish = True
                    is_logged_in = True
                    current_user = student  
                    user_type = 'student'
                    break

            if not tekshirish:
                print("Username yoki password noto'g'ri!")
        elif inputauth == 2:  
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
        else:
            print('Bunday tanlov yo\'q')
    else:
        if user_type == 'student':
            print(menu_students)
            input_menu = int(input('Tanlang: '))
            
            if input_menu == 1: 
                print(f"Fullname: {current_user['fullname']}")
            elif input_menu == 2:  
                print(f"Grade: {current_user['grade']}")
            elif input_menu == 3:  
                print(f"Class: {current_user['class']}")
            elif input_menu == 4: 
                print(f"HomeTask: {current_user['homeTask']}")
            else:
                print("Noto'g'ri tanlov!")
        elif user_type == 'teacher':
            print(menu_teachers)
            input_menu = int(input('Tanlang: '))
            
            if input_menu == 1: 
                print("Bu sizning sinflaringiz!")
                print(users['students'])
            elif input_menu == 2:  
                print("Bu sizning o'quvchilaringiz!")
                for k, v in users['students'].items():
                    print(f"ID: {k}, FullName: {v['fullname']}, Grade: {v['grade']}, Class: {v['class']}")
            elif input_menu == 3:
                print("Baholamoqchi bo'lgan o'quvchingizning ID sini yuboring!")
                student_id = input('Kiriting: ')
                for k, v in users['students'].items():
                    print(k)
                    print(v)
                    if student_id in k:
                        print(f"{k}")
            elif input_menu == 4:
                break
            else:
                print("Noto'g'ri tanlov!")
