# 사용자에게 질문
# 정답확인
# 마지막 질문까지 진행

# quiz_brain class 생성
# 속성과 메소드 정의

class QuizBrain:
    
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        input(f'Q.{self.question_number}: {current_question.text} (True/False): ')
    

