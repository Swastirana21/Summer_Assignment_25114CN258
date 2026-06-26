# Quiz application 
def quiz_application():
    score=0
    questions=[
        ("What is the capital of India?","Delhi"),
        ("What is 5+3?","8"),
         ("What language is this code written in?","Python")]
    for question,answer in questions:
        user_answer=input(question+" ").lower()
        if user_answer==answer.lower():
            print("Correct")
            score+=1
        else:
            print("Wrong! Correct answer is:",answer)
    print("Your score:",score,"/",len(questions))
quiz_application()
