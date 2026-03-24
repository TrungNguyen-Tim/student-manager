from utils.calculator import calculate_average
from utils.classifier import classify_student, check_pass
from utils.input_handler import input_student, input_score, input_number_of_students


def main():
    students = []
    n = input_number_of_students()
    # Nhập thông tin sinh viên vào list
    for i in range(n):
        print(f"Sinh viên thứ {i+1}:")
        students.append(input_student())
    # In thông tin sinh viên
    for student in students:
        print(student["name"], student["avg"], student["classification"], check_pass(student["avg"]), sep = " - ")
        

if __name__ == "__main__":
    main()