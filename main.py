questions = [
    {
        "prompt": "What is the capital city of Nepal?",
        "options": ["A. Tikapur", "B. Kathmanud", "C. Dhangadhi", "D. Nepalgung"],
        "Answer": "B"
    },
    {
        "prompt": "Who is known as father of modern electricity?",
        "options": ["A. Nikola Tesla", "B. Albert Einstein", "C. Sir Issac Newton", "D. Thomas Edison"],
        "Answer": "A"
    },
    {
        "prompt": "Which country has the highest population in 2024",
        "options": ["A. China", "B. USA", "C. India", "D. Pakistan"],
        "Answer": "C"
    },
    {
        "prompt": "Who is known as father of computer",
        "options": ["A. Charles Babbage", "B. Newton", "C. Nikola Tesla", "D. Albert Einstein"],
        "Answer": "A"
    }
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        Answer = input("Enter your answer(A, B, C, D): ").upper()
        if Answer == question["Answer"]:
            print("Correct, good job!!!\n")
            score = score + 1
        else:
            print("Wrong, LOOSER!!!! The correct answer is", question["Answer"], "\n")
            
    print(f"You got {score} out of {len(questions)} question correct")
    
run_quiz(questions)
                  
                  