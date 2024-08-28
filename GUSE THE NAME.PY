import random



while True:

    letters=("a","b","c","d","e","f","g","h","i","j","k","l","m","o","p","q","r","s","t","w","x","y","z")
    letter = input("Guse a letters a-z\n")
    computer =random.choice(letters)
    
    
    print(f"The computer chose:{computer}")
    print(f"You chose:{letter}")
    
        
    if letter == computer:
        print("Yeha its a match")
        break
    
    else:
        print("Not a match")
        
        

        