import tkinter as tk

#Window creation
window = tk.Tk()
window.title("Epic Mini Games")
window.geometry("600x400")
window.config(bg="grey")
window.minsize(600, 400)

#Creating frames
menu_frame = tk.Frame(window, bg="blue")
play_frame = tk.Frame(window, bg="red")
show_score_frame = tk.Frame(window, bg="green")
reset_score_frame = tk.Frame(window, bg="yellow")
rps_frame = tk.Frame(window, bg="purple")
guess_number_frame = tk.Frame(window, bg="black")

#Main menu
menu_frame.grid_rowconfigure(0, weight=0)
menu_frame.grid_rowconfigure(1, weight=1)
menu_frame.grid_columnconfigure(0, weight=1)
menu_frame.grid_columnconfigure(1, weight=3)

title = tk.Label(menu_frame, text="Epic Mini Games", font=("Arial",24), bg="black", fg="white")
title.grid(row=0, column=0, columnspan=2, pady=20)

menu_sidebar = tk.Frame(menu_frame, bg="blue")
menu_sidebar.grid(row=1, column=0, sticky="nsew")

menu_content = tk.Frame(menu_frame, bg="blue")
menu_content.grid(row=1, column=1, sticky="nsew")


menu_frame.pack(fill="both", expand=True)
#Show frame function
def show_frame(frame_to_show):
    menu_frame.pack_forget()
    play_frame.pack_forget()
    show_score_frame.pack_forget()
    reset_score_frame.pack_forget()
    rps_frame.pack_forget()
    guess_number_frame.pack_forget()
    
    frame_to_show.pack(fill="both", expand=True)

#Menu Buttons + Exit Button
play_button = tk.Button(menu_sidebar, text="Play", command=lambda: show_frame(play_frame), width=15, height=2)
play_button.pack(pady=10, fill="x", padx=10)

show_score_button = tk.Button(menu_sidebar, text="Show Score", command=lambda: show_frame(show_score_frame), width=15, height=2)
show_score_button.pack(pady=10, fill="x", padx=10)

reset_score_button = tk.Button(menu_sidebar, text="Reset Score", command=lambda: show_frame(reset_score_frame), width=15, height=2)
reset_score_button.pack(pady=10, fill="x", padx=10)

def exit_button_press():
    window.destroy()

exit_button = tk.Button(menu_sidebar, text="Exit", command=exit_button_press, width=15, height=2)
exit_button.pack(pady=10, fill="x", padx=10)


#Play frame
play_text = tk.Label(play_frame, text="which game you wanna play?", font=("Arial",24), bg="black", fg="white")
play_text.pack(fill="x", pady=20)

play_sidebar = tk.Frame(play_frame, bg="blue", width=150)
play_sidebar.pack(side="left", fill="y")
play_sidebar.pack_propagate(False)

play_rps_button = tk.Button(play_sidebar, text="Rock Paper Scissor", command=lambda: show_frame(rps_frame), width=15, height=2)
play_rps_button.pack(pady=10)

play_guess_number_button = tk.Button(play_sidebar, text="Guess Number", command=lambda: show_frame(guess_number_frame), width=15, height=2)
play_guess_number_button.pack(pady=10)

#Back Buttons
back_from_play_button = tk.Button(play_sidebar, text="Back", command=lambda: show_frame(menu_frame), width=15, height=2)
back_from_play_button.pack(pady=10)

back_from_show_score_button = tk.Button(show_score_frame, text="Back", command=lambda: show_frame(menu_frame), width=15, height=2)
back_from_show_score_button.pack(pady=10)

back_from_reset_score_button = tk.Button(reset_score_frame, text="Back", command=lambda: show_frame(menu_frame), width=15, height=2)
back_from_reset_score_button.pack(pady=10)

window.mainloop()