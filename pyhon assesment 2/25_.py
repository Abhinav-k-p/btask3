# Quiz Game in Python

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question):
        print(question)

    def get_user_answer(self):
        return input("Your answer: ").lower()

    def evaluate_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            print("Correct!\n")
            self.score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.\n")

    def run_quiz(self):
        for question, correct_answer in self.questions.items():
            self.display_question(question)
            user_answer = self.get_user_answer()
            self.evaluate_answer(user_answer, correct_answer)

        print(f"Quiz completed! Your score: {self.score}/{len(self.questions)}")


questions = {
    "Total number od district in kerala?": "14",
    "Which is one of the highest population district in kerala?": "Malappuram",
    "Who is the cheif minister of kerala?": "Pinarayi vijayan",
    "how many states in india?": "28",
    "where is the gateway of india located'?": "Mumbai"
}

quiz = Quiz(questions)
quiz.run_quiz()
