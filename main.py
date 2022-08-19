from replit import clear

import art

print(art.logo)
print("Bienvenido al programa de subasta secreta")

pujas = {}

restart = True
while restart:
  name = input("¿Cuál es tu nombre?: ")
  bid = int(input("¿Cuánto ofreces?: $"))

  pujas[name] = bid

  answer = input("¿Hay otros compradores? Escribe 'si' o 'no'.\n")

  if answer == "no":
    restart = False

  clear()

max_bid = 0
winner = ""

for bidder in pujas:

  if pujas[bidder] > max_bid:
    max_bid = pujas[bidder]
    winner = bidder

print(f"El ganador es {winner} con una puja de ${max_bid}.")