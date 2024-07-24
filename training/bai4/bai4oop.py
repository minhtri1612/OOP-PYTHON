class DATE:
    def __init__(self,ngay,thang,nam):
        self.ngay=ngay
        self.thang=thang
        self.nam=nam
    
    def describe(self):
        print(f"ngay:{self.ngay},thang:{self.thang},nam:{self.nam}")
    
class CANBO(DATE):
    def __init__(self,ma,ten,luong_co_ban,ngay,thang,nam):
        super().__init__(ngay,thang,nam)
        self.ma=ma
        self.ten=ten
        self.luong_co_ban=luong_co_ban
        
    tien_phu_cap=300
    
    def describe(self):
        super().describe()
        print(f"ma can bo:{self.ma},ten can bo:{self.ten}")
    
    def tinh_luong(self):
        return self.luong_co_ban + self.tien_phu_cap

A1=CANBO(123,"tri",1000,1,5,222)
A2=CANBO(324,"Dat",300,2,3,78)
A3=CANBO(898,"thuyt",330,2,3,43)
employee=[A1,A2,A3]


cc=sorted(employee, key=lambda nv: nv.tinh_luong())
for i in cc:
    i.describe()
    print(f"Tinh luong: {i.tinh_luong()}")



    
