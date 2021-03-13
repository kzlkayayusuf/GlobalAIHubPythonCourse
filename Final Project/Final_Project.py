
"""
Created on Fri Mar 12 22:44:29 2021

@author: kzlkayayusuf
"""

class Question:
    def __init__(self,text,choices,answer):
        self.text= text
        self.choices = choices
        self.answer= answer
        
    def checkAnswer(self,answer):
        return self.answer == answer
    

class Quiz:
    def __init__(self,questions):
        self.questions= questions
        self.score = 0
        self.questionIndex = 0
        self.rightAnswer = 0
        
    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        question= self.getQuestion()
        print(f'Soru {self.questionIndex +1}: {question.text}')
        
        for q in question.choices:
            print('-' + q)
            
        answer = input('Yanıtınız : ')
        if (answer == " " or answer==""):
            print("Bu soruya cevap vermek istemediğinizden eminmisiniz?")
            self.yesOrNo()
        else:
            self.guess(answer)
            self.loadQuestion()
        
    def yesOrNo(self):
        yesOrNo = input('Evet mi Hayır mı : ')
        if(yesOrNo == 'Evet'):
            answer = " "
            self.guess(answer)
            self.loadQuestion()
        elif(yesOrNo == 'Hayır'):
            answer = input('Yanıtınız : ')
            if (answer == " " or answer==""):
                print("Bu soruya cevap vermek istemediğinizden eminmisiniz?")
                self.yesOrNo()
            else:
                self.guess(answer)
                self.loadQuestion()
        else:
            print("Büyük Küçük harf kullanımına dikkat ederek tekrar yazınız.")
            self.yesOrNo()
                
    def guess(self,answer):
        question= self.getQuestion()
        
        if question.checkAnswer(answer):
            self.score +=10
            self.rightAnswer+=1
            print("Yanıtınız Doğru :)")
        elif(answer == " "):
            print(f"Soruyu cevaplamadınız, Doğru Cevap: {question.answer}")
        else:
            print(f"Yanıtınız Yanlış :(, Doğru Cevap: {question.answer}")
        self.questionIndex += 1
    def loadQuestion(self):
        if len(self.questions)== self.questionIndex:
            self.showScore()
            self.displayProgress()
        else:
            self.displayProgress()
            self.displayQuestion()
            
    def showScore(self):
        print('Puanınız : ', self.score)
        
    def displayProgress(self):
        totalQuestion= len(self.questions)
        questionNumber = self.questionIndex + 1
        
        if questionNumber>totalQuestion:
            print('Quiz bitti.')
            if (self.rightAnswer<=5):
                print("Başarısız Oldunuz! :(")
            else:
                print("Tebrikler, Geçtiniz :)")
        else:
            print(f'Toplam {totalQuestion} sorunun {questionNumber}.sorusu '.center(70,'*'))
            
questionsAnswers ={
    "Türk Tarihinde 26 Ağustos 1071 yılında hangi olay meydana gelmiştir?":
        [['Malazgirt Savaşı','Pasinler Savaşı','Dandanakan Savaşı','Miryokefalon Savaşı'],
        "Malazgirt Savaşı"],
    "Osmanlı Devleti, İttifak Devletlerinin yanında hangi savaşa girmek zorunda kalmıştır?":
        [['1. Dünya Savaşı','2. Dünya Savaşı','1. İnönü Savaşı','Sakarya Savaşı'],
         "1. Dünya Savaşı"],
    "1. Dünya Savaşı sonrası işgal edilen yerlerden düşmanı temizlemek amacıyla doğan teşkilatın adı nedir?":
        [['Çelik Kuvvet','Kuva-i Milliye','Hat-ı Hümayün','Sath-ı Milliye'],
        "Kuva-i Milliye"],
    "Bağımsızlığını kazanmak için, Osmanlılar\'a ilk önce isyan etmiş millet hangisidir?":
        [['Arnavutlar','Bulgarlar','Yunanlılar','Sırplar'],
         "Sırplar"],
    "1876 anayasasının adı nedir?":
        [['Gülhane Hatt-i Hümayunu','Takrir-i Sükun','Kanun-i Esasi','Tanzimat Fermanı'],
         "Kanun-i Esasi"],
    "Arap Endülüs Emevi devleti hangi ülkede kurulmuştur?":
        [['Cezayir','İspanya','Mısır','Suudi Arabistan'],
         "İspanya"],
    "Atatürkçülüğün durağan bir düşünce olmaması aşağıdaki ilkelerden hangisine dayanmaktadır?":
        [['İnkılapçılık','Milliyetçilik','Devletçilik','Halkçılık'],
         "İnkılapçılık"],
    "Mudanya Ateşkes Antlaşması hangi tarihte imzalanmıştır?":
        [['1938','1918','1902','1922'],
         "1922"],
    "Amerika kıtası kaç yılında keşfedilmiştir?":
        [['1299','1583','1376','1492'],
         "1492"],
    "Yakın Çağ\'ın başlamasına neden olan olay hangisidir?":
        [['Yazının İcadı','İstanbul`un Fethi','Fransız İhtilali','Paranın İcadı'],
         "Fransız İhtilali"]
        }

questions= list()

for text,choicesAnswer in questionsAnswers.items():
    questions.append(Question(text,choicesAnswer[0],choicesAnswer[1]))
          

quiz=Quiz(questions)
quiz.loadQuestion()
