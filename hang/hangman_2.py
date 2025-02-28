# importing random module
import random

# importing hangman patterns from hangman_pics file
from hangman_pics import hangman

#defining list of fruits
mylist=["apple","banana","orange","watermelon","kiwi"]

#initializing variable for storing no:of attempts
count_temp=0


word=random.choice(mylist)
length=len(word)
print(hangman[0])
dash_list=[" ___ ,"]*length
print(dash_list)

def get_from_user():
    global guess
    print("it is a fruit,guess it")
    guess=input("enter your guess")
    is_present(guess)

def is_present(guess):
    global count_temp
    if guess in word:
        for i,j in enumerate(word):
            if word[i]==guess:
                dash_list[i]=guess
                count_temp+=0
        print(dash_list)             
    else:
        count_temp+=1
        if (" ___ ," in dash_list) and count_temp!=6:
            printing_hangman(count_temp)
            get_from_user()
        elif (" ___ ," in dash_list) and count_temp==6: 
            printing_hangman(count_temp)
            print("\n you lost")
            exit()
    
def printing_hangman(count_temp):
        print(hangman[count_temp])
   

while count_temp<length:
    get_from_user()
    if " ___ ," not in dash_list:
        print("you win")
        break
    



    
        
