from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *

bot = ChatBot("My Bot")

convo=[
    'hii',
    'hello',
    'what is your name',
    'i am bot',

]
trainer=ListTrainer(bot)

#now traning the bot

trainer.train(convo)

# ans=bot.get_response("what is your name")
# print(ans)

# print("talk to bot")

# while True:
#     query=input()
#     if query == 'exit':
#         break
#     answer=bot.get_response(query)
#     print("bot : ",answer)

main = Tk()
main.geometry("500x650")
main.title("chat bot")

def ask_from_bot():
    query = textf.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END,"you : " + query)
    print(type(answer_from_bot))
    msgs.insert(END,"bot : " + str(answer_from_bot))
    print(type(answer_from_bot))
    textf.delete(0,END)


frame = Frame(main)

sc=Scrollbar(frame)

msgs=Listbox(frame,width=80,height=20)

sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()

#creating text field

textf = Entry(main, font=("verdana", 20))
textf.pack(fill=X, pady=10)


btn=Button(main,text="Ask from bot",font=("verdana",20),command=ask_from_bot)
btn.pack()


main.mainloop()


