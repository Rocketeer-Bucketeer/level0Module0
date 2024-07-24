from tkinter import messagebox, simpledialog, Tk
import sys
import random

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # 1. Change this line to give you a random number between 1 - 100.
    random_num = random.randint(1, 100)

    # 2. Print out the random variable that you made in step #1
    print(random_num)
    # 3. Code a for loop to run steps 4-10, 10 times
    for i in range (10):
        guess = simpledialog.askinteger("High or Low", "Guess a number from 1 - 100")
        if guess == (random_num):
            messagebox.showinfo("High or Low", "You guessed it!")
        elif guess < (random_num):
            messagebox.showinfo("High or Low", "Higher")
        elif guess > (random_num):
            messagebox.showinfo("High or low", "Lower")
    messagebox.showerror("High or Low", "You lost.... nice try though! The answer was " + random_num.__str__() +".")

        # 4. Ask the user for a guess using a pop-up window, and save their response

        # 5. If the guess is correct
            # 6. Win. Use 'sys.exit(0)' to end the program

        # 7. if the guess is high
            # 8. Tell them it's too high
        # 9. Else if the guess is low
            # 10. Tell them it's too low

    #11. Outside of the loop, tell the user they lost

    window.mainloop()
