import random
import tkinter as tk
from tkinter import messagebox, ttk

words = [
    "python", "hangman", "programming", "developer", "challenge",
    "computer", "keyboard", "internet", "software", "hardware",
    "algorithm", "function", "variable", "database", "network",
    "browser", "website", "application", "interface", "password",
    "security", "encryption", "technology", "innovation", "digital",
    "monitor", "processor", "memory", "storage", "language",
    "framework", "library", "module", "package", "server"
]
word = random.choice(words)
guessed = []
wrong = 0
max_wrong = 10
hints = 2

# Dictionary of hints for each word
word_hints = {
    "python": [
        "Hint: What is a popular programming language named after a snake?",
        "Hint: This word starts with 'p' and is used by many data scientists."
    ],
    "hangman": [
        "Hint: What game are you currently playing?",
        "Hint: This word describes a classic word-guessing game."
    ],
    "programming": [
        "Hint: What do developers do to create software?",
        "Hint: This word describes writing code for computers."
    ],
    "developer": [
        "Hint: What do you call someone who builds software applications?",
        "Hint: This person writes code and creates digital solutions."
    ],
    "challenge": [
        "Hint: What is a difficult task that tests your abilities?",
        "Hint: This word means something that is hard to accomplish."
    ],
    "computer": [
        "Hint: What electronic device are you using right now?",
        "Hint: This machine processes data and runs programs."
    ],
    "keyboard": [
        "Hint: What do you use to type letters and numbers?",
        "Hint: This input device has keys arranged in rows."
    ],
    "internet": [
        "Hint: What connects computers worldwide?",
        "Hint: This global network allows you to browse websites."
    ],
    "software": [
        "Hint: What are programs and applications called?",
        "Hint: This is the non-physical part of a computer system."
    ],
    "hardware": [
        "Hint: What are the physical components of a computer?",
        "Hint: This includes things like CPU, RAM, and motherboard."
    ],
    "algorithm": [
        "Hint: What is a step-by-step procedure to solve a problem?",
        "Hint: Programmers use this to create efficient solutions."
    ],
    "function": [
        "Hint: What is a reusable block of code in programming?",
        "Hint: This performs a specific task when called."
    ],
    "variable": [
        "Hint: What stores data values in programming?",
        "Hint: This can change its value during program execution."
    ],
    "database": [
        "Hint: Where is information stored and organized?",
        "Hint: This system manages large amounts of data."
    ],
    "network": [
        "Hint: What connects multiple devices together?",
        "Hint: This allows computers to communicate with each other."
    ],
    "browser": [
        "Hint: What application do you use to view websites?",
        "Hint: Chrome, Firefox, and Safari are examples of this."
    ],
    "website": [
        "Hint: What is a collection of web pages on the internet?",
        "Hint: You visit this using a web browser."
    ],
    "application": [
        "Hint: What is a program designed for end users?",
        "Hint: This software performs specific tasks for users."
    ],
    "interface": [
        "Hint: What is the point of interaction between user and system?",
        "Hint: This is how you interact with software or hardware."
    ],
    "password": [
        "Hint: What secret code protects your accounts?",
        "Hint: You need this to log into secure systems."
    ],
    "security": [
        "Hint: What protects systems from threats and attacks?",
        "Hint: This ensures data and systems are safe."
    ],
    "encryption": [
        "Hint: What process converts data into a secret code?",
        "Hint: This protects sensitive information from unauthorized access."
    ],
    "technology": [
        "Hint: What is the application of scientific knowledge?",
        "Hint: This includes tools, machines, and systems."
    ],
    "innovation": [
        "Hint: What is the introduction of something new or improved?",
        "Hint: This drives progress and creates new solutions."
    ],
    "digital": [
        "Hint: What describes data stored in binary format?",
        "Hint: This is the opposite of analog."
    ],
    "monitor": [
        "Hint: What displays the output from your computer?",
        "Hint: This screen shows what you're working on."
    ],
    "processor": [
        "Hint: What is the brain of the computer?",
        "Hint: This component executes instructions and processes data."
    ],
    "memory": [
        "Hint: What temporarily stores data while the computer is running?",
        "Hint: RAM is a type of this."
    ],
    "storage": [
        "Hint: Where is data permanently saved on a computer?",
        "Hint: Hard drives and SSDs are examples of this."
    ],
    "language": [
        "Hint: What do programmers use to write code?",
        "Hint: Python, Java, and C++ are examples of this."
    ],
    "framework": [
        "Hint: What provides a foundation for building applications?",
        "Hint: This structure simplifies software development."
    ],
    "library": [
        "Hint: What is a collection of pre-written code?",
        "Hint: Programmers import this to use existing functions."
    ],
    "module": [
        "Hint: What is a file containing Python code?",
        "Hint: This can be imported and used in other programs."
    ],
    "package": [
        "Hint: What is a collection of related modules?",
        "Hint: This organizes code into a directory structure."
    ],
    "server": [
        "Hint: What provides services or resources to other computers?",
        "Hint: This computer hosts websites and applications."
    ]
}

def animate_label(label, new_text, color="#00FF00"):
    """Animate label text change with retro effect"""
    label.config(fg=color)
    label.config(text=new_text)
    
def update_display():
    display = " ".join([l if l in guessed else "_" for l in word])
    animate_label(word_label, display, "#00FF00")  # Bright green for retro
    
    # Update tries with retro color coding
    tries_left = max_wrong - wrong
    if tries_left <= 3:
        tries_color = "#FF0000"  # Bright red
    elif tries_left <= 6:
        tries_color = "#FFAA00"  # Amber/Orange
    else:
        tries_color = "#00FF00"  # Bright green
    tries_label.config(text=f">>> TRIES: {tries_left}", fg=tries_color)
    
    # Update hints with retro style
    hint_color = "#00FFFF" if hints > 0 else "#888888"  # Cyan or gray
    hint_label.config(text=f">>> HINTS: {hints}", fg=hint_color)
    
    # Update wrong guesses display
    wrong_letters = [l for l in guessed if l not in word]
    if wrong_letters:
        wrong_display = f">>> WRONG: {', '.join(wrong_letters)}"
        wrong_label.config(text=wrong_display, fg="#FF0000")
    else:
        wrong_label.config(text="", fg="#FF0000")
    
    # Update progress bar
    progress = (max_wrong - wrong) / max_wrong * 100
    progress_bar['value'] = progress

def flash_feedback(message, color, duration=1500):
    """Show animated feedback message with retro style"""
    feedback_label.config(text=f">>> {message}", fg=color)
    feedback_label.pack(pady=5)
    root.after(duration, lambda: feedback_label.config(text=""))

def guess_letter():
    global wrong, hints
    letter = entry.get().lower().strip()
    entry.delete(0, tk.END)

    if letter == "hint":
        if hints > 0:
            if word in word_hints:
                available_hints = word_hints[word]
                hint_index = 2 - hints  # Use different hint each time
                if hint_index < len(available_hints):
                    hint_text = available_hints[hint_index]
                else:
                    hint_text = available_hints[-1]  # Use last hint if more requests
                hints -= 1
                update_display()
                # Show hint in retro styled messagebox
                hint_window = tk.Toplevel(root)
                hint_window.title(">>> HINT <<<")
                hint_window.geometry("550x180")
                hint_window.configure(bg="#000000")
                hint_window.transient(root)
                hint_window.grab_set()
                
                hint_frame = tk.Frame(hint_window, bg="#000000", padx=20, pady=20)
                hint_frame.pack(fill=tk.BOTH, expand=True)
                
                hint_title = tk.Label(
                    hint_frame,
                    text=">>> HINT ACTIVATED <<<",
                    font=("Courier", 14, "bold"),
                    bg="#000000",
                    fg="#00FFFF"
                )
                hint_title.pack(pady=5)
                
                hint_text_label = tk.Label(
                    hint_frame, 
                    text=hint_text, 
                    font=("Courier", 11),
                    bg="#000000",
                    fg="#00FF00",
                    wraplength=500,
                    justify=tk.LEFT
                )
                hint_text_label.pack(pady=10)
                
                close_btn = tk.Button(
                    hint_frame,
                    text=">>> CONTINUE <<<",
                    command=hint_window.destroy,
                    font=("Courier", 12, "bold"),
                    bg="#001100",
                    fg="#8B0000",
                    activebackground="#002200",
                    activeforeground="#8B0000",
                    relief=tk.SOLID,
                    bd=3,
                    highlightbackground="#00FF00",
                    highlightthickness=2,
                    padx=20,
                    pady=8,
                    cursor="hand2"
                )
                close_btn.pack(pady=5)
            else:
                flash_feedback("NO HINTS AVAILABLE!", "#FF0000")
        else:
            flash_feedback("NO HINTS LEFT!", "#FF0000")
        return

    if len(letter) != 1 or not letter.isalpha():
        flash_feedback("ERROR: Enter a single letter!", "#FF0000")
        return

    if letter in guessed:
        flash_feedback("ERROR: Already guessed!", "#FF0000")
        return

    guessed.append(letter)

    if letter not in word:
        wrong += 1
        flash_feedback(f"'{letter.upper()}' NOT FOUND!", "#FF0000")
        # Animate button shake
        animate_button_shake(guess_button)
    else:
        flash_feedback(f"'{letter.upper()}' FOUND!", "#00FF00")
        # Animate correct guess
        animate_correct_guess()

    update_display()
    check_win_loss()

def animate_button_shake(button):
    """Retro flash animation for wrong guess"""
    original_fg = button.cget("fg")
    colors = ["#FF0000", original_fg, "#FF0000", original_fg]
    for i, color in enumerate(colors):
        root.after(i * 100, lambda c=color: button.config(fg=c, highlightbackground=c))

def animate_correct_guess():
    """Retro pulse animation for correct guess"""
    original_font = word_label.cget("font")
    sizes = [36, 40, 36]
    colors = ["#00FF00", "#00FFFF", "#00FF00"]
    for i, (size, color) in enumerate(zip(sizes, colors)):
        root.after(i * 100, lambda s=size, c=color: word_label.config(font=("Courier", s, "bold"), fg=c))
    root.after(300, lambda: word_label.config(font=original_font, fg="#00FF00"))

def check_win_loss():
    if "_" not in [l if l in guessed else "_" for l in word]:
        show_win_screen()
    elif wrong >= max_wrong:
        show_lose_screen()

def show_win_screen():
    """Retro win screen"""
    win_window = tk.Toplevel(root)
    win_window.title(">>> VICTORY <<<")
    win_window.geometry("500x300")
    win_window.configure(bg="#000000")
    win_window.transient(root)
    win_window.grab_set()
    
    win_frame = tk.Frame(win_window, bg="#000000", padx=30, pady=30)
    win_frame.pack(fill=tk.BOTH, expand=True)
    
    win_label = tk.Label(
        win_frame,
        text=">>> VICTORY ACHIEVED <<<",
        font=("Courier", 20, "bold"),
        bg="#000000",
        fg="#00FF00"
    )
    win_label.pack(pady=15)
    
    word_label_win = tk.Label(
        win_frame,
        text=f">>> WORD: {word.upper()} <<<",
        font=("Courier", 16, "bold"),
        bg="#000000",
        fg="#00FFFF"
    )
    word_label_win.pack(pady=15)
    
    message_label = tk.Label(
        win_frame,
        text=">>> MISSION COMPLETE <<<",
        font=("Courier", 14),
        bg="#000000",
        fg="#00FF00"
    )
    message_label.pack(pady=10)
    
    close_btn = tk.Button(
        win_frame,
        text=">>> EXIT <<<",
        command=lambda: [win_window.destroy(), root.destroy()],
        font=("Courier", 13, "bold"),
        bg="#001100",
        fg="#8B0000",
        activebackground="#002200",
        activeforeground="#8B0000",
        relief=tk.SOLID,
        bd=3,
        highlightbackground="#00FF00",
        highlightthickness=2,
        padx=30,
        pady=12,
        cursor="hand2"
    )
    close_btn.pack(pady=20)

def show_lose_screen():
    """Retro lose screen"""
    lose_window = tk.Toplevel(root)
    lose_window.title(">>> GAME OVER <<<")
    lose_window.geometry("500x300")
    lose_window.configure(bg="#000000")
    lose_window.transient(root)
    lose_window.grab_set()
    
    lose_frame = tk.Frame(lose_window, bg="#000000", padx=30, pady=30)
    lose_frame.pack(fill=tk.BOTH, expand=True)
    
    lose_label = tk.Label(
        lose_frame,
        text=">>> GAME OVER <<<",
        font=("Courier", 20, "bold"),
        bg="#000000",
        fg="#FF0000"
    )
    lose_label.pack(pady=15)
    
    word_label_lose = tk.Label(
        lose_frame,
        text=f">>> WORD: {word.upper()} <<<",
        font=("Courier", 16, "bold"),
        bg="#000000",
        fg="#FFAA00"
    )
    word_label_lose.pack(pady=15)
    
    message_label = tk.Label(
        lose_frame,
        text=">>> TRY AGAIN <<<",
        font=("Courier", 14),
        bg="#000000",
        fg="#FF0000"
    )
    message_label.pack(pady=10)
    
    close_btn = tk.Button(
        lose_frame,
        text=">>> EXIT <<<",
        command=lambda: [lose_window.destroy(), root.destroy()],
        font=("Courier", 13, "bold"),
        bg="#110000",
        fg="#8B0000",
        activebackground="#220000",
        activeforeground="#8B0000",
        relief=tk.SOLID,
        bd=3,
        highlightbackground="#FF0000",
        highlightthickness=2,
        padx=30,
        pady=12,
        cursor="hand2"
    )
    close_btn.pack(pady=20)

# Create main window with retro style
root = tk.Tk()
root.title(">>> HANGMAN GAME <<<")
root.geometry("650x600")
root.configure(bg="#000000")
root.resizable(False, False)

# Center the window
root.update_idletasks()
x = (root.winfo_screenwidth() // 2) - (650 // 2)
y = (root.winfo_screenheight() // 2) - (600 // 2)
root.geometry(f"650x600+{x}+{y}")

# Main container frame with retro border
main_frame = tk.Frame(root, bg="#000000", padx=20, pady=20)
main_frame.pack(fill=tk.BOTH, expand=True)

# Retro border effect
border_frame = tk.Frame(main_frame, bg="#00FF00", height=2)
border_frame.pack(fill=tk.X, pady=(0, 10))

# Title with retro style
title_label = tk.Label(
    main_frame,
    text=">>> HANGMAN GAME <<<",
    font=("Courier", 24, "bold"),
    bg="#000000",
    fg="#00FF00"
)
title_label.pack(pady=(10, 20))

# Word display frame with retro terminal look
word_frame = tk.Frame(main_frame, bg="#001100", relief=tk.SOLID, bd=2, highlightbackground="#00FF00", highlightthickness=2)
word_frame.pack(pady=20, padx=20, fill=tk.X)

word_label = tk.Label(
    word_frame,
    text="",
    font=("Courier", 36, "bold"),
    bg="#001100",
    fg="#00FF00",
    pady=25
)
word_label.pack()

# Stats frame
stats_frame = tk.Frame(main_frame, bg="#000000")
stats_frame.pack(pady=15)

tries_label = tk.Label(
    stats_frame,
    text=f">>> TRIES: {max_wrong}",
    font=("Courier", 14, "bold"),
    bg="#000000",
    fg="#00FF00"
)
tries_label.pack(side=tk.LEFT, padx=25)

hint_label = tk.Label(
    stats_frame,
    text=f">>> HINTS: {hints}",
    font=("Courier", 14, "bold"),
    bg="#000000",
    fg="#00FFFF"
)
hint_label.pack(side=tk.LEFT, padx=25)

# Wrong guesses label
wrong_label = tk.Label(
    main_frame,
    text="",
    font=("Courier", 12, "bold"),
    bg="#000000",
    fg="#FF0000"
)
wrong_label.pack(pady=8)

# Progress bar with retro style
progress_frame = tk.Frame(main_frame, bg="#000000")
progress_frame.pack(pady=15, fill=tk.X, padx=20)

progress_label = tk.Label(
    progress_frame,
    text=">>> PROGRESS <<<",
    font=("Courier", 10, "bold"),
    bg="#000000",
    fg="#888888"
)
progress_label.pack(anchor=tk.W)

# Custom retro progress bar
progress_bar = ttk.Progressbar(
    progress_frame,
    length=550,
    mode='determinate',
    maximum=100,
    value=100
)
progress_bar.pack(pady=5, fill=tk.X)
# Style the progress bar
style = ttk.Style()
style.theme_use('default')
style.configure("TProgressbar", background="#00FF00", troughcolor="#001100", borderwidth=0)

# Input frame
input_frame = tk.Frame(main_frame, bg="#000000")
input_frame.pack(pady=20)

entry_label = tk.Label(
    input_frame,
    text=">>> ENTER LETTER <<<",
    font=("Courier", 12, "bold"),
    bg="#000000",
    fg="#00FFFF"
)
entry_label.pack()

entry = tk.Entry(
    input_frame,
    font=("Courier", 20, "bold"),
    width=18,
    justify=tk.CENTER,
    relief=tk.SOLID,
    bd=3,
    bg="#001100",
    fg="#00FF00",
    insertbackground="#00FF00",
    highlightbackground="#00FF00",
    highlightthickness=2
)
entry.pack(pady=12)
entry.focus()

# Buttons frame
buttons_frame = tk.Frame(main_frame, bg="#000000")
buttons_frame.pack(pady=15)

guess_button = tk.Button(
    buttons_frame,
    text=">>> GUESS <<<",
    command=guess_letter,
    font=("Courier", 13, "bold"),
    bg="#001100",
    fg="#8B0000",
    activebackground="#002200",
    activeforeground="#8B0000",
    relief=tk.SOLID,
    bd=3,
    highlightbackground="#00FF00",
    highlightthickness=2,
    padx=25,
    pady=10,
    cursor="hand2",
    compound="center"
)
guess_button.pack(side=tk.LEFT, padx=15)

hint_button = tk.Button(
    buttons_frame,
    text=">>> HINT <<<",
    command=lambda: [entry.delete(0, tk.END), entry.insert(0, "hint"), guess_letter()],
    font=("Courier", 13, "bold"),
    bg="#001111",
    fg="#8B0000",
    activebackground="#002222",
    activeforeground="#8B0000",
    relief=tk.SOLID,
    bd=3,
    highlightbackground="#00FFFF",
    highlightthickness=2,
    padx=25,
    pady=10,
    cursor="hand2",
    compound="center"
)
hint_button.pack(side=tk.LEFT, padx=15)

# Feedback label
feedback_label = tk.Label(
    main_frame,
    text="",
    font=("Courier", 12, "bold"),
    bg="#000000",
    fg="#00FF00"
)
feedback_label.pack(pady=8)

# Instructions with retro style
instructions_label = tk.Label(
    main_frame,
    text=">>> TYPE 'hint' FOR CLUE <<<",
    font=("Courier", 9, "bold"),
    bg="#000000",
    fg="#888888"
)
instructions_label.pack(pady=10)

# Bottom border
border_frame2 = tk.Frame(main_frame, bg="#00FF00", height=2)
border_frame2.pack(fill=tk.X, pady=(10, 0))

# Bind Enter key
entry.bind("<Return>", lambda e: guess_letter())

# Initialize display
update_display()

# Start main loop
root.mainloop()