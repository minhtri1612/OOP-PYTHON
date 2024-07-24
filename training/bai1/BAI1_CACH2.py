class PhuongTienGiaoThong:
    def __init__(self, hang_sx, phuong_tien, nam_sx, max_speed):
        self.hang_sx = hang_sx
        self.phuong_tien = phuong_tien
        self.nam_sx = nam_sx
        self.max_speed = max_speed

    def describe(self):
        print(f"Hãng sản xuất: {self.hang_sx}, tên phương tiện: {self.phuong_tien}, năm sản xuất: {self.nam_sx}, vận tốc tối đa: {self.max_speed} km/h")

class Oto(PhuongTienGiaoThong):
    def __init__(self, hang_sx, phuong_tien, nam_sx, max_speed, cho_ngoi, dong_co):
        super().__init__(hang_sx, phuong_tien, nam_sx, max_speed)
        self.cho_ngoi = cho_ngoi
        self.dong_co = dong_co

    def describe(self):
        super().describe()  # Call the describe method from the parent class to print common attributes
        print(f"Ô tô có số chỗ ngồi: {self.cho_ngoi}, kiểu động cơ của ô tô: {self.dong_co}")

    def speed_co_so(self):
        return self.max_speed / self.cho_ngoi

    def __lt__(self, other):
        if not isinstance(other, Oto):
            return NotImplemented
        return self.speed_co_so() < other.speed_co_so()

def main():
    oto_list = []
    n = int(input("Nhập số lượng ô tô cần tạo: "))

    for i in range(n):
        print(f"\nNhập thông tin cho ô tô thứ {i+1}:")
        hang_sx = input("Hãng sản xuất: ")
        phuong_tien = input("Tên phương tiện: ")
        nam_sx = int(input("Năm sản xuất: "))
        max_speed = float(input("Vận tốc tối đa (km/h): "))
        cho_ngoi = int(input("Số chỗ ngồi: "))
        dong_co = input("Kiểu động cơ: ")

        oto = Oto(hang_sx, phuong_tien, nam_sx, max_speed, cho_ngoi, dong_co)
        oto_list.append(oto)

    for oto in oto_list:
        oto.describe()

    if len(oto_list) >= 2:
        for i in range(len(oto_list)):
            for j in range(i + 1, len(oto_list)):
                print(f"\nSo sánh tốc độ cơ sở của ô tô {i+1} và ô tô {j+1}:")
                print(f"Ô tô {i+1} có tốc độ cơ sở thấp hơn ô tô {j+1}: {oto_list[i] < oto_list[j]}")

if __name__ == "__main__":
    main()
