import re
import pyautogui
import tkinter as tk


def show_success_alert(message):
    root = tk.Tk()
    root.withdraw()
    dialog = tk.Toplevel(root)
    dialog.configure(background='green')
    dialog.title('Warning')
    dialog.resizable(False, False)
    message_label = tk.Label(dialog, text=message, fg='white', bg='green', font='Helvetica 20 bold', padx=20, pady=40)
    message_label.pack()
    ok_button = tk.Button(dialog, text='OK', width=10, command=dialog.destroy)
    ok_button.pack(pady=(0, 20))
    dialog.overrideredirect(True)
    window_width = 500
    window_height = 200
    screen_width = dialog.winfo_screenwidth()
    screen_height = dialog.winfo_screenheight()
    x_coordinate = (screen_width // 2) - (window_width // 2)
    y_coordinate = (screen_height // 2) - (window_height // 2)
    dialog.geometry(f'{window_width}x{window_height}+{x_coordinate}+{y_coordinate}')
    dialog.focus_force()
    dialog.grab_set()
    root.wait_window(dialog)

def show_error_alert(message):
    root = tk.Tk()
    root.withdraw()
    dialog = tk.Toplevel(root)
    dialog.configure(background='red')
    dialog.title('Warning')
    dialog.resizable(False, False)
    heading_label = tk.Label(dialog, text='WEAK PASSWORD', fg='white', bg='red', font='Helvetica 15 bold')
    heading_label.pack(padx=20, pady=(20, 0))
    message_label = tk.Label(dialog, text=message, fg='white', bg='red', font='Helvetica 12')
    message_label.pack(padx=20, pady=(0, 20))
    ok_button = tk.Button(dialog, text='OK', width=10, command=dialog.destroy)
    ok_button.pack(pady=(0, 20))
    dialog.overrideredirect(True)
    window_width = 700
    window_height = 150
    screen_width = dialog.winfo_screenwidth()
    screen_height = dialog.winfo_screenheight()
    x_coordinate = (screen_width // 2) - (window_width // 2)
    y_coordinate = (screen_height // 2) - (window_height // 2)
    dialog.geometry(f'{window_width}x{window_height}+{x_coordinate}+{y_coordinate}')
    dialog.focus_force()
    dialog.grab_set()
    root.wait_window(dialog)


password = pyautogui.password('Enter your password: ', title=' Password Strength Determiner ')

if len(password) >= 8:
    if any(char.isupper() for char in password) and any(char.isdigit() for char in password):
        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            show_success_alert("STRONG PASSWORD!")
        else:
            show_error_alert("The password should contain at least one special character.")
    else:
        show_error_alert("The password should contain at least one uppercase letter and one digit.")
else:
    show_error_alert("The password should be at least 8 characters long.")
