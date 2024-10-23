email = input("enter your Email : ")#gag.in
if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if(email[-4] == ".") ^ (email[-3] == "."):
                pass
            else:
                print("wrong Email 4")

        else:
            print("wrong Email 3")
    else:
        print('wrong email 2')
else:
    print("Wrong Email 1")