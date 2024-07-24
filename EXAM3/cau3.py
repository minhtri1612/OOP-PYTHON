class Participant:
    def __init__(self,par_name,par_year,par_field):
        self.par_name=par_name
        self.par_year=par_year
        self.par_field=par_field
    
    def describe(self):
        print(f"name={self.par_name},year={self.par_year},field={self.par_field}")

class Mentor:
    def __init__(self,men_name,men_year,men_subject):
        self.men_name=men_name
        self.men_year=men_year
        self.men_subject=men_subject
        
    def describe(self):
        print(f"name={self.men_name},year={self.men_year},subject={self.men_subject}")
    
class Coordinator:
    def __init__(self,cor_name,cor_year,cor_division):
        self.cor_name=cor_name
        self.cor_year=cor_year
        self.cor_division=cor_division
        
    def describe(self):
        print(f"name={self.cor_name},year={self.cor_year},division={self.cor_division}")
class Society:
    def __init__(self,name):
        self.name=name
        self.members=[]
    
    def addMember(self,member):
        self.members.append(member)
        
    def describe(self):
        print(f"Society Name: {self.name}")
        print("Members in the Library:")
        for i in self.members:
            i.describe()
    
    def countCoordinators(self):
        count = 0
        for member in self.members:
            if isinstance(member, Coordinator):
                count += 1
        return count
    
    def sortBirthYear(self):
        coordinators = [member for member in self.members if isinstance(member, Coordinator)]
        coordinators.sort(key=lambda c: c.cor_year)
        other_members = [member for member in self.members if not isinstance(member, Coordinator)]
        self.members = other_members + coordinators
            
    
    
pa=Participant("Alice",1995,"Art")
pa.describe()
mentor1=Mentor("Bob",1980,"Math")
mentor1.describe()
mentor2=Mentor("Carol",1970,"Science")
mentor2.describe()
coordinator1=Coordinator("David",1960,"Events")
coordinator1.describe()
coordinator2=Coordinator("Thomas",1980,"Logistics")
coordinator2.describe()
coordinator3=Coordinator("minh tri",1980,"CSE")
coordinator3.describe()
society1=Society("society1")
society1.addMember(mentor1)
society1.addMember(mentor2)
society1.addMember(coordinator1)
society1.addMember(coordinator2)
society1.addMember(coordinator3)
society1.describe()
society1.sortBirthYear()
society1.describe()
num_coordinators = society1.countCoordinators()
print(f"Number of Coordinators: {num_coordinators}")