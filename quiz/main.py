from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random
#  question bank
question_bank = [] # container that hold qestion object

# isolate the question and ans dictionary from list and put the object in question bank
for item in question_data:
    q=Question(item['text'],item['choice'] ,item['answer']) # object item-->dict
    question_bank.append(q)


# create instance or object by passing the the Q and A
quiz = QuizBrain(question_bank) #object

correct = True
while(correct):
    #  
    answ =quiz.next_question()
    # print(answ)
    if (quiz.is_correct_answer(answ)):
        quiz.score+=1
        quiz.question_no+=1
        print(f"your answer is correct your score is {quiz.score}")
        # quiz.next_question()
        total_q = len(question_bank) 
        if quiz.question_no >=total_q:
            quiz.question_no=0
            question_bank= random.shuffle(question_bank)

    else:
        print(f"your answer is wrong your score is {quiz.score}")
        correct = False
# print(f'{question_bank[0].answer}\n')
