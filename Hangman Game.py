import random
with open('sample','r') as f:
    words = f.readlines()

word=random.choice(words)[:-1]


#word ="rakesh"
allowed_time= len(word)+1
guess=[]
done = False
print("Enter your name : " ,)
print(f"HI  {input()} Wellcome To This Game!!...")
print("It is so excited to see you !!!")
print("Lets Play !!!......")
print(f"You have {allowed_time-1} letter word ....Guess it !!")
print()

while not done :
    for letter in word :
        if letter.lower() in guess:
            print(letter,end=" ")
        else:
            print("*",end=" ")
    print("")


    x =input(f"Chance left {allowed_time},Next guess : ")
    guess.append((x.lower()))
    if x.lower() not in word.lower():
        allowed_time-=1
        if allowed_time==0:
            break
    done = True
    for letter in word:
        if letter.lower() not in guess:
            done= False
if done:
    print("You found word :" ,word)
else:
    print("Time over ")
    print("This word is :",word)