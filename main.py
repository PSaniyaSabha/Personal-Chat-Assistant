#ChatBot Using Python

import datetime
import time

name = input("Hey,Enter your good name:")
presentHour = datetime.datetime.now().hour

if 5 <= presentHour <=11:
    print("Good Morning",name)
elif 11 <= presentHour <=17:
        print("Good Afternoon",name)
elif 17 <= presentHour <=20:

../..........................................................................................................................................................................................................................................................................................                                                                                                                                  else:
    print("Good Night",name)



print("Namaste! Welcome to Your Buddy ChatBot")
print("You can ask me basic question")



#chatbot memory creation [dictionary of responses]
responses = {
    "hello": "Hello there! How can I Help you today?",
    "how are you": "I'm doing well, thank you!",
    "what is your name": "I'm Your Buddy ChatBot",
    "Who are you": "I'm Your Buddy ChatBot, here to assist you!",
    "Motivate me": "Believe in yourself! Every bug of your project makes you a good developer.",
    "Aaj hum kya karein": "Chup chap jaa kar kitaab kholein aur padhai shuru karein!",
    "bye": "Goodbye! Have a great day!"
}



#Method/Function to get response from chatbot
def getResponseofBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
    return "I'm sorry, I don't understand your question."
    


#take user input
while True:
    userInput = input("Please ask your question:")
    reply = getResponseofBot(userInput)
    print("Bot Response:", reply)

    if "bye" in userInput.lower():
        break
