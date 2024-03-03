from data import question_data
from question_model import Question
from quiz_brain import Quizbrain
c=0
question_bank=[]
for i in question_data:
    
    question_bank.append(Question(i["text"],i["answer"]))



quiz=Quizbrain(question_bank)
while quiz.still_has_Questions(): 
    quiz.next_question()

print("You have finished the Quiz")
print(f"Your final score is : {quiz.score}/{quiz.question_no}")