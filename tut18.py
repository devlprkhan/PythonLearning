'''
Exercise # 3

Create a program capable of displaying questions to the user like KBC. 
Use List data type to store the questions and their correct answers. 
Display the final amount the person is taking home after playing the game.
'''

# Solution

# Steps to solve the problem
# 1: iterate the questions from the quiz_question ==> Done
# 2: show on input ==> Done
# 3: store the users answers in a separate dictionary ==> Done
# 4: compare the user answers with the quiz_question "answer" ==> Done
# 5: extract  the matched answers and its points in separate dictionary ==> Done
# 6: iterate over the matched answers and extract the points and multiply them by the 100 ==> Done
# 7: sum the points and return the result ==> Done


quiz_questions = {
    "Question 1": {
        "question": "What color is the sky on a clear day?",
        "answer": "Blue",
        "points": 1
    },
    "Question 2": {
        "question": "How many legs does a cat have?",
        "answer": "4",
        "points": 1
    },
    "Question 3": {
        "question": "What is the capital of the United States?",
        "answer": "Washington",
        "points": 2
    },
    "Question 4": {
        "question": "What do bees primarily collect from flowers?",
        "answer": "Nectar",
        "points": 2
    },
    "Question 5": {
        "question": "Which month of the year has 28 days?",
        "answer": "All",
        "points": 3
    }
}

user_answer = {}
for question in quiz_questions:
  question_key = f"{question}"
  answer = input(f"Question: {quiz_questions[question]['question']}: ")
  user_answer[question_key] = {
        "question": quiz_questions[question]['question'],
        "answer": answer,
    }
  
correct_answers = {}
for answer in user_answer:
  extracted_answer = user_answer[answer]['answer']
  for actual_answer in quiz_questions:
    if(extracted_answer.title() == quiz_questions[actual_answer]['answer']):
      correct_answers[actual_answer] = {
        "points": quiz_questions[actual_answer]['points'],
        "question": quiz_questions[actual_answer]['question'],
        "answer": quiz_questions[actual_answer]['answer'],
        }

def pointsCalculator(points):
  calculated_points = []
  for point in points:
    multiplied_value = points[point]['points'] * 1500
    calculated_points.append(multiplied_value)
    total_earned_points = sum(calculated_points)
  return total_earned_points

print("\n\n")
print("***************Result*****************")
if(bool(correct_answers)):
  earnedAmount = pointsCalculator(correct_answers)
  print("Congratulation You Earned: ", earnedAmount)
else:
  earnedAmount = 0
  print("You lose (Please Try Again)!")
