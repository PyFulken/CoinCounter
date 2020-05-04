#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#My 1st attempt at creating code to find the minimum coins to give in change.......
Total = 5.00 #Total is the amount payed
Price = 3.37 #Price is the amount owed
Coins = [2.00,1.00,0.50,0.20,0.10,0.05,0.02,0.01] #Lista de moedas existentes
CoinsUsed = {"2€":0,"1€":0,"0.50€":0,"0.20€":0,"0.10€":0,"0.05€":0,"0.02€":0,"0.01€":0}
Iteration = 0
Owed = Total - Price
print(Owed)
while Owed != 0 and Owed > 0:
    while Owed > Coins[Iteration]:
        Owed -= Coins[Iteration]
        CoinsUsed["2€"]+=1
    else
        Iteration+=1
    while Owed > Coins[Iteration]:
        Owed -= Coins[Iteration]
        CoinsUsed["1€"]+=1
    else
        Iteration+=1
    while Owed > Coins[Iteration]:
        Owed -= Coins[Iteration]
        CoinsUsed["0.50€"]+=1
    else
        Iteration+=1
    while Owed > Coins[Iteration]:
        Owed -= Coins[Iteration]
        CoinsUsed["0.20€"]+=1
    else
        Iteration+=1
    while Owed > Coins[Iteration]:
        Owed -= Coins[Iteration]
        CoinsUsed["0.10€"]+=1
    else
        Iteration+=1
    while Owed > Coins[Iteration]:
        Owed -= Coins[Iteration]
        CoinsUsed["0.05€"]+=1
    else
        Iteration+=1
    while Owed > Coins[Iteration]:
        Owed -= Coins[Iteration]
        CoinsUsed["0.02€"]+=1
    else
        Iteration+=1
    while Owed > Coins[Iteration]:
        Owed -= Coins[Iteration]
        CoinsUsed["0.01€"]+=1
    else
        Iteration+=1
else
    print("The number of coins used was:\n%s moedas de 2€;\n%s moedas de 1€;\n%s moedas de 0.50€;\n%s moedas de 0.20€;\n%s moedas de 0.10€;\n%s moedas de 0.05€;\n%s moedas de 0.02€;\n%s moedas de 0.01€;"%(CoinsUsed["2€"],CoinsUsed["1€"],CoinsUsed["0.50€"],CoinsUsed["0.20€"],CoinsUsed["0.10€"],CoinsUsed["0.05€"],CoinsUsed["0.02€"],CoinsUsed["0.01€"]))

#DOES NOT WORK


# In[ ]:


#My 2nd attempt at creating code to find the minimum coins to give in change.
Total = 5.00 #Total is the amount payed
Price = 3.37 #Price is the amount owed
Coins = [2.00,1.00,0.50,0.20,0.10,0.05,0.02,0.01] #Lista de moedas existentes
CoinsUsed = {"2€":0,"1€":0,"0.50€":0,"0.20€":0,"0.10€":0,"0.05€":0,"0.02€":0,"0.01€":0} #Database to store amount used
Iteration = 0 #Iteration counter?
Owed = Total - Price
print(Owed)
while Owed != 0 and Owed > 0:
    while Owed > Coins[0]:
        Owed -= Coins[0]
        CoinsUsed["2€"]+=1
    else:
        Iteration+=1
    while Owed > Coins[Iteration]:
        Owed -= Coins[Iteration]
        CoinsUsed["1€"]+=1
    else:
        Iteration+=1
    while Owed > Coins[Iteration]:
        Owed -= Coins[Iteration]
        CoinsUsed["0.50€"]+=1
    else:
        Iteration+=1
    while Owed > Coins[Iteration]:
        Owed -= Coins[Iteration]
        CoinsUsed["0.20€"]+=1
    else:
        Iteration+=1
    while Owed > Coins[Iteration]:
        Owed -= Coins[Iteration]
        CoinsUsed["0.10€"]+=1
    else:
        Iteration+=1
    while Owed > Coins[Iteration]:
        Owed -= Coins[Iteration]
        CoinsUsed["0.05€"]+=1
    else:
        Iteration+=1
    while Owed > Coins[Iteration]:
        Owed -= Coins[Iteration]
        CoinsUsed["0.02€"]+=1
    else:
        Iteration+=1
    while Owed > Coins[Iteration]:
        Owed -= Coins[Iteration]
        CoinsUsed["0.01€"]+=1
    else:
        Iteration+=1
else:
    print("The number of coins used was:\n%s moedas de 2€;\n%s moedas de 1€;\n%s moedas de 0.50€;\n%s moedas de 0.20€;\n%s moedas de 0.10€;\n%s moedas de 0.05€;\n%s moedas de 0.02€;\n%s moedas de 0.01€;"%(CoinsUsed["2€"],CoinsUsed["1€"],CoinsUsed["0.50€"],CoinsUsed["0.20€"],CoinsUsed["0.10€"],CoinsUsed["0.05€"],CoinsUsed["0.02€"],CoinsUsed["0.01€"]))

#RUNS BUT INDEX ERROR ON LINE 15, OUT OF RANGE


# In[ ]:


#My 3rd attempt at creating code to find the minimum coins to give in change.
Total = 5.00 #Total is the amount payed
Price = 3.37 #Price is the amount owed
Coins = [2.00,1.00,0.50,0.20,0.10,0.05,0.02,0.01] #Lista de moedas existentes
CoinsUsed = {"2€":0,"1€":0,"0.50€":0,"0.20€":0,"0.10€":0,"0.05€":0,"0.02€":0,"0.01€":0} #Database to store amount used
Iteration = 0 #Iteration counter?
Owed = Total - Price
while Owed != 0 and Owed > 0:
    while Owed > Coins[0]:
        Owed -= Coins[0]
        CoinsUsed["2€"]+=1
    else:
        Iteration+=1
    while Owed > Coins[1]:
        Owed -= Coins[1]
        CoinsUsed["1€"]+=1
    else:
        Iteration+=1
    while Owed > Coins[2]:
        Owed -= Coins[2]
        CoinsUsed["0.50€"]+=1
    else:
        Iteration+=1
    while Owed > Coins[3]:
        Owed -= Coins[3]
        CoinsUsed["0.20€"]+=1
    else:
        Iteration+=1
    while Owed > Coins[4]:
        Owed -= Coins[4]
        CoinsUsed["0.10€"]+=1
    else:
        Iteration+=1
    while Owed > Coins[5]:
        Owed -= Coins[5]
        CoinsUsed["0.05€"]+=1
    else:
        Iteration+=1
    while Owed > Coins[6]:
        Owed -= Coins[6]
        CoinsUsed["0.02€"]+=1
    else:
        Iteration+=1
    while Owed > Coins[7]:
        Owed -= Coins[7]
        CoinsUsed["0.01€"]+=1
    else:
        Iteration+=1
else:
    print("The number of coins used was:\n%s moedas de 2€;\n%s moedas de 1€;\n%s moedas de 0.50€;\n%s moedas de 0.20€;\n%s moedas de 0.10€;\n%s moedas de 0.05€;\n%s moedas de 0.02€;\n%s moedas de 0.01€;"%(CoinsUsed["2€"],CoinsUsed["1€"],CoinsUsed["0.50€"],CoinsUsed["0.20€"],CoinsUsed["0.10€"],CoinsUsed["0.05€"],CoinsUsed["0.02€"],CoinsUsed["0.01€"]))

#RUNS INFINITE AGAIN


# In[ ]:


#My 4th attempt at creating code to find the minimum coins to give in change.
Total = 5.00 #Total is the amount payed
Price = 3.37 #Price is the amount owed
Coins = [2.00,1.00,0.50,0.20,0.10,0.05,0.02,0.01] #Lista de moedas existentes
CoinsUsed = {"2€":0,"1€":0,"0.50€":0,"0.20€":0,"0.10€":0,"0.05€":0,"0.02€":0,"0.01€":0} #Database to store amount used
Iteration = 0 #Iteration counter? 
TotalCoins = 0
Owed = Total - Price
print("The total change owed is:", Owed)
while Owed >= Coins[Iteration]:
    Owed -= Coins[Iteration]
    CoinsUsed["2€"]+=1
else:
    Iteration +=1
while Owed >= Coins[Iteration]:
    Owed -= Coins[Iteration]
    CoinsUsed["1€"]+=1
else:
    Iteration +=1
while Owed >= Coins[Iteration]:
    Owed -= Coins[Iteration]
    CoinsUsed["0.50€"]+=1
else:
    Iteration +=1
while Owed >= Coins[Iteration]:
    Owed -= Coins[Iteration]
    CoinsUsed["0.20€"]+=1
else:
    Iteration +=1
while Owed >= Coins[Iteration]:
    Owed -= Coins[Iteration]
    CoinsUsed["0.10€"]+=1
else:
    Iteration +=1
while Owed >= Coins[Iteration]:
    Owed -= Coins[Iteration]
    CoinsUsed["0.05€"]+=1
else:
    Iteration +=1
while Owed >= Coins[Iteration]:
    Owed -= Coins[Iteration]
    CoinsUsed["0.02€"]+=1
else:
    Iteration +=1
while Owed >= Coins[Iteration]:
    Owed -= Coins[Iteration]
    CoinsUsed["0.01€"]+=1
else:
    Iteration +=1

TotalCoins = CoinsUsed["2€"] + CoinsUsed["1€"] + CoinsUsed["0.50€"] + CoinsUsed["0.20€"] + CoinsUsed["0.10€"] + CoinsUsed["0.05€"] + CoinsUsed["0.02€"] + CoinsUsed["0.01€"]
print("The number of coins used was:\n%s moedas de 2€;\n%s moedas de 1€;\n%s moedas de 0.50€;\n%s moedas de 0.20€;\n%s moedas de 0.10€;\n%s moedas de 0.05€;\n%s moedas de 0.02€;\n%s moedas de 0.01€;\nThe total of coins used for change is: %s"%(CoinsUsed["2€"],CoinsUsed["1€"],CoinsUsed["0.50€"],CoinsUsed["0.20€"],CoinsUsed["0.10€"],CoinsUsed["0.05€"],CoinsUsed["0.02€"],CoinsUsed["0.01€"],TotalCoins))

#WORKSSSSSSSSSSSSSSSS!!!!!!!!!!!!!!!!!!!! But it's missing 1 cent


# In[25]:


#My 5th attempt at creating code to find the minimum coins to give in change.
InputTotal = 20.57 #InputTotal is the amount payed, inserted by the user
Total = int(InputTotal*100) #Total is the amount payed turned into int for bug reasons
InputPrice = 3.37 #InputPrice is the amount owed, inserted by the user
Price = int(InputPrice*100)
Coins = [200,100,50,20,10,5,2,1] #Lista de moedas existentes
CoinsUsed = {"2€":0,"1€":0,"0.50€":0,"0.20€":0,"0.10€":0,"0.05€":0,"0.02€":0,"0.01€":0} #Database to store amount used
Iteration = 0 #Iteration counter to change the position used in the Dict 
TotalCoins = 0 #Self-explanatory
Owed = Total - Price
print("The total change owed is:", Owed/100)
while Owed >= Coins[Iteration]:
    Owed -= Coins[Iteration]
    CoinsUsed["2€"]+=1
else:
    Iteration +=1
while Owed >= Coins[Iteration]:
    Owed -= Coins[Iteration]
    CoinsUsed["1€"]+=1
else:
    Iteration +=1
while Owed >= Coins[Iteration]:
    Owed -= Coins[Iteration]
    CoinsUsed["0.50€"]+=1
else:
    Iteration +=1
while Owed >= Coins[Iteration]:
    Owed -= Coins[Iteration]
    CoinsUsed["0.20€"]+=1
else:
    Iteration +=1
while Owed >= Coins[Iteration]:
    Owed -= Coins[Iteration]
    CoinsUsed["0.10€"]+=1
else:
    Iteration +=1
while Owed >= Coins[Iteration]:
    Owed -= Coins[Iteration]
    CoinsUsed["0.05€"]+=1
else:
    Iteration +=1
while Owed >= Coins[Iteration]:
    Owed -= Coins[Iteration]
    CoinsUsed["0.02€"]+=1
else:
    Iteration +=1
while Owed >= Coins[Iteration]:
    Owed -= Coins[Iteration]
    CoinsUsed["0.01€"]+=1
else:
    Iteration +=1
TotalCoins = CoinsUsed["2€"] + CoinsUsed["1€"] + CoinsUsed["0.50€"] + CoinsUsed["0.20€"] + CoinsUsed["0.10€"] + CoinsUsed["0.05€"] + CoinsUsed["0.02€"] + CoinsUsed["0.01€"]
print("The number of coins used was:\n%s moedas de 2€;\n%s moedas de 1€;\n%s moedas de 0.50€;\n%s moedas de 0.20€;\n%s moedas de 0.10€;\n%s moedas de 0.05€;\n%s moedas de 0.02€;\n%s moedas de 0.01€;\nThe total of coins used for change is: %s"%(CoinsUsed["2€"],CoinsUsed["1€"],CoinsUsed["0.50€"],CoinsUsed["0.20€"],CoinsUsed["0.10€"],CoinsUsed["0.05€"],CoinsUsed["0.02€"],CoinsUsed["0.01€"],TotalCoins))

#WORKSSSSSSSSSSSSSSSS!!!!!!!!!!!!!!!!!!!!


# In[3]:


#My 6th attempt at creating code to find the minimum coins to give in change, without loops.
Troco = 1249
DoisEuros = int(Var/200)
UmEuro = int((Var-(200*DoisEuros))/100)
Cinquenta = int((Var-(200*DoisEuros)-(100*UmEuro))/50)
Vinte = int((Var-(200*DoisEuros)-(100*UmEuro)-(50*Cinquenta))/20)
Dez = int((Var-(200*DoisEuros)-(100*UmEuro)-(50*Cinquenta)-(20*Vinte))/10)
Cinco = int((Var-(200*DoisEuros)-(100*UmEuro)-(50*Cinquenta)-(20*Vinte)-(10*Dez))/5)
Dois = int((Var-(200*DoisEuros)-(100*UmEuro)-(50*Cinquenta)-(20*Vinte)-(10*Dez)-(5*Cinco))/2)
Um = int((Var-(200*DoisEuros)-(100*UmEuro)-(50*Cinquenta)-(20*Vinte)-(10*Dez)-(5*Cinco)-(2*Dois))/1)
print("O troco é:", Troco/100)
print("Moedas de dois euros usadas:", DoisEuros)
print("Moedas de um euro usadas:", UmEuro)
print("Moedas de cinquenta centimos usadas:", Cinquenta)
print("Moedas de vinte centimos usadas:", Vinte)
print("Moedas de dez centimos usadas:", Dez)
print("Moedas de cinco centimos usadas:", Cinco)
print("Moedas de dois centimos usadas:", Dois)
print("Moedas de um centimo usadas:", Um)


# In[11]:


#My 7th attempt at creating code to find the minimum coins to give in change, without loops, more concise.
Preço = 55
Pago = 57.01
Troco = (Pago*100)-(Preço*100)
print("O troco é:", Troco/100)
VinteNota = int(Troco/2000)
Troco -= 2000*VinteNota
DezNota = int(Troco/1000)
Troco -= 1000*DezNota
CincoNota = int(Troco/500)
Troco -= 500*CincoNota
DoisEuros = int(Troco/200)
Troco -= 200*DoisEuros
UmEuro = int(Troco/100)
Troco -= 100*UmEuro
Cinquenta = int(Troco/50)
Troco -= 50*Cinquenta
Vinte = int(Troco/20)
Troco -= 20*Vinte
Dez = int(Troco/10)
Troco -= 10*Dez
Cinco = int(Troco/5)
Troco -= 5*Cinco
Dois = int(Troco/2)
Troco -= 2*Dois
Um = int(Troco/1)
print("Notas de 20 euros usadas:", VinteNota)
print("Notas de 10 euros usadas:", DezNota)
print("Notas de 5 euros usadas:", CincoNota)
print("Moedas de dois euros usadas:", DoisEuros)
print("Moedas de um euro usadas:", UmEuro)
print("Moedas de cinquenta centimos usadas:", Cinquenta)
print("Moedas de vinte centimos usadas:", Vinte)
print("Moedas de dez centimos usadas:", Dez)
print("Moedas de cinco centimos usadas:", Cinco)
print("Moedas de dois centimos usadas:", Dois)
print("Moedas de um centimo usadas:", Um)


# In[15]:


#My 8th attempt at creating code to find the minimum coins to give in change, without loops, 
#WITH THE POWER OF FUUUUUUUUNCTIOOOONS.
def coin_counter_function(CurrentChange,CurrentCoin):
    AmountOfCoins = int(CurrentChange/CurrentCoin)
    CurrentChange -= CurrentCoin*AmountOfCoins
    return AmountOfCoins
while coin_counter_function(1000,50)


# In[16]:


def coin_counter_function(CurrentChange,CurrentCoin):
    AmountOfCoins = int(CurrentChange/CurrentCoin)
    CurrentChange -= CurrentCoin*AmountOfCoins
    return AmountOfCoins,CurrentChange

coins,change = coin_counter_function(500,50)

print(coins)
print(change)


# In[ ]:




