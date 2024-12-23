def get_user_input():
    while True:
        try:
            counts = int(input("Số tab mở để lấy dữ liệu: "))
            return counts
        except ValueError:
            print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")
