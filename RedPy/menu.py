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
Press 7: To Exit!''')
print("-"*80)
print('Please Enter your choice:',end=' ')
choice = int(input())
print("-"*80, end='\n')

if choice==1:
    os.system("date")
elif choice==2:
    os.system("cal")
elif choice==3:
    os.system("yum install httpd")
elif choice==4:
    print('Choice 4')
elif choice==5:
    user_name = input('Enter the username: ')
    os.system("useradd {}".format(user_name))
elif choice==6:
    os.system("date")
elif choice==7:
    os.system("date")
else:
    print('Option not available')
print("-"*80, end='\n')