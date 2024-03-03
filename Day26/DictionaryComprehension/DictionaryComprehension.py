from random import randint          
studentList=["Vishal","Amit","arun",'aman',"Abhi","salman","katara","Aang"]

student_dic={student: randint(1,100) for student in studentList}
print(student_dic)
# {key:value for (key,value) in dic.items()}
pass_student_dic={student: score for  student ,  score in student_dic.items() if score>50}
print(pass_student_dic)