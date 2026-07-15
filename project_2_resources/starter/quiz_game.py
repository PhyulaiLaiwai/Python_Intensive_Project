# ==============================
# 📚 Python Intensive Course
# ==============================

# ==============================
# 🔄 Project 2: Interactive Quiz Game
# ==============================


# ****************************************
# start you code her ..........💪
import time
def show_countdown(second):
    """
    Show a countdown from the given number of seconds
    """
    print(f"\n You have {second}seconds to answer!😎")
    for i in range(second,0,-1):
        print(i,end='')
        time.sleep(1)
        print("\n")


def ask_Q (question,options,correct_ans,time_limit=10):
    """ 
     Ask single multiple choice Question with time limit
     Return  1 if the answer correct and on time
     Otherwise 0 

    """
    print(question)
    for option in options:
        print(option)
    start_time = time.time() #give current time 
    user_input= input("Enter letter of your answer: ").strip().upper()
    elsped = time.time()- start_time

    if elsped > time_limit:
        print("Time Up ⏰")
        return 0
    elif user_input == correct_ans:
        print("Correct! \n")
        return 1
    else: 
        print(f" wrong Correct answer is {correct_ans}😊\n")
        return 0
    
def main():
    """
    Run the Quiz Game

    """
    print("Welcome to Quiz Game🤩")
    score=0
    time_limit= 10
    question= [
        {"question":"what data type is used for True /False in Python",
         "option":["A.str","B.bool","C.int","D.char"],
         "answer":"B"},
        {"question":"how many color in Myanmar country flag",
         "option":["A.2","B.4","C.3","D.5"],
         "answer":"B"},

    ]
    for q in question:
        show_countdown(time_limit)
        score+=  ask_Q(q["question"],q["option"],q["answer"],time_limit)
        print(f"Quiz finish ! Your score is {score}/{len(question)}✅")
if __name__ == "__main__":
    main()

