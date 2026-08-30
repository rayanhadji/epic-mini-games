import tkinter as tk
import random

#Window creation=============================================================================================================================
window = tk.Tk()
window.title("Epic Mini Games")
window.geometry("600x400")
window.config(bg="grey")
#============================================================================================================================================

#Creating frames=============================================================================================================================
menu_frame = tk.Frame(window, bg="blue")
play_frame = tk.Frame(window, bg="red")
show_score_frame = tk.Frame(window, bg="green")
reset_score_frame = tk.Frame(window, bg="yellow")
rps_frame = tk.Frame(window, bg="purple")
guess_number_frame = tk.Frame(window, bg="black")
#============================================================================================================================================

#Main menu===================================================================================================================================
title = tk.Label(menu_frame, text="Epic Mini Games", font=("Arial",24), bg="black", fg="white")
title.pack(fill="x", pady=20)

menu_frame.pack(fill="both", expand=True)
menu_sidebar = tk.Frame(menu_frame, bg="blue", width=150)
menu_sidebar.pack(side="left", fill="y")
menu_sidebar.pack_propagate(False)
#============================================================================================================================================

#Show frame function=========================================================================================================================
def show_frame(frame_to_show):
    menu_frame.pack_forget()
    play_frame.pack_forget()
    show_score_frame.pack_forget()
    reset_score_frame.pack_forget()
    rps_frame.pack_forget()
    guess_number_frame.pack_forget()
    
    frame_to_show.pack(fill="both", expand=True)
#============================================================================================================================================

#Menu Buttons + Exit Button==================================================================================================================
play_button = tk.Button(menu_sidebar, text="Play", command=lambda: show_frame(play_frame), width=15, height=2)
play_button.pack(pady=10)

show_score_button = tk.Button(menu_sidebar, text="Show Score", command=lambda: show_frame(show_score_frame), width=15, height=2)
show_score_button.pack(pady=10)

reset_score_button = tk.Button(menu_sidebar, text="Reset Score", command=lambda: show_frame(reset_score_frame), width=15, height=2)
reset_score_button.pack(pady=10)

def exit_button_press():
    window.destroy()

exit_button = tk.Button(menu_sidebar, text="Exit", command=exit_button_press, width=15, height=2)
exit_button.pack(pady=10)
#============================================================================================================================================

#Play frames=================================================================================================================================
play_text = tk.Label(play_frame, text="which game you wanna play?", font=("Arial",24), bg="black", fg="white")
play_text.pack(fill="x", pady=20)

play_sidebar = tk.Frame(play_frame, bg="blue", width=150)
play_sidebar.pack(side="left", fill="y")
play_sidebar.pack_propagate(False)

play_rps_button = tk.Button(play_sidebar, text="Rock Paper Scissor", command=lambda: show_frame(rps_frame), width=15, height=2)
play_rps_button.pack(pady=10)

play_guess_number_button = tk.Button(play_sidebar, text="Guess Number", command=lambda: [show_frame(guess_number_frame), start_guess_game()], width=15, height=2)
play_guess_number_button.pack(pady=10)
#============================================================================================================================================

#Back Buttons================================================================================================================================
back_from_play_button = tk.Button(play_sidebar, text="Back", command=lambda: show_frame(menu_frame), width=15, height=2)
back_from_play_button.pack(pady=10)

back_from_show_score_button = tk.Button(show_score_frame, text="Back", command=lambda: show_frame(menu_frame), width=15, height=2)
back_from_show_score_button.pack(pady=10)

back_from_reset_score_button = tk.Button(reset_score_frame, text="Back", command=lambda: show_frame(menu_frame), width=15, height=2)
back_from_reset_score_button.pack(pady=10)
#============================================================================================================================================

#rock paper scissor game=====================================================================================================================
user_score = 0
pc_score = 0

#choices functions
def choose_rock():
    global user_score, pc_score
    pc_choice = random.choice(["rock", "paper", "scissor"])
    
    if pc_choice == "rock":
        rps_result_label.config(text="pc choosed rock, it's a tie")
    elif pc_choice == "paper":
        rps_result_label.config(text="pc choosed paper, you lost try again")
        pc_score +=1
    else:
        rps_result_label.config(text="pc choosed scissor, congratulations you won")
        user_score +=1
    
    rps_score_label.config(text=f"you: {user_score} - PC: {pc_score}")
    
def choose_paper():
    global user_score, pc_score
    pc_choice = random.choice(["rock", "paper", "scissor"])
    
    if pc_choice == "paper":
        rps_result_label.config(text="pc choosed paper, it's a tie")
    elif pc_choice == "scissor":
        rps_result_label.config(text="pc choosed scissor, you lost try again")
        pc_score +=1
    else:
        rps_result_label.config(text="pc choosed rock, congratulations you won")
        user_score +=1
    
    rps_score_label.config(text=f"you: {user_score} - PC: {pc_score}")
    
def choose_scissor():
    global user_score, pc_score
    pc_choice = random.choice(["rock", "paper", "scissor"])
    
    if pc_choice == "scissor":
        rps_result_label.config(text="pc choosed scissor, it's a tie")
    elif pc_choice == "rock":
        rps_result_label.config(text="pc choosed rock, you lost try again")
        pc_score +=1
    else:
        rps_result_label.config(text="pc choosed paper, congratulations you won")
        user_score +=1
    
    rps_score_label.config(text=f"you: {user_score} - PC: {pc_score}")

#creating images
rock_image = tk.PhotoImage(file="images/rock.png")
paper_image = tk.PhotoImage(file="images/paper.png")
scissor_image = tk.PhotoImage(file="images/scissor.png")

#rock paper scissor game insides
rps_score_label = tk.Label(rps_frame, text=f"you: {user_score} - PC: {pc_score}", font=("Arial", 14), bg="black", fg="white")
rps_score_label.pack(pady=10)

rps_result_label = tk.Label(rps_frame, text="", font=("Arial", 14), bg="black", fg="white")
rps_result_label.pack(pady=10)

rock_button = tk.Button(rps_frame, image=rock_image, command=choose_rock, width=100, height=100)
rock_button.pack(pady=10)

paper_button = tk.Button(rps_frame, image=paper_image, command=choose_paper, width=100, height=100)
paper_button.pack(pady=10)

scissor_button = tk.Button(rps_frame, image=scissor_image, command=choose_scissor, width=100, height=100)
scissor_button.pack(pady=10)

rps_game_back_button = tk.Button(rps_frame, text="Back", command=lambda: show_frame(play_frame), width=10, height=2)
rps_game_back_button.pack(pady=10)
#============================================================================================================================================

#guess the number game=======================================================================================================================
attempts = 0
target_number = 0

#start function
def start_guess_game():
    global attempts, target_number
    target_number = random.randint(1, 100)
    attempts = 0
    
    guess_result_label.config(text="Guess a number")
    guess_entry.delete(0, "end")
    guess_button.config(state="normal")
    
#guess check function
def check_guess():
    global attempts
    try:
        user_guess = int(guess_entry.get())
    except ValueError:
        guess_result_label.config(text="That's not a number!")
        return
    
    attempts += 1
    guess_entry.delete(0, "end")
        
    if user_guess == target_number:
        guess_result_label.config(text=f"congratulations, you found it in {attempts} attempts")
        guess_button.config(state="disabled")
    elif user_guess > target_number:
        guess_result_label.config(text="Try a bit lower")
    else:
        guess_result_label.config(text="Try a bit higher")
    
#guess the number game insides    
guess_result_label = tk.Label(guess_number_frame, text="Guess a number", font=("Arial", 14), bg="black", fg="white")
guess_result_label.pack(pady=10)

guess_entry = tk.Entry(guess_number_frame, font=("Arial", 16), width=10)
guess_entry.pack(pady=10)

guess_button = tk.Button(guess_number_frame, text="Guess", command=check_guess, width=10, height=2)
guess_button.pack(pady=10)

new_game_button = tk.Button(guess_number_frame, text="New Game", command=start_guess_game, width=10, height=2)
new_game_button.pack(pady=10)

guess_game_back_button = tk.Button(guess_number_frame, text="Back", command=lambda: show_frame(play_frame), width=10, height=2)
guess_game_back_button.pack(pady=10)
#============================================================================================================================================
window.mainloop()