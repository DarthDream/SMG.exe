import json
student = {}
next_id = 1

try:
    with open("student.json", "r") as file:
        data = json.load(file)

        if "student" in data:
            product = data["student"]
            next_id = data.get("next_id", 1)

        else:
            for name, price in data.items():
                student[name] = {
                    "id": next_id,
                    "price": price
                }
                next_id += 1

            next_id = max(
                [info["id"] for info in student.values()],
                default=0
            ) + 1

except (FileNotFoundError, KeyError, json.JSONDecodeError):
    product = {}
    next_id = 1

def save_student():
    with open("student.json", "w") as file:
        json.dump({
            "next_id": next_id,
            "Student": product
        }, file, indent=4)


def save_json():
    save_student()
    print("JSON fayli yadda saxlanildi")


def get_price(name):
    return product[name]["price"]


def sort_by_pricepl():
    qiymet = sorted(student, key=get_price, reverse=False)

    for name in qiymet:
        print(f"ID: {student[name]['id']} | {name} | {student[name]['price']}")



def sort_by_pricemn():
    qiymet = sorted(student, key=get_price, reverse=True)

    for name in qiymet:
        print(f"ID: {student[name]['id']} | {name} | {student[name]['price']}")


def filter_student():
    print('''
    1.Azdan coxa
    2.Coxdan aza
    3.Back
    ''')

    try:
        choice = int(input("Secim et: "))

        if choice == 1:
            print("Azdan coxa siralandi")
            sort_by_pricepl()

        elif choice == 2:
            print("Coxdan aza siralandi")
            sort_by_pricemn()

        elif choice == 3:
            return

        else:
            print("Sehv choice!!!")

    except ValueError:
        print("ERROR 404 have problem")


def add_student():
    global next_id

    try:
        sagird = input("Sagird daxil et: ").strip()

        if not sagird:
            print("Sagird adi bos ola bilmez")
            return

        for name in product:
            if name.lower() == sagird.lower():
                print("Sagird artiq var")
                return

        qiymet = float(input("Qiymet daxil et: "))

        if qiymet < 0:
            print("Qiymet menfi ola bilmez")
            return

        product[sagird] = {
            "id": next_id,
            "price": qiymet
        }

        print(f"Sagird elave edildi! ID: {next_id}")

        next_id += 1
        save_student()

    except ValueError:
        print("ERROR 404 have problem")


def show_student():
    if not student:
        print("Sagird yoxdur")
        return

    for name, info in student.items():
        print(f"ID: {info['id']} | Sagird: {name} | Qiymet: {info['price']}")


def delete_student():
    try:
        student_id = int(input("Sagirdin ID-ni daxil et: "))

        for name in list(student):
            if student[name]["id"] == student_id:
                del student[name]
                save_student()
                print("Sagird silindi")
                return

        print("Bu ID-de sagird yoxdur")

    except ValueError:
        print("Duzgun ID daxil et!")




def app():
    while True:
        print('''
        ============ STUDENT MANAGEMENT SYSTEM ============
        
            1.Add Student
            2.Show Student
            3.Delete Student By ID
            4.Save JSON
            5.Filter by price

                ***6.Exit***
        ''')

        try:
            choice = int(input("Secim et: "))

            if choice == 1:
                add_student()

            elif choice == 2:
                show_student()

            elif choice == 3:
                delete_student()

            elif choice == 4:
                save_json()

            elif choice == 5:
                filter_student()

            elif choice == 6:
                break

            else:
                print("Yanlis secim")

        except ValueError:
            print("Duzgun secim daxil et!")