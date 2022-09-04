import tkinter
import customtkinter


def login_screen():
    global login_window
    login_window = customtkinter.CTk()
    login_window.title("Login")
    login_window.geometry("400x200")
    login_window.resizable(0, 0)
    username_label = customtkinter.CTkLabel(login_window, text="Username: ")
    password_label = customtkinter.CTkLabel(login_window, text="Password: ")
    username_entry = customtkinter.CTkEntry(login_window, width=170, corner_radius=20)
    password_entry = customtkinter.CTkEntry(login_window, width=170, corner_radius=20)
    login_btn = customtkinter.CTkButton(login_window, text="Login", width=80, corner_radius=20, command=signup_screen)
    username_label.place(x=50, y=30)
    password_label.place(x=50, y=65)
    username_entry.place(x=160, y=30)
    password_entry.place(x=160, y=65)
    login_btn.place(x=125, y=105)
    login_window.mainloop()


def signup_screen():
    login_window.destroy()
    signup_window = customtkinter.CTk()
    signup_window.title("Signup")
    signup_window.geometry("400x180")
    signup_window.resizable(0, 0)
    username_label = customtkinter.CTkLabel(signup_window, text="Username: ")
    password_label = customtkinter.CTkLabel(signup_window, text="Password: ")
    username_entry = customtkinter.CTkEntry(signup_window, width=200, corner_radius=20)
    password_entry = customtkinter.CTkEntry(signup_window, width=130, corner_radius=20)
    generate_btn = customtkinter.CTkButton(signup_window, text="Generate", width=30, corner_radius=20)
    back_btn = customtkinter.CTkButton(signup_window, text="Back", width=80, corner_radius=20, command=login_screen)
    signup_btn = customtkinter.CTkButton(signup_window, text="Signup", width=80, corner_radius=20)
    bark_switch = customtkinter.CTkSwitch(signup_window, text="")
    username_label.place(x=20, y=30)
    password_label.place(x=20, y=65)
    username_entry.place(x=130, y=30)
    password_entry.place(x=130, y=65)
    generate_btn.place(x=265, y=65)
    back_btn.place(x=125, y=105)
    signup_btn.place(x=215, y=105)
    bark_switch.place(x=340, y=150)
    signup_window.mainloop()


login_screen()
