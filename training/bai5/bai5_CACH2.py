class HANGHOA:
    def __init__(self,ma_hang,ten_hang):
        self.ma_hang=ma_hang
        self.ten_hang=ten_hang
        
    def describe(self):
        print(f"ma hang:{self.ma_hang}, ten hang:{self.ten_hang}")
        
class MAYTINH(HANGHOA):
    def __init__(self,ma_hang,ten_hang,nha_sx,nam_sx,gia_ban):
        super().__init__(ma_hang,ten_hang)
        self.nha_sx=nha_sx
        self.nam_sx=nam_sx
        self.gia_ban=gia_ban
    
    ty_le_khuyen_mai=0.5
    
    def describe(self):
        print(f"nha san xuat:{self.nha_sx}, nam san xuat:{self.nam_sx}, gia ban niem yet:{self.gia_ban}")
        
    def gia_ban_thuc_te(self):
        return self.gia_ban-self.gia_ban*self.ty_le_khuyen_mai
    
def man():
    List_MAYTINH=[]
    n=int(input("Nhap so luong MAYTINH:"))
    for i in range(n):
        print(f"thong tin cua MAYTINH thu {i+1}:")
        ma_hang=input("nhap ten ma hang:")
        ten_hang=input("nhap ten hang:")
        nha_sx=input("nhap ten nha san xuat:")
        nam_sx=int(input("nhap nam san xuat:"))
        gia_ban=int(input("nhap gia ban:"))
        COMPUTER=MAYTINH(ma_hang,ten_hang,nha_sx,nam_sx,gia_ban)
        List_MAYTINH.append(COMPUTER)
        
    List_MAYTINH.sort(key=lambda COMPUTER:COMPUTER.gia_ban_thuc_te())
    for COMPUTER in List_MAYTINH:
        COMPUTER.describe()
        print(f"gia ban thuc te:{COMPUTER.gia_ban_thuc_te()}")
        
        COMPUTER_MIN=max(List_MAYTINH,key=lambda COMPUTER:COMPUTER.tinhluong())
        print(f"may tinh thap nhat:{COMPUTER_MIN.gia_ban_thuc_te()}")
        COMPUTER_MIN.describe()
        print(f"tinh gia ban: {COMPUTER_MIN.gia_ban_thuc_te()}\n")
        
man()