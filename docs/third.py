import json
import os

class Student:
    def __init__(self, name, roll_no, marks, grade):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        self.grade = grade

    def to_dict(self):
        return {
            'name': self.name,
            'roll_no': self.roll_no,
            'marks': self.marks,
            'grade': self.grade
        }

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Roll No: {self.roll_no}\n"
                f"Marks: {self.marks}\n"
                f"Grade: {self.grade}")

class StudentDatabase:
    def __init__(self, filename='students.json'):
        self.filename = filename
        self.students = []
        self.load_students()

    def load_students(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.students = [Student(**item) for item in data]

    def save_students(self):
        with open(self.filename, 'w') as f:
            json.dump([s.to_dict() for s in self.students], f, indent=4)

    def add_student(self):
        print("\n📘 Add New Student")
        name = input("Enter Name: ")
        roll_no = input("Enter Roll Number: ")
        marks = float(input("Enter Marks: "))
        grade = input("Enter Grade: ")
        if any(s.roll_no == roll_no for s in self.students):
            print("❌ Student with this roll number already exists.")
            return
        student = Student(name, roll_no, marks, grade)
        self.students.append(student)
        self.save_students()
        print("✅ Student added successfully.")

    def view_students(self):
        print("\n📋 All Students")
        if not self.students:
            print("No records found.")
            return
        for idx, student in enumerate(self.students, 1):
            print(f"\nStudent #{idx}")
            print(student)

    def search_student(self):
        roll_no = input("\n🔍 Enter Roll Number to search: ")
        found = False
        for student in self.students:
            if student.roll_no == roll_no:
                print("\n📄 Student Found:")
                print(student)
                found = True
                break
        if not found:
            print("❌ Student not found.")

    def update_student(self):
        roll_no = input("\n✏️ Enter Roll Number to update: ")
        for student in self.students:
            if student.roll_no == roll_no:
                print("Leave blank to keep current value.")
                name = input(f"Enter New Name [{student.name}]: ") or student.name
                marks = input(f"Enter New Marks [{student.marks}]: ")
                grade = input(f"Enter New Grade [{student.grade}]: ") or student.grade

                student.name = name
                student.marks = float(marks) if marks else student.marks
                student.grade = grade
                self.save_students()
                print("✅ Student record updated.")
                return
        print("❌ Student not found.")

    def delete_student(self):
        roll_no = input("\n🗑️ Enter Roll Number to delete: ")
        for i, student in enumerate(self.students):
            if student.roll_no == roll_no:
                confirm = input(f"Are you sure you want to delete {student.name}? (y/n): ")
                if confirm.lower() == 'y':
                    del self.students[i]
                    self.save_students()
                    print("✅ Student deleted.")
                return
        print("❌ Student not found.")

    def clear_database(self):
        confirm = input("⚠️ Are you sure you want to delete all records? (y/n): ")
        if confirm.lower() == 'y':
            self.students = []
            self.save_students()
            print("🧹 All records deleted.")

def main_menu():
    db = StudentDatabase()
    while True:
        print("\n🎓 Student Management System")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Clear All Records")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            db.add_student()
        elif choice == '2':
            db.view_students()
        elif choice == '3':
            db.search_student()
        elif choice == '4':
            db.update_student()
        elif choice == '5':
            db.delete_student()
        elif choice == '6':
            db.clear_database()
        elif choice == '7':
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()

import json
import os

class Student:
    def __init__(self, name, roll_no, marks, grade):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        self.grade = grade

    def to_dict(self):
        return {
            'name': self.name,
            'roll_no': self.roll_no,
            'marks': self.marks,
            'grade': self.grade
        }

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Roll No: {self.roll_no}\n"
                f"Marks: {self.marks}\n"
                f"Grade: {self.grade}")

class StudentDatabase:
    def __init__(self, filename='students.json'):
        self.filename = filename
        self.students = []
        self.load_students()

    def load_students(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.students = [Student(**item) for item in data]

    def save_students(self):
        with open(self.filename, 'w') as f:
            json.dump([s.to_dict() for s in self.students], f, indent=4)

    def add_student(self):
        print("\n📘 Add New Student")
        name = input("Enter Name: ")
        roll_no = input("Enter Roll Number: ")
        marks = float(input("Enter Marks: "))
        grade = input("Enter Grade: ")
        if any(s.roll_no == roll_no for s in self.students):
            print("❌ Student with this roll number already exists.")
            return
        student = Student(name, roll_no, marks, grade)
        self.students.append(student)
        self.save_students()
        print("✅ Student added successfully.")

    def view_students(self):
        print("\n📋 All Students")
        if not self.students:
            print("No records found.")
            return
        for idx, student in enumerate(self.students, 1):
            print(f"\nStudent #{idx}")
            print(student)

    def search_student(self):
        roll_no = input("\n🔍 Enter Roll Number to search: ")
        found = False
        for student in self.students:
            if student.roll_no == roll_no:
                print("\n📄 Student Found:")
                print(student)
                found = True
                break
        if not found:
            print("❌ Student not found.")

    def update_student(self):
        roll_no = input("\n✏️ Enter Roll Number to update: ")
        for student in self.students:
            if student.roll_no == roll_no:
                print("Leave blank to keep current value.")
                name = input(f"Enter New Name [{student.name}]: ") or student.name
                marks = input(f"Enter New Marks [{student.marks}]: ")
                grade = input(f"Enter New Grade [{student.grade}]: ") or student.grade

                student.name = name
                student.marks = float(marks) if marks else student.marks
                student.grade = grade
                self.save_students()
                print("✅ Student record updated.")
                return
        print("❌ Student not found.")

    def delete_student(self):
        roll_no = input("\n🗑️ Enter Roll Number to delete: ")
        for i, student in enumerate(self.students):
            if student.roll_no == roll_no:
                confirm = input(f"Are you sure you want to delete {student.name}? (y/n): ")
                if confirm.lower() == 'y':
                    del self.students[i]
                    self.save_students()
                    print("✅ Student deleted.")
                return
        print("❌ Student not found.")

    def clear_database(self):
        confirm = input("⚠️ Are you sure you want to delete all records? (y/n): ")
        if confirm.lower() == 'y':
            self.students = []
            self.save_students()
            print("🧹 All records deleted.")

def main_menu():
    db = StudentDatabase()
    while True:
        print("\n🎓 Student Management System")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Clear All Records")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            db.add_student()
        elif choice == '2':
            db.view_students()
        elif choice == '3':
            db.search_student()
        elif choice == '4':
            db.update_student()
        elif choice == '5':
            db.delete_student()
        elif choice == '6':
            db.clear_database()
        elif choice == '7':
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()

import json
import os

class Student:
    def __init__(self, name, roll_no, marks, grade):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        self.grade = grade

    def to_dict(self):
        return {
            'name': self.name,
            'roll_no': self.roll_no,
            'marks': self.marks,
            'grade': self.grade
        }

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Roll No: {self.roll_no}\n"
                f"Marks: {self.marks}\n"
                f"Grade: {self.grade}")

class StudentDatabase:
    def __init__(self, filename='students.json'):
        self.filename = filename
        self.students = []
        self.load_students()

    def load_students(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.students = [Student(**item) for item in data]

    def save_students(self):
        with open(self.filename, 'w') as f:
            json.dump([s.to_dict() for s in self.students], f, indent=4)

    def add_student(self):
        print("\n📘 Add New Student")
        name = input("Enter Name: ")
        roll_no = input("Enter Roll Number: ")
        marks = float(input("Enter Marks: "))
        grade = input("Enter Grade: ")
        if any(s.roll_no == roll_no for s in self.students):
            print("❌ Student with this roll number already exists.")
            return
        student = Student(name, roll_no, marks, grade)
        self.students.append(student)
        self.save_students()
        print("✅ Student added successfully.")

    def view_students(self):
        print("\n📋 All Students")
        if not self.students:
            print("No records found.")
            return
        for idx, student in enumerate(self.students, 1):
            print(f"\nStudent #{idx}")
            print(student)

    def search_student(self):
        roll_no = input("\n🔍 Enter Roll Number to search: ")
        found = False
        for student in self.students:
            if student.roll_no == roll_no:
                print("\n📄 Student Found:")
                print(student)
                found = True
                break
        if not found:
            print("❌ Student not found.")

    def update_student(self):
        roll_no = input("\n✏️ Enter Roll Number to update: ")
        for student in self.students:
            if student.roll_no == roll_no:
                print("Leave blank to keep current value.")
                name = input(f"Enter New Name [{student.name}]: ") or student.name
                marks = input(f"Enter New Marks [{student.marks}]: ")
                grade = input(f"Enter New Grade [{student.grade}]: ") or student.grade

                student.name = name
                student.marks = float(marks) if marks else student.marks
                student.grade = grade
                self.save_students()
                print("✅ Student record updated.")
                return
        print("❌ Student not found.")

    def delete_student(self):
        roll_no = input("\n🗑️ Enter Roll Number to delete: ")
        for i, student in enumerate(self.students):
            if student.roll_no == roll_no:
                confirm = input(f"Are you sure you want to delete {student.name}? (y/n): ")
                if confirm.lower() == 'y':
                    del self.students[i]
                    self.save_students()
                    print("✅ Student deleted.")
                return
        print("❌ Student not found.")

    def clear_database(self):
        confirm = input("⚠️ Are you sure you want to delete all records? (y/n): ")
        if confirm.lower() == 'y':
            self.students = []
            self.save_students()
            print("🧹 All records deleted.")

def main_menu():
    db = StudentDatabase()
    while True:
        print("\n🎓 Student Management System")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Clear All Records")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            db.add_student()
        elif choice == '2':
            db.view_students()
        elif choice == '3':
            db.search_student()
        elif choice == '4':
            db.update_student()
        elif choice == '5':
            db.delete_student()
        elif choice == '6':
            db.clear_database()
        elif choice == '7':
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()

import json
import os

class Student:
    def __init__(self, name, roll_no, marks, grade):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        self.grade = grade

    def to_dict(self):
        return {
            'name': self.name,
            'roll_no': self.roll_no,
            'marks': self.marks,
            'grade': self.grade
        }

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Roll No: {self.roll_no}\n"
                f"Marks: {self.marks}\n"
                f"Grade: {self.grade}")

class StudentDatabase:
    def __init__(self, filename='students.json'):
        self.filename = filename
        self.students = []
        self.load_students()

    def load_students(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.students = [Student(**item) for item in data]

    def save_students(self):
        with open(self.filename, 'w') as f:
            json.dump([s.to_dict() for s in self.students], f, indent=4)

    def add_student(self):
        print("\n📘 Add New Student")
        name = input("Enter Name: ")
        roll_no = input("Enter Roll Number: ")
        marks = float(input("Enter Marks: "))
        grade = input("Enter Grade: ")
        if any(s.roll_no == roll_no for s in self.students):
            print("❌ Student with this roll number already exists.")
            return
        student = Student(name, roll_no, marks, grade)
        self.students.append(student)
        self.save_students()
        print("✅ Student added successfully.")

    def view_students(self):
        print("\n📋 All Students")
        if not self.students:
            print("No records found.")
            return
        for idx, student in enumerate(self.students, 1):
            print(f"\nStudent #{idx}")
            print(student)

    def search_student(self):
        roll_no = input("\n🔍 Enter Roll Number to search: ")
        found = False
        for student in self.students:
            if student.roll_no == roll_no:
                print("\n📄 Student Found:")
                print(student)
                found = True
                break
        if not found:
            print("❌ Student not found.")

    def update_student(self):
        roll_no = input("\n✏️ Enter Roll Number to update: ")
        for student in self.students:
            if student.roll_no == roll_no:
                print("Leave blank to keep current value.")
                name = input(f"Enter New Name [{student.name}]: ") or student.name
                marks = input(f"Enter New Marks [{student.marks}]: ")
                grade = input(f"Enter New Grade [{student.grade}]: ") or student.grade

                student.name = name
                student.marks = float(marks) if marks else student.marks
                student.grade = grade
                self.save_students()
                print("✅ Student record updated.")
                return
        print("❌ Student not found.")

    def delete_student(self):
        roll_no = input("\n🗑️ Enter Roll Number to delete: ")
        for i, student in enumerate(self.students):
            if student.roll_no == roll_no:
                confirm = input(f"Are you sure you want to delete {student.name}? (y/n): ")
                if confirm.lower() == 'y':
                    del self.students[i]
                    self.save_students()
                    print("✅ Student deleted.")
                return
        print("❌ Student not found.")

    def clear_database(self):
        confirm = input("⚠️ Are you sure you want to delete all records? (y/n): ")
        if confirm.lower() == 'y':
            self.students = []
            self.save_students()
            print("🧹 All records deleted.")

def main_menu():
    db = StudentDatabase()
    while True:
        print("\n🎓 Student Management System")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Clear All Records")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            db.add_student()
        elif choice == '2':
            db.view_students()
        elif choice == '3':
            db.search_student()
        elif choice == '4':
            db.update_student()
        elif choice == '5':
            db.delete_student()
        elif choice == '6':
            db.clear_database()
        elif choice == '7':
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()

import json
import os

class Student:
    def __init__(self, name, roll_no, marks, grade):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        self.grade = grade

    def to_dict(self):
        return {
            'name': self.name,
            'roll_no': self.roll_no,
            'marks': self.marks,
            'grade': self.grade
        }

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Roll No: {self.roll_no}\n"
                f"Marks: {self.marks}\n"
                f"Grade: {self.grade}")

class StudentDatabase:
    def __init__(self, filename='students.json'):
        self.filename = filename
        self.students = []
        self.load_students()

    def load_students(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.students = [Student(**item) for item in data]

    def save_students(self):
        with open(self.filename, 'w') as f:
            json.dump([s.to_dict() for s in self.students], f, indent=4)

    def add_student(self):
        print("\n📘 Add New Student")
        name = input("Enter Name: ")
        roll_no = input("Enter Roll Number: ")
        marks = float(input("Enter Marks: "))
        grade = input("Enter Grade: ")
        if any(s.roll_no == roll_no for s in self.students):
            print("❌ Student with this roll number already exists.")
            return
        student = Student(name, roll_no, marks, grade)
        self.students.append(student)
        self.save_students()
        print("✅ Student added successfully.")

    def view_students(self):
        print("\n📋 All Students")
        if not self.students:
            print("No records found.")
            return
        for idx, student in enumerate(self.students, 1):
            print(f"\nStudent #{idx}")
            print(student)

    def search_student(self):
        roll_no = input("\n🔍 Enter Roll Number to search: ")
        found = False
        for student in self.students:
            if student.roll_no == roll_no:
                print("\n📄 Student Found:")
                print(student)
                found = True
                break
        if not found:
            print("❌ Student not found.")

    def update_student(self):
        roll_no = input("\n✏️ Enter Roll Number to update: ")
        for student in self.students:
            if student.roll_no == roll_no:
                print("Leave blank to keep current value.")
                name = input(f"Enter New Name [{student.name}]: ") or student.name
                marks = input(f"Enter New Marks [{student.marks}]: ")
                grade = input(f"Enter New Grade [{student.grade}]: ") or student.grade

                student.name = name
                student.marks = float(marks) if marks else student.marks
                student.grade = grade
                self.save_students()
                print("✅ Student record updated.")
                return
        print("❌ Student not found.")

    def delete_student(self):
        roll_no = input("\n🗑️ Enter Roll Number to delete: ")
        for i, student in enumerate(self.students):
            if student.roll_no == roll_no:
                confirm = input(f"Are you sure you want to delete {student.name}? (y/n): ")
                if confirm.lower() == 'y':
                    del self.students[i]
                    self.save_students()
                    print("✅ Student deleted.")
                return
        print("❌ Student not found.")

    def clear_database(self):
        confirm = input("⚠️ Are you sure you want to delete all records? (y/n): ")
        if confirm.lower() == 'y':
            self.students = []
            self.save_students()
            print("🧹 All records deleted.")

def main_menu():
    db = StudentDatabase()
    while True:
        print("\n🎓 Student Management System")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Clear All Records")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            db.add_student()
        elif choice == '2':
            db.view_students()
        elif choice == '3':
            db.search_student()
        elif choice == '4':
            db.update_student()
        elif choice == '5':
            db.delete_student()
        elif choice == '6':
            db.clear_database()
        elif choice == '7':
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()


import json
import os

class Student:
    def __init__(self, name, roll_no, marks, grade):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        self.grade = grade

    def to_dict(self):
        return {
            'name': self.name,
            'roll_no': self.roll_no,
            'marks': self.marks,
            'grade': self.grade
        }

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Roll No: {self.roll_no}\n"
                f"Marks: {self.marks}\n"
                f"Grade: {self.grade}")

class StudentDatabase:
    def __init__(self, filename='students.json'):
        self.filename = filename
        self.students = []
        self.load_students()

    def load_students(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.students = [Student(**item) for item in data]

    def save_students(self):
        with open(self.filename, 'w') as f:
            json.dump([s.to_dict() for s in self.students], f, indent=4)

    def add_student(self):
        print("\n📘 Add New Student")
        name = input("Enter Name: ")
        roll_no = input("Enter Roll Number: ")
        marks = float(input("Enter Marks: "))
        grade = input("Enter Grade: ")
        if any(s.roll_no == roll_no for s in self.students):
            print("❌ Student with this roll number already exists.")
            return
        student = Student(name, roll_no, marks, grade)
        self.students.append(student)
        self.save_students()
        print("✅ Student added successfully.")

    def view_students(self):
        print("\n📋 All Students")
        if not self.students:
            print("No records found.")
            return
        for idx, student in enumerate(self.students, 1):
            print(f"\nStudent #{idx}")
            print(student)

    def search_student(self):
        roll_no = input("\n🔍 Enter Roll Number to search: ")
        found = False
        for student in self.students:
            if student.roll_no == roll_no:
                print("\n📄 Student Found:")
                print(student)
                found = True
                break
        if not found:
            print("❌ Student not found.")

    def update_student(self):
        roll_no = input("\n✏️ Enter Roll Number to update: ")
        for student in self.students:
            if student.roll_no == roll_no:
                print("Leave blank to keep current value.")
                name = input(f"Enter New Name [{student.name}]: ") or student.name
                marks = input(f"Enter New Marks [{student.marks}]: ")
                grade = input(f"Enter New Grade [{student.grade}]: ") or student.grade

                student.name = name
                student.marks = float(marks) if marks else student.marks
                student.grade = grade
                self.save_students()
                print("✅ Student record updated.")
                return
        print("❌ Student not found.")

    def delete_student(self):
        roll_no = input("\n🗑️ Enter Roll Number to delete: ")
        for i, student in enumerate(self.students):
            if student.roll_no == roll_no:
                confirm = input(f"Are you sure you want to delete {student.name}? (y/n): ")
                if confirm.lower() == 'y':
                    del self.students[i]
                    self.save_students()
                    print("✅ Student deleted.")
                return
        print("❌ Student not found.")

    def clear_database(self):
        confirm = input("⚠️ Are you sure you want to delete all records? (y/n): ")
        if confirm.lower() == 'y':
            self.students = []
            self.save_students()
            print("🧹 All records deleted.")

def main_menu():
    db = StudentDatabase()
    while True:
        print("\n🎓 Student Management System")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Clear All Records")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            db.add_student()
        elif choice == '2':
            db.view_students()
        elif choice == '3':
            db.search_student()
        elif choice == '4':
            db.update_student()
        elif choice == '5':
            db.delete_student()
        elif choice == '6':
            db.clear_database()
        elif choice == '7':
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()

import json
import os

class Student:
    def __init__(self, name, roll_no, marks, grade):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        self.grade = grade

    def to_dict(self):
        return {
            'name': self.name,
            'roll_no': self.roll_no,
            'marks': self.marks,
            'grade': self.grade
        }

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Roll No: {self.roll_no}\n"
                f"Marks: {self.marks}\n"
                f"Grade: {self.grade}")

class StudentDatabase:
    def __init__(self, filename='students.json'):
        self.filename = filename
        self.students = []
        self.load_students()

    def load_students(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.students = [Student(**item) for item in data]

    def save_students(self):
        with open(self.filename, 'w') as f:
            json.dump([s.to_dict() for s in self.students], f, indent=4)

    def add_student(self):
        print("\n📘 Add New Student")
        name = input("Enter Name: ")
        roll_no = input("Enter Roll Number: ")
        marks = float(input("Enter Marks: "))
        grade = input("Enter Grade: ")
        if any(s.roll_no == roll_no for s in self.students):
            print("❌ Student with this roll number already exists.")
            return
        student = Student(name, roll_no, marks, grade)
        self.students.append(student)
        self.save_students()
        print("✅ Student added successfully.")

    def view_students(self):
        print("\n📋 All Students")
        if not self.students:
            print("No records found.")
            return
        for idx, student in enumerate(self.students, 1):
            print(f"\nStudent #{idx}")
            print(student)

    def search_student(self):
        roll_no = input("\n🔍 Enter Roll Number to search: ")
        found = False
        for student in self.students:
            if student.roll_no == roll_no:
                print("\n📄 Student Found:")
                print(student)
                found = True
                break
        if not found:
            print("❌ Student not found.")

    def update_student(self):
        roll_no = input("\n✏️ Enter Roll Number to update: ")
        for student in self.students:
            if student.roll_no == roll_no:
                print("Leave blank to keep current value.")
                name = input(f"Enter New Name [{student.name}]: ") or student.name
                marks = input(f"Enter New Marks [{student.marks}]: ")
                grade = input(f"Enter New Grade [{student.grade}]: ") or student.grade

                student.name = name
                student.marks = float(marks) if marks else student.marks
                student.grade = grade
                self.save_students()
                print("✅ Student record updated.")
                return
        print("❌ Student not found.")

    def delete_student(self):
        roll_no = input("\n🗑️ Enter Roll Number to delete: ")
        for i, student in enumerate(self.students):
            if student.roll_no == roll_no:
                confirm = input(f"Are you sure you want to delete {student.name}? (y/n): ")
                if confirm.lower() == 'y':
                    del self.students[i]
                    self.save_students()
                    print("✅ Student deleted.")
                return
        print("❌ Student not found.")

    def clear_database(self):
        confirm = input("⚠️ Are you sure you want to delete all records? (y/n): ")
        if confirm.lower() == 'y':
            self.students = []
            self.save_students()
            print("🧹 All records deleted.")

def main_menu():
    db = StudentDatabase()
    while True:
        print("\n🎓 Student Management System")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Clear All Records")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            db.add_student()
        elif choice == '2':
            db.view_students()
        elif choice == '3':
            db.search_student()
        elif choice == '4':
            db.update_student()
        elif choice == '5':
            db.delete_student()
        elif choice == '6':
            db.clear_database()
        elif choice == '7':
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()
