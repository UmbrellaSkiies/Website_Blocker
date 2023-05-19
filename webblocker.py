from tkinter import *
import tkinter as tk

root = tk.Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title("Surf Blocker | Browser Blocker")

Label(root, text='The Matrix Website Blocker', font='arial 20 bold', fg='#4a2140', pady=15).pack()

# Instructions label
instructions_label = Label(root, text='Enter the websites you want to block (separated by commas):', font='arial 11', fg='grey')
instructions_label.pack()

host_path = 'C:\Windows\System32\drivers\etc\hosts'
ip_address = '127.0.0.1'

Label(root, text='Enter Websites:', font='arial 13 bold').place(x=5, y=115)

Websites = Text(root, font='arial 11', height=2, width=40)
Websites.place(x=140, y=110)

status_label = Label(root, text="Status Goes Here", font='arial 12 bold')
status_label.place(x=210, y=240)

def block_website():
    website_lists = Websites.get(1.0, END)
    Website = list(website_lists.split(","))

    with open(host_path, 'r+') as host_file:
        file_content = host_file.read()

        for web in Website:
            if web in file_content:
                status_label.config(text='Already Blocked', fg='red')
            else:
                host_file.write(ip_address + " " + web + '\n')
                status_label.config(text='Blocked', fg='red')    #### pady=22 #####

def unblock_website():
    website_lists = Websites.get(1.0, END)
    Website = list(website_lists.split(","))

    with open(host_path, 'r+') as host_file:
        lines = host_file.readlines()
        host_file.seek(0)
        blocked = False

        for line in lines:
            if not any(web.strip() in line for web in Website):
                host_file.write(line)
            else:
                blocked = True
        host_file.truncate()

    if blocked:
        status_label.config(text='Unblocked', fg='green')
    else:
        status_label.config(text='Website(s) already unblocked', fg='black')

def clear_entry():
    Websites.delete(1.0, END)

def exit_app():
    root.destroy()

block = Button(root, text='Block', font='arial 12 bold', pady=5, command=block_website, width=8, bg='red', activebackground='pink')
block.place(x=210, y=170)

unblock = Button(root, text='Unblock', font='arial 12 bold', pady=5, command=unblock_website, width=8, bg='green', activebackground='light green')
unblock.place(x=310, y=170)

clear = Button(root, text='Clear', font='arial 12 bold', pady=5, command=clear_entry, width=6, bg='royal blue', activebackground='sky blue')
clear.place(x=30, y=170)

exit_button = Button(root, text='Exit', font='arial 12 bold', pady=5, command=exit_app, width=6, bg='gray', activebackground='light gray')
exit_button.place(x=30, y=230)

root.mainloop()
