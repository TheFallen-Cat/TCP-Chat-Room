import tkinter as tk
import os
import threading
import tkinter
from tkinter.scrolledtext import ScrolledText
from tkinter import BOTH, TOP, X, Y, simpledialog
from tkinter import ttk
import datetime as dt

try:
    import socket
except:
    os.system("pip install sockets")
    import socket

HOST = '192.168.0.108'
PORT = 9999
msg_time = dt.datetime.now()
main_time = msg_time.strftime("%I:%M %p")



#the main class for running the client
class Client():

    def __init__(self, host, port):
        
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.client.connect((host, port))

        print("Connected!")

        nick_window = tk.Tk()
        nick_window.withdraw()

        self.nickname = simpledialog.askstring( "Nickname", "Enter your name...", parent=nick_window)

        self.isGuiDone = False
        self.isRunning = True

        self.gui_thread = threading.Thread(target = self.gui_loop)
        self.recieve_thread = threading.Thread(target = self.recieve_loop)

        self.gui_thread.start()
        self.recieve_thread.start()


    def gui_loop(self):

        #root configurations
        self.main_window = tk.Tk()
        self.main_window.configure(bg="#0a121b")
        self.main_window.geometry("300x450")
        self.main_window.title('TCP Chat')
        self.main_window.iconbitmap('E:\Python Files\TCP Chat Room\chat_icon.ico')

        #root bindings
        self.main_window.bind('<Control-z>', self.undo)

        #tabbed widgets
        self.main_tab_container = ttk.Notebook(self.main_window)
        self.main_tab_container.pack(expand=True, fill=BOTH)



        #tabbed frames 
        self.chat_frame = tk.Frame(self.main_tab_container, bg="#0f2138")
        self.chat_frame.pack()
        self.chat_frame.focus()

        self.settings_frame = tk.Frame(self.main_tab_container, bg="#0f2138")
        self.settings_frame.pack()


        #adding all the frames in the notebook
        self.main_tab_container.add(self.chat_frame, text="Chat")
        self.main_tab_container.add(self.settings_frame, text="Options")
        
        #save chat logs
        self.chat_log_button = tk.Button(self.settings_frame, text="Save Chat Log", font=("Fixedsys", 12), bg='#0f2138', fg='white', relief='flat', borderwidth=0,command=self.save_log)
        self.chat_log_button.pack(side=TOP)

        #scrolled text widget for showing the messages
        self.message_area = ScrolledText(self.chat_frame, bg="#0f2138", fg="white", height=1, font=("Fixedsys", 12))
        self.message_area.pack(fill=Y, expand=True)
        self.message_area.config(state='disabled')

        #taking the message input from the client
        self.message_input = tk.Text(self.chat_frame, fg="white", bg="#0f2138", height=2, font=("Fixedsys", 12), undo=True)
        self.message_input.pack()
        self.message_input.focus_set()

        #send message button
        self.send_button = tk.Button(self.chat_frame, text="Send", bg="#0f2138", fg="white", highlightthickness=2, command=self.write_loop, font=("Fixedsys", 12))
        self.send_button.pack()

        #bool to let the program know that it has done building the GUI and now start the connection process
        self.isGuiDone = True

        self.main_window.protocol("WM_DELETE_WINDOW", self.stop)
        self.main_window.mainloop()
            
    #write messages loop
    def write_loop(self):
        msg = self.message_input.get(1.0, tk.END).strip()

        if msg == "":
            pass

        else:
            msg_to_send = f"{self.nickname} : {msg}\n"
            self.client.send(msg_to_send.encode('utf-8'))
            self.message_input.delete(1.0, tk.END)

    #function to perform when the program closes
    def stop(self):

        self.isRunning = False
        self.main_window.destroy()
        self.client.close()
        exit(0)

    
    #loop for recieving messages and printing them
    def recieve_loop(self):
        while self.isRunning:

            try:
                message = self.client.recv(1024).decode('ascii')
                if message == "NICK":
                    self.client.send(self.nickname.encode('ascii'))

                else:

                    if self.isGuiDone:
                        self.insert_message(f"[{main_time}] {message}")

            except ConnectionAbortedError:
                break
            except:
                print("An error encountered!")
                self.client.close()
                break

    #inserting the recieved message in the message area
    def insert_message(self, msg):

        self.message_area['state'] = tk.NORMAL
        self.message_area.insert(tk.END, msg)
        self.message_area.yview(tk.END)
        self.message_area['state'] = tk.DISABLED



    #changing the themes
    def save_log(self):

        self.chat_data = self.message_area.get('1.0','end')
        with open('chat_log.txt', 'w') as log:
            log.write(self.chat_data)

        log.close()

    #undo function for message input
    def undo(self, event):
        try:
            self.message_input.edit_undo()
        except tkinter.TclError:
            pass


    #for some reason the redo command is not working xD

CLIENT = Client(HOST, PORT)