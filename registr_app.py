import customtkinter
import socket

from tkinter import messagebox
from hashlib import sha256

class RegistrForm(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title('Registr from')
        self.geometry('400x500')
        self.resizable(False, False)

        self.name_field = customtkinter.CTkEntry(master = self, width = 200, height = 30, placeholder_text = 'name', fg_color= ('white'), text_color = ('black'))
        self.name_field.grid(padx = 100, pady = (150, 0))

        self.surname_field = customtkinter.CTkEntry(master = self, width = 200, height = 30, placeholder_text = 'surname', fg_color= ('white'), text_color = ('black'))
        self.surname_field.grid(padx = 100, pady = (10, 0))

        self.email_field = customtkinter.CTkEntry(master = self, width = 200, height = 30, placeholder_text = 'email', fg_color= ('white'), text_color = ('black'))
        self.email_field.grid(padx = 100, pady = (10, 0))

        self.password_field = customtkinter.CTkEntry(master = self, width = 200, height = 30, show = '*', placeholder_text = 'password', fg_color= ('white'), text_color = ('black'))
        self.password_field.grid(padx = 100, pady = (10, 0))

        self.send_information = customtkinter.CTkButton(master = self, width = 200, height = 30, text = 'Registration', command = self.send_data_server)
        self.send_information.grid(padx = 100, pady = (10, 0))

    def send_data_server(self):

        application_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.name = self.name_field.get()
        self.surname = self.surname_field.get()
        self.email = self.email_field.get()
        self.password = self.password_field.get()

        if self.name == '':
            messagebox.showerror('Warnings!', 'Name field is empty!')
            self.name_field.focus()

        elif self.surname == '':
            messagebox.showerror('Warnings!', 'Surname field is empty!')
            self.surname_field.focus()

        elif self.email == '':
            messagebox.showerror('Warnings!', 'Email field is empty!')
            self.email_field.focus()

        elif self.password == '':
            messagebox.showerror('Warnings!', 'Password field is empty!')
            self.password_field.focus()
        
        else:

            person_info = {
                    'name' : self.name,
                    'surname' : self.surname,
                    'email' : self.email,
                    'password' : sha256(self.password.encode('utf-8')).hexdigest()
                }

            try:
                application_socket.connect(('127.0.0.1', 8888))

            except:
                pass

            else:
                send_data = f'{person_info["name"]} : {person_info["surname"]} : {person_info["email"]} : {person_info["password"]}'.encode()

                application_socket.send(send_data)

                application_socket.close()

                self.name_field.delete(0, 'end')
                self.surname_field.delete(0, 'end')
                self.email_field.delete(0, 'end')
                self.password_field.delete(0, 'end')

if __name__ == '__main__':
    main_window = RegistrForm()
    main_window.mainloop()
