todos = []
condition = True
quis2 = input("What you want to add in your todo list ?")
print(quis2)
todos.append(quis2)
while condition:
    print("If you want to leave write")
    ques1 = input("Would you want to add more !")
    todos.append(ques1)
    print(ques1)
    condition += 1
    if ques1=="no":
        break
todos.pop()
print("Your Todo list is here:")
for i in todos:
 print(i)

