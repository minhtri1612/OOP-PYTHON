class DichVU:
    def __init__(self,ma_DV,ten_DV,gia_cuoc):
        self.ma_DV=ma_DV
        self.ten_DV=ten_DV
        self.gia_cuoc=gia_cuoc
        
    def laygiacuoc(self):
        return self.gia_cuoc        

    def describe(self):
        print(f"ma DV:{self.ma_DV}, ten DV:{self.ten_DV}, gia cuoc:{self.gia_cuoc}")
    
class Nguoi:
    def __init__(self,ho_ten,dia_chi,so_dt):
        self.ho_ten=ho_ten
        self.dia_chi=dia_chi
        self.so_dt=so_dt
        
    def describe(self):
        print(f"ho ten:{self.ho_ten}, dia chi:{self.dia_chi}, so dien thoai:{self.so_dt}")
        
class KhachHang(Nguoi):
    def __init__(self, ho_ten, dia_chi, so_dt, ds_dichvu):
        super().__init__(ho_ten, dia_chi, so_dt)
        self.ds_dichvu = ds_dichvu  # List of DichVU instances
        
    def describe(self):
        super().describe()
        print(f"So luong dich vu: {len(self.ds_dichvu)}")
        for dv in self.ds_dichvu:
            dv.describe()
        
    def TongGiaCuoc(self):
        return sum(dv.laygiacuoc() for dv in self.ds_dichvu)

# Example usage
dv1 = DichVU("DV01", "Dich vu 1", 100)
dv2 = DichVU("DV02", "Dich vu 2", 200)
dv3 = DichVU("DV03", "Dich vu 3", 300)

kh = KhachHang("Nguyen Van A", "123 Le Loi", "0123456789", [dv1, dv2, dv3])

kh.describe()
print(f"Tong gia cuoc: {kh.TongGiaCuoc()}")

