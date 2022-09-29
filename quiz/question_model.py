# from data import question_data 
import random
# a class that model the dquestion(q and ans)
class Question:
    # 'type' = 'True/ False' # first atribute
    def __init__(self,question,choice,ans):
        self.text = question
        self.choice = choice
        self.answer = ans

