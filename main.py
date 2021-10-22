from tkinter import *
root =Tk()
text = Text(root, bg = "royal blue", fg ="green")
text.grid(row = 0,column= 0, columnspan =2)
entry = Entry(root, width = 80)
entry.grid(row = 1, column= 0)

screen.clr()
def send():
    send = "You" + entry.get()
    text.insert(END, "\n" + send)
    if(entry.get()== "Hi"):
        text.insert(END,"\n" "Bot: Hello")
    elif(entry.get() == "Hello"):
        text.insert(END, "\n" + "Bot: Hi")
    elif(entry.get() == "How are you?"):
        text.insert(END, "\n" + "Bot: i'm fine and you?")
    elif(entry.get() == "i'm fine too"):
        text.insert(END, "\n" + "Bot:nice to hear that")
        text.insert(END, "\n" + "Bot:How May be foe service")
    else:
        text.insert(END, "\n" + "Bot: Sorry could not comprend request.")

send = Button(root, text ="send",bg="yellow",fg = "white", width = 20,command =send())
send.grid(row = 1,column =1)
root.title("Conversation")
root.mainloop()