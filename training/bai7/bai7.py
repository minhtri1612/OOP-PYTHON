class SACH:
    def __init__(self,ma_sach,name_sach):
        self.ma_sach=ma_sach
        self.name_sach=name_sach
        
    def describe(self):
        print(f"ma sach:{self.ma_sach}, ten sach:{self.name_sach}")
    
class MUONTRA(SACH):
    def __init__(self,ma_sach,name_sach,ma_doc_gia,so_luong):
        super().__init__(ma_sach,name_sach)
        self.ma_doc_gia=ma_doc_gia
        self.so_luong=so_luong
        
    phi_cuoc=100

    def describe(self):
        print(f"ma doc gia:{self.ma_doc_gia}, so luong:{self.so_luong}")
        
    def sotien_cuoc(self):
        return self.so_luong*self.phi_cuoc
    
sach1=MUONTRA(123,"tuoi tho",213,5)
sach2=MUONTRA(415,"tom",34,10)
sach3=MUONTRA(747,"and",76,3)
sach4=MUONTRA(356,"jerry",16,8)
sach5=MUONTRA(198,"dkmm",98,3)
List_muontra=[sach1,sach2,sach3,sach4,sach5]

cc=sorted(List_muontra, key=lambda x: x.sotien_cuoc())
for i in cc:
    if i.sotien_cuoc() >10:
        i.describe()
        
MAX_muontra=max(List_muontra, key=lambda x: x.sotien_cuoc())
print(f"tien cuoc nhieu nhat:{MAX_muontra.sotien_cuoc()}")
