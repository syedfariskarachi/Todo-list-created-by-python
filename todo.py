todos = []
condition = True
quis1 = input("What you want to add in your todo list ?\n")
print(quis1)
todos.append(quis1)
while condition:
    ques2 = input("Whould you want to add more !\n")
    todos.append(ques2)
    print(ques2)
    condition += 1
    if ques2 == "no":
        break
todos.pop()
print("Your TODOS list is ready",todos)
