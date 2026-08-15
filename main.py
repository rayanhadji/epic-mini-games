import tkinter as tk

#Window creation
window = tk.Tk()
window.title("Epic Mini Games")
window.geometry("600x400")
window.config(bg="grey")

#Creating frames
menu_frame = tk.Frame(window, bg="blue")
play_frame = tk.Frame(window, bg="red")
show_score_frame = tk.Frame(window, bg="green")
reset_score_frame = tk.Frame(window, bg="yellow")

#Main menu
menu_frame.pack(fill="both", expand=True)

title = tk.Label(menu_frame, text="Epic Mini Games", font=("Arial",24), bg="black", fg="white")
title.pack(pady=20)

#Show frame function
def show_frame(frame_to_show):
    menu_frame.pack_forget()
    play_frame.pack_forget()
    show_score_frame.pack_forget()
    reset_score_frame.pack_forget()
    
    frame_to_show.pack(fill="both", expand=True)

#Menu Buttons + Exit Button
play_button = tk.Button(menu_frame, text="Play", command=lambda: show_frame(play_frame), width=15, height=2)
play_button.pack(pady=10)

show_score_button = tk.Button(menu_frame, text="Show Score", command=lambda: show_frame(show_score_frame), width=15, height=2)
show_score_button.pack(pady=10)

reset_score_button = tk.Button(menu_frame, text="Reset Score", command=lambda: show_frame(reset_score_frame), width=15, height=2)
reset_score_button.pack(pady=10)

def exit_button_press():
    window.destroy()

exit_button = tk.Button(menu_frame, text="Exit", command=exit_button_press, width=15, height=2)
exit_button.pack(pady=10)

#Back Buttons
back_from_play_button = tk.Button(play_frame, text="Back", command=lambda: show_frame(menu_frame), width=15, height=2)
back_from_play_button.pack(pady=10)

back_from_show_score_button = tk.Button(show_score_frame, text="Back", command=lambda: show_frame(menu_frame), width=15, height=2)
back_from_show_score_button.pack(pady=10)

back_from_reset_score_button = tk.Button(reset_score_frame, text="Back", command=lambda: show_frame(menu_frame), width=15, height=2)
back_from_reset_score_button.pack(pady=10)

window.mainloop()