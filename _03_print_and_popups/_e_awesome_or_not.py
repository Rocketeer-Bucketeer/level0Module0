from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    window.withdraw()
    hi = random.randint(0, 3)
    print(hi)
    something = simpledialog.askstring("maybe", "What do you think is awesome?")
    if hi == 0 :
        messagebox.showinfo("maybe", "I agree! It is awesome!")
    if hi == 1:
        messagebox.showinfo("maybe", "It's fine... I guess")
    if hi == 2:
        messagebox.showinfo("maybe", "*yawn* That's boring")
    if hi == 3:
        messagebox.showinfo("maybe", "I have no idea what you said. It sounds awesome though")
    window.mainloop()
    # Hide the window using the window's .withdraw() method

    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
    
    # 2. Print your variable to the console
    
    # 3. Get the user to enter something that they think is awesome
    
    # 4. If your variable is  0
        # -- tell the user whatever they entered is awesome!
        
    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
    
    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
    
    # 7. If your variable is  3
        # -- invent your own message to give to the user (be nice).
        
    # Run the window's .mainloop() method
