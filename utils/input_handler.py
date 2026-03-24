from .calculator import calculate_average
from .classifier import classify_student
# Import từ module trong cùng package


def input_number_of_students():
    while True:
        # Kiểm tra xem số lượng sinh viên có hợp lệ không(Kiểu dữ liệu số và lớn hơn 0)
        try:
            n = int(input("Có bao nhiêu học sinh? "))
            # Kiểm tra xem dữ liệu người dùng nhập có phải là số âm
            if n > 0:
                return n
            else:
                print("Phải > 0")
        # Báo lỗi khi người dùng không nhập dữ liệu dạng số
        except ValueError:
            print("Vui lòng nhập số")


def input_score(subject):
    while True:
        # Kiểm tra xem người dùng có nhập đúng kiểu dữ liệu số
        try:
            score = float(input(f"Nhập điểm {subject}: "))
            # Kiểm tra nếu số điểm nhỏ hơn 0 hoặc lớn hơn 10
            if 0 <= score <=10:
                return score
            else:
                print("Điểm phải từ 0 đến 10")
        # Báo lỗi nếu người dùng không nhập dữ liệu số
        except ValueError:
            print("Vui lòng nhập số!")
            

def input_student():
    # Kiểm tra nếu tên sinh viên bị để trống
    while True:
        name = input("Nhập tên sinh viên: ").strip()
        if name:
            break
        else:
            print("Không để trống tên học sinh")
    math = input_score("toán")
    eng = input_score("anh")
    it = input_score("tin")
    avg = calculate_average(math, eng, it)
    return {
        "name": name, 
        "math": math, 
        "eng": eng,
        "it": it,
        "avg": avg,
        "classification": classify_student(avg)
    }