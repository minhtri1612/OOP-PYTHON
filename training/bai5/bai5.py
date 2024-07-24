class HANGHOA:
    def __init__(self,ma_hang,ten_hang):
        self.ma_hang=ma_hang
        self.ten_hang=ten_hang
        
    def describe(self):
        print(f"ma hang:{self.ma_hang}, ten hang:{self.ten_hang}")
        
class MAYTINH(HANGHOA):
    def __init__(self,ten_hang,ma_hang,nha_sx,nam_sx,gia_ban):
        super.__init__(ma_hang,ten_hang)
        self.nha_sx=nha_sx
        self.nam_sx=nam_sx
        self.gia_ban=gia_ban
    
    ty_le_khuyen_mai=10
    
    def describe(self):
        super().describe()
        print(f"nha san xuat:{self.nha_sx}, nam san xuat:{self.nam_sx}, gia ban niem yet:{self.gia_ban}")
        
    def gia_ban_thuc_te(self):
        return self.gia_ban- self.ty_le_khuyen_mai*self.gia_ban
    
