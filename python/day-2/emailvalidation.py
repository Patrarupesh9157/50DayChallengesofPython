email = input('Enater your Email address : ')
k= 0
j = 0
d=0
if len(email) >= 6:
    if email[0].isalpha():
        if ('@' in email) and email.count('@') <=1:
            for i in email:
                if i==i.isspace():
                    k=1
                elif i.isalpha():
                    if i==i.upper():
                        j=1
                elif i.isdigit():
                    continue 
                elif i=="_" or i=="." or i== "@":
                    continue
                else :
                    d=1
            if k== 1 or j== 1:
                print('Wrong Email')
            else :
                print('Your email is correct')
        else :
            print('Wrong Email')
    else :
        print('Wrong Email')
else :
    print('Wrong Email')
