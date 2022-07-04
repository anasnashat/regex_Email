import re


Email_list = ['anas_nashat.eg@gmail.com' , 'anas_nashat.eg@yahoo.edu' , 'anas_nashat.eg@yahoo.com','anas_nashat.eg@outlook.edu' , '.@gmail.com']

def check_email(email):
    is_email= re.search(r'^[A-z0-9]{1,}[\.-]?[A-z0-9]{1,}@\w+\.\w{2,3}$' , email)

    if is_email:
        print(f'{email} is valid email')
    else:
        print(f'{email} not valid')

for em in Email_list:
    check_email(em)
