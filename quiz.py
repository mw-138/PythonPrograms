class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


class Quiz:
    def __init__(self, questions):
        self.questions = questions

        score = 0
        question_number = 1

        for question in self.questions:
            answer = input(f"Q{question_number}: {question.question} ")
            if answer.lower() == question.answer.lower():
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect! The answer is {question.answer}")
            question_number += 1

        print(f"You completed the quiz with {score}/{len(self.questions)} ({score / len(self.questions) * 100}%)")
