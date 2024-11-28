# Print “Welcome” if your name is present in the list and “See you next time” if 
# name is not present

l1 = input("Enter name: ")
name_list = ["hari", "avisa", "babu"]

if l1 in name_list:
    print("Welcome")
else:
    print("see you next time")
