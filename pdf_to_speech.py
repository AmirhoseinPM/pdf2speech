from tkinter import *
from tkinter import filedialog
import PyPDF2
import pyttsx3


def extract_text():
    file = filedialog.askopenfile(parent=root, mode="rb", title="Choose a PDF file")
    if file != None:
        pdfReader = PyPDF2.PdfReader(file)
        global extracted_text
        extraced_text = ""        
        for page in pdfReader.pages:
            extracted_text += page.extract_text()
        file.close()


def speak_text():
    global rate
    global male
    global female
    
    new_rate = int(rate.get()) if rate.get() else 100
    engine.setProperty("rate", new_rate)
    male_option = int(male.get())
    female_option = int(female.get())

    all_voices = engine.getProperty('voices')
    maleVoice = all_voices[0].id
    femaleVoice = all_voices[1].id

    print(male_option, female_option)

    if (male_option == 0 and female_option == 0) or (male_option==1 and female_option==1):
        engine.setProperty("voice", maleVoice)
    elif (male_option == 1 and female_option == 0):
        engine.setProperty("voice", maleVoice)
    else:
        engine.setProperty("voice", femaleVoice)

    engine.say(extracted_text)
    engine.runAndWait()
    

def stop_speaking():
    print("stop")
    engine.stop()


def Application(root):
    root.geometry('{}x{}'.format(700, 600))  # 700 * 600 window size
    root.resizable(width=False, height=False)  # disable maximize and minimize btn
    root.title("PDF TO AUDIO")
    root.configure(background="light grey")

    global male, female, rate

    # create  frame1 and frame2 on root
    frame1 = Frame(root, width=500, height=200, bg="indigo")
    frame2 = Frame(root, width=500, height=400, bg="light grey")

    frame1.pack(side="top", fill="both")
    frame2.pack(side="top", fill="y")

    # Frame1 widgets
    name1 = Label(frame1, text="PDF to Audio", fg="black", bg="blue",
                  font="Arial 28 bold")
    name1.pack()

    name2 = Label(frame1, text="Here your PDF file", fg="red", bg="indigo",
                  font="Calibre 25 bold")
    name2.pack()

    # Frame2 widgets
    btn = Button(frame2, text="Upload your PDF file", activeforeground="red",
                 command=extract_text, padx="70", pady="10", fg="white", bg="black",
                 font="Arial 12")
    btn.grid(row=0, pady="20", columnspan=2)

    rate_text = Label(frame2, text="Enter Rate of Speech:", fg="black", bg="aqua",
                      font="Arial 12")
    rate_text.grid(row=1, column=0, padx=0, pady=15, sticky=W)
    rate = Entry(frame2, text="100", fg="black", bg="white", font="Arial 12")
    rate.grid(row=1, column=1, padx=30, pady=15, sticky=W)

    voice_text = Label(frame2, text="Select voice:", fg="black", bg="aqua", 
                       font="Arial 12")
    voice_text.grid(row=2, column=0, pady=15, padx=0, sticky=E)
    male = IntVar()
    male_option = Checkbutton(frame2, text="Male", bg="pink", font="Arial 12",
                              variable=male, onvalue=1, offvalue=0)
    male_option.grid(row=2, column=1, padx=30, pady=0, sticky=W)
    female = IntVar()
    female_option = Checkbutton(frame2, text="Female", bg="pink", font="Arial 12",
                                variable=female, onvalue=1, offvalue=0)
    female_option.grid(row=3, column=1, padx=30, pady=0, sticky=W)

    submit_button = Button(frame2, text="Play PDF file", bg="black", fg="white", 
                           command=speak_text, padx=60, pady=10, activeforeground="red",
                           font="Arial 12")
    submit_button.grid(row=4, pady=65, columnspan=2)
    """
    stop_button = Button(frame2, text="Stop", bg="black", fg="white", 
                         activeforeground="red", padx=60, pady=10,
                         command=stop_speaking, font="Arial 12")
    stop_button.grid(row=4, column=1, pady=65)
    """


if __name__ == "__main__":
    extracted_text, rate, male, female = "", 100, 0, 0
    engine = pyttsx3.init()
    root = Tk()
    Application(root)
    root.mainloop()
