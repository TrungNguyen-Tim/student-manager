def classify_student(avg_score):
    if avg_score >= 8:
        return "Giỏi"
    elif avg_score >= 6.5:
        return "Khá"
    elif avg_score >= 5:
        return "Trung bình"
    else:
        return "Yếu"
    
def check_pass(avg):
    return "PASS!" if avg >= 5 else "FAIL!"
