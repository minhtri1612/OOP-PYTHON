class NGUOI:
    def __init__(self,ma_dinh_danh,ho_ten):
        self.ma_dinh_danh=ma_dinh_danh
        self.ho_ten=ho_ten
        
    def describe(self):
        print(f"ma dinh danh:{self.ma_dinh_danh}, ho va ten:{self.ho_ten}")
        
class NHANVIEN(NGUOI):
    def __init__(self,ma_dinh_danh,ho_ten,nam_sinh,he_so_luong):
        super().__init__(ma_dinh_danh,ho_ten)
        self.nam_sinh=nam_sinh
        self.he_so_luong=he_so_luong
        
    tien_phu_cap=100
    
    def describe(self):
        super().describe()
        print(f"he so luong:{self.he_so_luong}, nam sinh:{self.nam_sinh}")
        
    def tinh_luong(self):
        return self.he_so_luong*1550 +self.tien_phu_cap
    
    def __gt__(self,other):
        return self.tinh_luong() >other.tinh_luong()
    
def main():
    NHANVIEN_LIST=[]
    n=int(input("nhap so luong nhan vien:"))
    for i in range(n):
        print(f"\nNhập thông tin cho nhan vien thứ {i+1}:")
        ma_dinh_danh=float(input("nhap ma dinh danh:"))            
        ho_ten=input("nhap ho ten:")
        nam_sinh=int(input("nhap nam sinh:"))            
        he_so_luong=int(input("nhap he so luong:"))
        nv=NHANVIEN(ma_dinh_danh,ho_ten,nam_sinh,he_so_luong)
        NHANVIEN_LIST.append(nv)
            
    for i in NHANVIEN_LIST:
        i.describe()
            
    if len(NHANVIEN_LIST) >= 2:
        for i in range(len(NHANVIEN_LIST)):
            for j in range(i + 1, len(NHANVIEN_LIST)):
                print(f"\nSo sánh nhan vien {i+1} và nhan vien {j+1}:")
                print(f"nhan vien {i+1} có  luong cao hơn nhan vien{j+1}: {NHANVIEN_LIST[i] > NHANVIEN_LIST[j]}")

if __name__ == "__main__":
    main()