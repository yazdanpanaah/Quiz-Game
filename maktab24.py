import random
import csv
import pandas

class Quize:   
    def __init__(self ,question , answer) :
        self.question = question
        self.answer = answer
    
    def check_answer(self , user_answer):
        if self.answer == user_answer:
            print('correct answer!!')
            return 'True'

        elif self.answer == '':
            return 'empty'
        else:
            print('wrong!!')
            return 'False'

    def __str__(self):
        return f'question is :{self.question}'


class TrueFalse(Quize):
    def __init__(self, question, answer):
        super().__init__(question, answer)
    
        
class MultipChoice(Quize):
    def __init__(self, question, answer):
        super().__init__(question, answer)
    def check_answer(self, user_answer):
        super().check_answer()

class ShortAnswer(Quize):
    def __init__(self, question, answer):
        super().__init__(question, answer)
    
    def check_answer(self, user_answer):
        if self.answer == user_answer.lower():
            print('correct answer!!')
            return 'True'

        elif self.answer == '':
            return 'empty'
        else:
            print('wrong!!')
            return 'False'
            

class Score:
    Q = 0
    correct = 0
    wrong = 0
    remain = 5
    def __init__(self):
        self.win_situation = False
        self.score = 0
        
    def count_score(self ,condition):
        
        if condition == 'True':
             print(self.__iadd__(10))
             Score.correct +=1

        elif condition == 'empty':
            print(self.score)

        else:
            print(self.__isub__(3))
            Score.wrong +=1

        
        csv_columns = ['Q' ,'correct', 'wrong','score','remaining']
        Score.remain -=1
        Score.Q +=1
        dict_data = [{'Q':Score.Q ,'correct':Score.correct, 'wrong':Score.wrong,'score':self.score,'remaining': Score.remain}]

        with open('score.csv','a') as f:
            writer = csv.DictWriter(f, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
                
        df = pandas.read_csv('score.csv', index_col='Q')
        print(df)
       
       
    
    def win_lose(self):
        if 40 <=self.score :
            print()
            print()
            print('----you win----')
        else:
            print()
            print()
            print('----you lose----')
            

    

    def __iadd__(self, other):
        self.score += other
        return self.score

    def __isub__(self, other):
        self.score -= other
        return self.score






data = [
    'what is capital of japan?\n>>>',
    "what's monkey favorit food?\n>>>",
    'What country won the very first FIFA World Cup in 1930?\n>>>',
    ' What year was the very first model of the iPhone released?\n>>>',
    'Which email service is owned by Microsoft?\n>>>',
    ' When did Jonas Brothers make their comeback to the music world?\n1.2015\n2.2011\n3.2019\n4.2010\n',
    ' What is the national language of Canada?\n1.canadian\n2.dutch\n3.english\n4.french\n',
    ' What is the national animal of Pakistan?\n1.wolf\n2.Peacock\n3.Markhor\n4.lion\n',
    ' What native country is Brazil?\n1.brazilian\n2.South American\n3.North American\n4.West American\n',
    'Brazil is the biggest producer of?\n1.rice\n2.Oil\n3.Coffee\n4.flower\n',
    'Marrakesh is the capital of Morocco:\n1.True\n2.False\n',
    'Facebook is not as popular as it used to be, it’s losing its audiences\n1.True\n2.False\n',
    'Almost (30%) of Americans are self-employed\n1.True\n2.False\n',
    'The Great Wall of China is visible from space.\n1.True\n2.False\n',
    'There are more ancient pyramids in Sudan than in Egypt.\n1.True\n2.False\n'


]
ans_data =['tokyo','banana','uruguye','2007','hotmail','3','2','3','3','3','2','2','1','2','1']

chosen_questions = []

short_ans = random.randint(0,4)
chosen_questions.append(data[short_ans])

multiple_choice = random.randint(5,9)
chosen_questions.append(data[multiple_choice])

True_false = random.randint(10,14)

chosen_questions.append(data[True_false])

for i in range(2):
    while True:
        other_question = random.choice(data)
        if other_question not in chosen_questions:
            chosen_questions.append(other_question)
            break

score_obj = Score()

for i in range(len(data)):
    if data[i] in chosen_questions:
        if 0<= i < 5:
            obj1 = ShortAnswer(data[i],ans_data[i])
            while True:
                user_answer = input(data[i])
                if user_answer.isalpha():
                        break
                else:
                    print('just a word not num!!')
                    
            check = obj1.check_answer(user_answer)
            if check == 'True':
                score_obj.count_score('True')
            elif check == 'empty':
                score_obj.count_score('empty')
            else:
                score_obj.count_score('False')
            
        
        elif 5 <= i <10:
            obj1 = Quize(data[i],ans_data[i])
            while True:
                user_answer = input(data[i])
                if user_answer.isnumeric():
                    if 1<= int(user_answer) <=4:
                        break
                    else:
                        print('pick a number from 1 to 4')
                else:
                    print('just integer!!')
            check = obj1.check_answer(user_answer)
            if check == 'True':
                score_obj.count_score('True')
            elif check == 'empty':
                score_obj.count_score('empty')
            else:
                score_obj.count_score('False')
          
        
        elif 10<= i <15:
            obj1 =Quize(data[i],ans_data[i])
            while True:
                user_answer = input(data[i])
                if user_answer.isnumeric():
                    if 1<= int(user_answer) <3:
                        break
                    else:
                        print('pick a number from 1 to 4')
                else:
                    print('just integer!!')
                    
            check = obj1.check_answer(user_answer)
            if check == 'True':
                score_obj.count_score('True')
            elif check == 'empty':
                score_obj.count_score('empty')
            else:
                score_obj.count_score('False')
              

            
score_obj.win_lose()







