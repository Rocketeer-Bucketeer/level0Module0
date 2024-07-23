from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # Put this sentence in a pop-up message box:
    messagebox.showinfo("informer", "If you find yourself having to cross a piranha-infested river, heres how to do it...")
# "If you find yourself having to cross a piranha-infested river, here's how to do it..."
    adjective = simpledialog.askstring("informer", "Enter an adjective")

    liquid = simpledialog.askstring("mad libs dude", "Enter a type of liquid")

    body_part = simpledialog.askstring("mad libs dude", "Enter a body part")
    verb = simpledialog.askstring("mad libs dude", "Enter a verb")
    place = simpledialog.askstring("mad libs dude", "Enter a place")
    messagebox.showinfo("informer", "Piranahas are more " + adjective +" during the day, so cross the river at night.")
    messagebox.showinfo("informer", "Piranahas are attracted to fresh " + liquid + " and will most")
    messagebox.showinfo("informer", "likely to take a bite out of your " + body_part + " if you " + verb + ".")
    messagebox.showinfo("informer", "Whatever you do, if you have an open wound, try to find another way to get back the")
    messagebox.showinfo("informer", place + ". Good luck!")

    window.mainloop()
    # Get the player to enter an adjective

    # Get the player to enter a type of liquid

    # Get the player to enter a body part

    # Get the player to enter a verb

    # Get the player to enter a place

    # The story below has has been written as a group of Strings joined
    # together by + signs. The story contains place holders, indicated
    # by [** **] which you need to replace with the values entered by the
    # player.
    # Hint: You will need to add more + signs to join the variables to the
    #       other parts of the story.

    story = (
        "Piranhas are more [**adjective**] during the day, so cross the river at\n"
        "night. Piranhas are attracted to fresh [**type of liquid**] and will most\n"
        "likely take a bite out of your [**body part**] if you [**verb**]. Whatever\n"
        "you do, if you have an open wound, try to find another way to get "
        "back to the [**place**]. Good luck!"
    )

    # Make a pop-up that contains the final story. The \n escape characters add
    # line breaks to the story. If you need to, move them around to make your
    # story look better in the pop-up

    # If you want to write your own Madlib story, just change the story variable
    # and ask the player different questions.

    # Run the window's .mainloop() method

    pass
