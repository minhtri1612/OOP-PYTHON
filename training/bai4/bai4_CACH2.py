class DATE:
    def __init__(self,ngay,thang,nam):
        self.thang=thang
        self.ngay=ngay
        self.nam=nam
        
    def describe(self):
        print(f"ngay:{self.ngay}, thang:{self.thang}, nam:{self.nam}")
        
class CANBO(DATE):
    def __init__(self,ngay,thang,nam,ma_can_bo,ten_can_bo,luong_co_ban):
        super().__init__(ngay,thang,nam)
        self.ma_can_bo=ma_can_bo
        self.ten_can_bo=ten_can_bo
        self.luong_co_ban=luong_co_ban
        
    tien_phu_cap=1000
    
    def describe(self):
        super().describe()
        print(f"ten can bo:{self.ten_can_bo}, ma can bo:{self.ma_can_bo}")
        
    def tinh_luong(self):
        return self.luong_co_ban+self.tien_phu_cap
    
def man():
    CANBO_LIST=[]
    n=int(input("nhap so luong doi tuong CAN BO:"))
    for i in range(n):
        print(f"nhap thong tin khach hang cua {i+1}:")
        ngay=int(input("nhap ngay:"))
        thang=int(input("nhap thang:"))
        nam=int(input("nhap nam:"))
        ma_can_bo=input("nhap ma CANBO:")
        ten_can_bo=input("nhap ten CANBO:")
        luong_co_ban=int(input("nhap luong co ban:"))
        CB=CANBO(ngay,thang,nam,ma_can_bo,ten_can_bo,luong_co_ban)
        CANBO_LIST.append(CB)
        
    CANBO_LIST.sort(key=lambda CB: CB.tinh_luong())
    
    for CB in CANBO_LIST:
        CB.describe()
        print(f"tinh luong:{CB.tinhluong()}")
        
    CANBO_MAX_LUONG=max(CANBO_LIST,key=lambda CB: CB.tinh_luong())
    print(f"can bo luong cao nhat: {CANBO_MAX_LUONG.tinhluong()}\n")
    CANBO_MAX_LUONG.describe()
    print(f"tinh luong: {CANBO_MAX_LUONG.tinh_luong()}\n")

man()