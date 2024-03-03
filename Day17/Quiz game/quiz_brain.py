
class Quizbrain:
    def __init__(self, q_list)  :
        self.question_no=0
        self.question_list=q_list
        self.score=0
    
    def still_has_Questions(self):
            if self.question_no < len(self.question_list):
                return True
            else:   
                return False
    
    

         
    def next_question(self):
        current_question=self.question_list[self.question_no]
        self.question_no+=1
        user_answer=input(f"Q{self.question_no}: {current_question.question} ? True/false : ")
        self.check_answer(user_answer,current_question.ans)

    def check_answer(self,userans,corect):
         if userans.lower()==corect.lower():
              self.score+=1
              print("Your are right")
         else:
            print("You are worong")            
         print(f"Correct answer was : {corect}.")
         print(f"your score is {self.score}/{self.question_no}")
         print("\n")
         
