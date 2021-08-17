

print ("Welcome To My Soccer Quiz challenge")
response =input("Would you like to play? ")

if response.lower() != "yes":
    print("Quiz cancelled")
    quit()

print("okay, let the challenge begin! ")

score = 0
answer = input("who is the current coach for Chelsea? ")
if answer.lower()== "thomas tuchel":
    print("correct! ")
    score+=1
else:
    print("incorrect, sorry  the correct answer is Thomas Tuchel !")
    


answer = input("who is the best player in EPL for the last season? ")
list = ["kevin de bruyne","mason mount","kai harvetz", "phil foden", "raheem sterling","n'golo kante"]
if answer.lower() in list:
    print("correct! ")
    score+=1
else:
    print(f"incorrect, sorry the correct answer can be one of {list}! ")
    
    
answer = input("which International team won the copa america ")
if answer.lower()== "argentina":
    print("correct! ")
    score+=1
else:
    print("incorrect, sorry  the correct answer is Argentina!")
    

answer = input("which Interantional team won the Euro world cup 2020? ")
if answer.lower()== "italy":
    print("correct! ")
    score+=1
else:
    print("incorrect, sorry the correct answer is Italy!")
    

answer = input("who is the top goal scorer in EPL for the previous season? ")
if answer.lower()== "harry kane":
    print("correct! ")
    score+=1
else:
    print("incorrect, sorry !")

answer = input("which player has received more balon dor's? ")
if answer.lower()== "lionel messi":
    print("correct! ")
    score+=1
else:
    print("incorrect, sorry the correct answer is Lionel Messi!")

print("Hint, give second names only For the question below: " )

answer = input("which player has more than  600 goals for one club? ")
players = ["messi", "ronaldo","pele","romario","bican"]
if answer.lower() in players:
    print("correct! ")
    score+=1
else:
    print(f"incorrect, sorry  the correct answer is one of {players}!")
    
answer = input("which team won the EUFA Champions League in the year 2018? ")
if answer.lower()== "real madrid":
    print("correct! ")
    score+=1
else:
    print("incorrect, sorry  the correct answer is Real Madrid!")

answer = input("which international team won the latest world cup ")
if answer.lower()== "france":
    print("correct! ")
    score+=1
else:
    print("incorrect, sorry  the correct answer is France!")

answer = input("which team won the Europa League season 2020-2021 ")
if answer.lower()== "villareal":
    print("correct! ")
    score+=1
else:
    print("incorrect, sorry  the correct answer is Villareal!")

answer = input("which team played the EUFA Champions League finals season 2020-2021 ")
teams =["manchester city", "chelsea"] 
if answer.lower() in teams:
    print("correct! ")
    score+=1
else:
    print("incorrect, sorry  the correct answer is either Chelsea or Manchester city !")
    
    
    
    
print ("congratulations, you got " + str (score) +  " out of 11")
print("congratulations, you got " +str ((score/11 )* 100) + " % ")
    
