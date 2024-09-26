mincharge = 35
freecharacters = 5
numChars = 8
woodType = 20
color = 15
charge = 0

numChars = int(input("How many characters are in your sign? "))
woodType = input("What type of wood? ")
color = input("What color? ")

if numChars > freecharacters: 
  numChars = numChars - freecharacters


if woodType == "oak":
  charge = charge + 20


if color == "gold":
  charge = charge + 15
  
  
charge = numChars * 4 + mincharge + charge
  
print("Your sign will cost $", charge) 