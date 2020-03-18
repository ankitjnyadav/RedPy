import os
os.system("tput setaf 1")
print("-"*80)
print("\t\t\t Welcome to our TUI, that makes life simple")
os.system("tput setaf 0")
print("-"*80)
print('''Press 1: To See Date
Press 2: To check cal
Press 3: To Configure Web Server
Press 4: To Create file
Press 5: To Create User
Press 6: To configure n/w
Press 7: To Exit!
Please Enter your choice:''',end=' ')
print("-"*80)

choice = input()
