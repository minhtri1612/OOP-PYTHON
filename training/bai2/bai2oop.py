class NGUOI:
    def __init__(self, ma_dinh_danh, ho_ten):
        self.ma_dinh_danh = ma_dinh_danh
        self.ho_ten = ho_ten
    
    def describe(self):
        print(f"Mã định danh người: {self.ma_dinh_danh}, họ và tên: {self.ho_ten}")
        
class NHANVIEN(NGUOI):
    tien_phu_cap = 400
    
    def __init__(self, nam_sinh, he_so_luong, ma_dinh_danh, ho_ten):
        super().__init__(ma_dinh_danh, ho_ten)
        self.nam_sinh = nam_sinh
        self.he_so_luong = he_so_luong
    
    def describe(self):
        super().describe()  # Call the describe method from the parent class to print common attributes
        print(f"Năm sinh: {self.nam_sinh}, hệ số lương: {self.he_so_luong}")
            
    def tinhluong(self):
        return self.he_so_luong * 1550 + self.tien_phu_cap

# Example usage
nv1 = NHANVIEN(1990, 300, 23, "Minh Tri")
nv2 = NHANVIEN(1988, 200, 24, "Thanh Dat")

nv1.describe()
nv2.describe()

print(f"Lương của nv1: {nv1.tinhluong()}")
print(f"Lương của nv2: {nv2.tinhluong()}")
