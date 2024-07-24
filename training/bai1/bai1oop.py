class PhuongTienGiaoThong:
    def __init__(self, hang_sx, phuong_tien, nam_sx, max_speed):
        self.hang_sx = hang_sx
        self.phuong_tien = phuong_tien
        self.nam_sx = nam_sx
        self.max_speed = max_speed

    def describe(self):
        print(f"Hãng sản xuất: {self.hang_sx}, tên phương tiện: {self.phuong_tien}, năm sản xuất: {self.nam_sx}, vận tốc tối đa: {self.max_speed}")

class Oto(PhuongTienGiaoThong):
    def __init__(self, hang_sx, phuong_tien, nam_sx, max_speed, van_toc_co_so, cho_ngoi, dong_co):
        super().__init__(hang_sx, phuong_tien, nam_sx, max_speed)
        self.cho_ngoi = cho_ngoi
        self.dong_co = dong_co
        self.van_toc_co_so = van_toc_co_so

    def describe(self):
        super().describe()  # Call the describe method from the parent class to print common attributes
        print(f"Ô tô có số chỗ ngồi: {self.cho_ngoi}, kiểu động cơ của ô tô: {self.dong_co}")

    def speed_co_so(self):
        return self.max_speed / self.cho_ngoi

    def __lt__(self, other):
        if not isinstance(other, Oto):
            return NotImplemented
        return self.speed_co_so() < other.speed_co_so()

# Example usage
oto1 = Oto("Toyota", "Camry", 2020, 240, 100, 5, "V6")
oto2 = Oto("Honda", "Accord", 2019, 220, 95, 4, "I4")

oto1.describe()
oto2.describe()

print("Ô tô 1 có tốc độ cơ sở thấp hơn ô tô 2:", oto1 < oto2)
