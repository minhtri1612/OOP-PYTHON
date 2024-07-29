class DATE:
    def __init__(self,ngay,thang,nam):
        self.ngay=ngay
        self.thang=thang
        self.nam=nam
    
    def getDay(self):
        return self.ngay

    def getMonth(self):
        return self.thang
    
    def getYear(self):
        return self.nam
    
    def describe(self):
        print(f"ngay:{self.ngay}, thang:{self.thang}, nam:{self.nam}")
        
class MUONTRA(DATE):
    def __init__(self,ngay,thang,nam,doc_gia,sach,so_luong):
        super().__init__(ngay,thang,nam)
        self.doc_gia=doc_gia
        self.sach=sach
        self.so_luong=so_luong
        
    phi_cuoc=100
    
    def describe(self):
        super().describe()
        print(f"ma doc gia:{self.doc_gia}, ten sach:{self.sach}")
    
    def so_tien_cuoc(self):
        return  self.so_luong*self.phi_cuoc
DANH_SACH=[]
a1= MUONTRA(16,12,2004,"minh tri","tuoi tho du doi",4)
a1.describe()
print("so tien muon sach cua a1:",a1.so_tien_cuoc())

a2= MUONTRA(3,1,2023,"bao ngoc","C++",6)
a2.describe()
print("so tien muon sach cua a2:",a2.so_tien_cuoc())

a3= MUONTRA(16,12,2011,"duc huy","NETOWORK",7)
a3.describe()
print("so tien muon sach cua 13:",a3.so_tien_cuoc())

a4= MUONTRA(16,12,2034,"minh chau","JAVA AND PYTHON",10)
a4.describe()
print("so tien muon sach cua a4:",a4.so_tien_cuoc())
DANH_SACH.extend([a1, a2, a3, a4])
print("doc gia muon truoc ngay 1/1/2020:")
for i in DANH_SACH:
    if i.getYear() < 2020:
        i.describe()
        
MAX_TIEN_CUOC=max(DANH_SACH, key=lambda x:x.so_tien_cuoc())
print(f"tien cuoc nhieu nhat:{MAX_TIEN_CUOC.so_tien_cuoc()}")