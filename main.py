from client import User_Inputs, __Responses

UserInput = ""
ChatBot_Name = "Chatbot"

UserInput = str.lower(input("User: "))

if UserInput in User_Inputs:
  index = User_Inputs.index(UserInput)
print(ChatBot_Name + __Responses[index])


