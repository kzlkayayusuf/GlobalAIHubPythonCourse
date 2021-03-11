
"""
Created on Thu Mar 11 14:20:08 2021

@author: kzlkayayusuf
"""

#CV Application

person1Cv = {
    "First Name": "Yusuf",
    "Last Name": "KIZILKAYA",
    "Age":26,
    "E-mail": "kzlkayayusuf@outlook.com",
    "Graduated": "Erzurum Technical University ",
    "Department": "Electric-Electronic Engineering",
    "Job Experience": "2 years"
    }
person2Cv = {
    "First Name": "Yaser",
    "Last Name": "ÇETİNKAYA",
    "Age":22,
    "E-mail": "cetinkayayaser@outlook.com",
    "Graduated": "Atatürk University",
    "Department": "Econometrist ",
    "Job Experience": "3 years"
    }
person3Cv = {
    "First Name": "Ali",
    "Last Name": "KAPLAN",
    "Age":28,
    "E-mail": "kaplanali@outlook.com",
    "Graduated": "Star Technical University ",
    "Department": "Mechanical engineer ",
    "Job Experience": "5 years"
    }
person4Cv = {
    "First Name": "Ayşe",
    "Last Name": "SEVER",
    "Age":24,
    "E-mail": "severay@outlook.com",
    "Graduated": "Hacettepe University",
    "Department": "Faculty Of Medicine",
    "Job Experience": "1 years"
    }
person5Cv = {
    "First Name": "Meral",
    "Last Name": "ÇAKAL",
    "Age":36,
    "E-mail": "cakalmeral@outlook.com",
    "Graduated": "Middle East Technical University",
    "Department": "Computer Engineering",
    "Job Experience": "7 years"
    }
CV = {
      "Person 1": person1Cv,
      "Person 2": person2Cv,
      "Person 3": person3Cv,
      "Person 4": person4Cv,
      "Person 5": person5Cv
      }

for person,cv in CV.items():
    print(f"{person}'s CV: ")
    for i in cv:
        info = cv[i]
        print(f"{i} : {info}")
    print("*************************************************")
    
    

        
  
    