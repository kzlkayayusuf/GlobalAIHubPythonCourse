
"""
Created on Thu Mar 11 21:54:14 2021

@author: kzlkayayusuf
"""

"""
students fonksiyonu ile öğrenciler isimlerini ve ara sınav notunu,proje notunu
ve final notunu girerler. for döngüsü ile istenilen 5 öğrenci oluşturuldu.
calculate fonksiyonu ile girilen notlar hesaplanarak geçme notu hesaplanır.
studentsInfo dictionary öğrencilerin isimlerini key olarak ve notlarını value olarak 
tutmamıza olanak sağlar.
passingGrade listesi ile öğrencilerin isimleri ve karşılarında hesaplanan geçme notunu
tutmamıza yarar.
passinGrade listesi içindeki notları küçükten büyüğe sıralamak için sorted metodunu 
kullandım ve bu notları soruda istenilen şekilde büyükten küçüğe doğru sıralamak için 
sorted metodu içinde reverse yani ters çeviri True yaparak büyükten küçüğe sıralamış oldum


"""
studentsInfo = dict()
passingGrade= list()

def students():
    fullName = input("Please type your name: ")
    midtermGrade = float(input("Please enter midterm grade: ")) 
    projectGrade = float(input("Please enter project grade: ")) 
    finalGrade = float(input("Please enter final grade: "))
    studentsInfo[fullName]= [midtermGrade,projectGrade,finalGrade]
def calculate():
    for k,v in studentsInfo.items():
        passingGrade.append(f"{((v[0]*(0.3)) + (v[1]*(0.3)) + (v[2]*(0.4)))}={k} ") 
        
        

for i in range(0,5):
    students()



calculate()

print(studentsInfo)
print(passingGrade)
print(sorted(passingGrade,reverse=True))


