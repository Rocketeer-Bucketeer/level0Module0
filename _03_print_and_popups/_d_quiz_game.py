from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    window.withdraw()
    score = 0
    first_question = simpledialog.askstring("Question", "Solve 1 + 1")
    if first_question == "2":
         score = score + 1
    print(score.__str__())
    second_question = simpledialog.askstring("Question", "What gets bigger the more you take out?")
    if second_question == ("A Hole") :
        score = score + 1
    print(score.__str__())
    third_question = simpledialog.askstring("Question", "How long did it take for me to think of this question?")
    if third_question == ("Three minutes") :
        score = score + 1
    print(score.__str__())
    fourth_question = simpledialog.askstring("Question", "Alright, get ready, hardest question coming up next.. also what's 8 +7")
    if fourth_question == ("15") :
        score = score + 1
    final_question = simpledialog.askstring("Questiom", " ")
    if final_question == ("Question"):
        score = score + 45982
        messagebox.showinfo("wow", "no way you actually did it, nice job! You get a free nothing")
    messagebox.showinfo("question", "Your score was " + score.__str__())
    window.mainloop()
    # Hide the window using the window's .withdraw() method
    
    # 1. Create a variable to hold the user's score. Set it equal to zero. 

    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    
    #      // 3.  Use an if statement to check if their answer is correct

    #      // 4.  if the user's answer was correct, add one to their score 
 
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
 
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method
