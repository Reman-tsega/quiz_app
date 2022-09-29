# from question_model import Question
# from data import question_data
# from main import question_bank
# ask the question next qustion
# check if the answer was correct
class QuizBrain:
    # question_list =''

    def __init__(self,q_list):
        self.question_list= q_list
        self.question_no =0
        self.score=0
    def next_question(self):
        current_question = self.question_list[self.question_no]#question dict
        # current_choice = self.question_list[self.]

        # self.question_no +=1
        choice = current_question.choice
        print(f'')
        ans = input(f'Q.{self.question_no+1}, {current_question.text} \nchoose the best answer {choice} ? :').capitalize()

        return ans

    def is_correct_answer(self,ans):
        correct_ans= self.question_list[self.question_no].answer

        # self.user_ans=

        if correct_ans==ans:
            return True
        return False




