from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
    
    # Make a new window variable, window = Tk()
window = Tk()
window.withdraw()
average_answer = simpledialog.askstring("Question Person", "Do you know how to code?")
if average_answer == ("Yes") or ("yes"):
    messagebox.showinfo("Question Person", "You shall rule the world!")
else:
    messagebox.showerror("Question Person", "You need to sign up for the league of amazing programmers")

window.mainloop()
    # Hide the window using the window's .withdraw() method
    
    # 1. Ask the user if they know how to write code.
    
    # 2. If they say "yes", tell them they will rule the world in a message box pop-up.

    # 3. Otherwise, tell them to sign up for classes at The League in an error box pop-up.
    
    # Run the window's .mainloop() method
