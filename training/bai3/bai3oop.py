class NGUOI:
    def __init__(self,ma_dinh_danh,ho_ten):
        self.ma_dinh_danh=ma_dinh_danh
        self.ho_ten=ho_ten
    def describe(self):
        print(f"mã định danh:{self.ma_dinh_danh}, họ và tên:{self.ho_ten}")
        
class NHANVIEN(NGUOI):
    def __init__(self,ma_dinh_danh,ho_ten,nam_sinh,he_so_luong):
        super().__init__(ma_dinh_danh,ho_ten)
        self.nam_sinh=nam_sinh
        self.he_so_luong=he_so_luong
    
    phu_cap=400
    
    def describe(self):
        super().describe()
        print(f"nam sinh:{self.nam_sinh}, he so luong:{self.he_so_luong}")
        
    def tinh_luong(self):
        return self.he_so_luong*1550 +self.phu_cap
    
nv1 = NHANVIEN(1, "Minh Tri", 1990, 3)
nv2 = NHANVIEN(2, "Thanh Dat", 1988, 2)
nv3 = NHANVIEN(3, "Ngoc Lan", 1992, 4)

# Create a list of employees
employees = [nv1, nv2, nv3]

# Find the employee with the highest salary
highest_salary_employee = max(employees, key=lambda nv: nv.tinh_luong())

# Print the details of the employee with the highest salary
print("Nhân viên có lương cao nhất:")
highest_salary_employee.describe()
print(f"Lương: {highest_salary_employee.tinh_luong()}")
