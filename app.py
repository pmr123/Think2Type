from tkinter import *
from PIL import ImageTk, Image
import model
import convert
from tkinter.filedialog import askopenfile
import pandas as pd


def go_back(window):
    window.destroy()
    main()

def get_input_screen(window):
    window.destroy()
    window2 = Tk()
    window2.title("Think2Type")
    window2.geometry('600x300')
    window2.configure(background='white')

    btn = Button(window2, text="Back", width=4, height=1, 
                 borderwidth= 1, bg="white", relief="solid",
                 command=lambda: go_back(window2))
    btn.place(relx=0.05, rely=0.10, anchor=CENTER)

    # pixelVirtual = PhotoImage(width=10, height=1)
    # img = ImageTk.PhotoImage(Image.open("img/Logo.jpeg"))
    # panel = Label(window2, image = img)
    # panel.place(relx=0.5, rely=0.05, anchor=N)

    v = StringVar(window2, "1") 
    values = {"Device Connected" : 1, 
              "Collecting Data" : 2, 
              "Predicting Thought" : 3, 
              "Morse Code Generated" : 4, 
              "Text Generated" : 5}

    for (text, value) in values.items(): 
        rbtn = Radiobutton(window2, text = text, variable=v,
                           value=value)
        rbtn.place(relx = 0.35, rely=0.05+0.1*(int(value))) 

    checkbtn = Checkbutton(window2, text="Show in Plain Text")
    checkbtn.place(relx = 0.7, rely=0.75)
    label = Label(window2, text='Password')
    label.place(relx = 0.2, rely =0.75)
    pasw = Entry(window2)
    pasw.place(relx = 0.3, rely=0.75)

def get_file_fill_password(pasw_field):
    f = askopenfile(mode ='r', filetypes =[('Comma Separated Values','*.csv'), ('Text Files','*.txt')])
    if f is not None:
        path = f.name
        df = pd.read_csv(path) #assuming csv file...
        data = df.values       ## size expected : (x,64)
                               ## x == length of the ^(pass)?word$

        # TODO : Make a file we can use ---> priority very high
        data = [] #till we dont get actual file to use
        password = ''
        for sequence in data: 
            morse_code = model.predict(sequence)
            character = convert.morse_to_text(morse_code)
            password += character
        if password == '':
            password = 'test'
        pasw_field.insert(0, password)

def upload_file(window):
    window.destroy()
    window2 = Tk()
    window2.title("Think2Type")
    window2.geometry('600x300')
    window2.configure(background='white')

    ## TODO: display the passoword in a text box ---> priority high
    ## TODO: Fix logo issue ---> priority low

    label = Label(window2, text='Password')
    label.place(relx = 0.25, rely =0.75)

    pasw_field = Entry(window2)
    pasw_field.place(relx = 0.40, rely=0.75)

    btn = Button(window2, text="Back", width=4, height=1, 
                 borderwidth= 1, bg="white", relief="solid",
                 command=lambda: go_back(window2))
    btn.place(relx=0.05, rely=0.10, anchor=CENTER)

    # img2 = ImageTk.PhotoImage(Image.open("./img/Logo.jpeg"))
    # panel2 = Label(window2, image = img2)
    # panel2.place(relx=0.5, rely=0.05, anchor=N)

    btn = Button(window2, text="Upload", width=20, height=4, 
                 borderwidth= 2, bg="white", relief="solid",
                 command=lambda: get_file_fill_password(pasw_field))
    btn.place(relx=0.5, rely=0.35, anchor=CENTER)

def main():
    window = Tk()
    window.title("Think2Type")
    window.geometry('600x300')
    window.configure(background='white')

    # pixelVirtual = PhotoImage(width=10, height=1)
    img = ImageTk.PhotoImage(Image.open("img/Logo.jpeg"))
    panel = Label(window, image = img)
    panel.place(relx=0.5, rely=0.05, anchor=N)

    btn = Button(window, text="Capture From Hardware", width=20, height=4, 
                 borderwidth= 2, bg="white", relief="solid",
                 command=lambda: get_input_screen(window))
    btn.place(relx=0.25, rely=0.5, anchor=CENTER)

    btn = Button(window, text="Upload Data File", width=20, height=4, 
                 borderwidth= 2, bg="white", relief="solid",
                 command=lambda: upload_file(window))
    btn.place(relx=0.75, rely=0.5, anchor=CENTER)

    # btn.grid(column=0,row=0)
    window.mainloop()

if __name__ == "__main__":
    main()
