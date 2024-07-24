class NGUOI:
    def __init__(self,ma_dinh_danh,ho_ten):
        self.ma_dinh_danh=ma_dinh_danh
        self.ho_ten=ho_ten
        
    def describe(self):
        print(f"ma dinh danh:{self.ma_dinh_danh}, ho ten:{self.ho_ten}")
        
class NHANVIEN(NGUOI):
    def __init__(self,ma_dinh_danh,ho_ten,nam_sinh,he_so_luong):
        super().__init__(ma_dinh_danh,ho_ten)
        self.nam_sinh=nam_sinh
        self.he_so_luong=he_so_luong
    
    tien_phu_cap=100
    
    def describe(self):
        super().describe()
        print(f"nam sinh:{self.nam_sinh}, he so luong:{self.he_so_luong}")
        
    def tinhluong(self):
        return self.he_so_luong*1550+self.tien_phu_cap
    
def man():
    nhanvien_list =[]
    n=int(input("nhap so luong nhan vien:"))
    for i in range(n):
        print(f"\nNhập thông tin cho nhan vien thứ {i+1}:")
        ma_dinh_danh=float(input("nhap ma dinh danh:"))            
        ho_ten=input("nhap ho ten:")
        nam_sinh=int(input("nhap nam sinh:"))            
        he_so_luong=int(input("nhap he so luong:"))
        nv=NHANVIEN(ma_dinh_danh,ho_ten,nam_sinh,he_so_luong)
        nhanvien_list.append(nv)
    
    nhanvien_list.sort(key=lambda nv: nv.tinhluong())
    
    print("\nDanh sách nhân viên theo tinhluong từ thấp đến cao:")
    for nv in nhanvien_list:
        nv.describe()
        print(f"tinhluong: {nv.tinhluong()}\n")
    
    # Nhân viên có tinhluong cao nhất
    nv_max_luong = max(nhanvien_list, key=lambda nv: nv.tinhluong())
    print("Nhân viên có tinhluong cao nhất:")
    nv_max_luong.describe()
    print(f"tinhluong: {nv_max_luong.tinhluong()}\n")

man()