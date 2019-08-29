import random

def choose():
    words =  ["failure","customer","album","tick","architect","scrap","cabinet","qualify","interest","zero"]
    pick = random.choice(words)
    return pick
def jumble(word):
    jumble = "".join(random.sample(word,len(word)))
    return jumble
def thank(p1n,p2n,p1,p2):
    print(p1n," Your Score is ",p1)
    print(p2n," Your Score is ",p2)
    print("Thank you for playing this game with me")

def play():
    p1name = input("Enter the first player name ")
    p2name = input("Enter the second player name ")
    pp1=0
    pp2=0
    turn = 0
    while(1):
        picked_word = choose()
        qn = jumble(picked_word)
        print(qn)
        if turn%2==0:
            print(p1name,"Your Turn")
            ans = input("What is on ur mind")
            if ans == picked_word:
                pp1 = pp1+1
                print("You guessed it right!!!")
                print(pp1)
            else:
                print("The word on my mind was ",picked_word)
                print("Better luck next time")
            c = int(input("press 1 to continue and 0  to exit"))
            if c == 0:
                thank(p1name,p2name,pp1,pp2)
                break
        if turn%2 ==1:
            print(p2name,"Your Turn")
            ans = input("What is on ur mind")
            if ans == picked_word:
                pp2 = pp2+1
                print("You guessed it right")
                print(pp2)
            else:
                print("Better luck next time")
            c = int(input("press 1 to continue and 0  to exit"))
            if c == 0:
                thank(p1name,p2name,pp1,pp2)
                break
        turn = turn + 1
play()

