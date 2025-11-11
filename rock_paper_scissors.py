# Write code below 💖
import random
player = 0
computer = random.randint(1,5)
whoWin = 1 # 1:person  2:cpus 3:tie
options = ["✊","✋","✌️","🦎","🖖"]


print("================================")
print("Rock Paper Scissors Lizard Spock")
print("================================")
print("1) ✊")
print("2) ✋")
print("3) ✌️")
print("4) 🦎")
print("5) 🖖")

while player < 1 or player > 5:
  player = int(input('Pick a number please: '))

if player == computer:
  whoWin = 3

elif player == 1:
  if computer == 2 or computer == 5:
    whoWin = 2

elif player == 2:
  if computer == 3 or computer == 4:
    whoWin = 2

elif player == 3:
  if computer == 1 or computer == 5:
    whoWin = 2

elif player == 4:
  if computer == 1 or computer == 3:
    whoWin = 2

elif player == 5:
  if computer == 4 or computer == 2:
    whoWin = 2

print("You chose: "+options[player-1])
print("CPU chose: "+options[computer-1])


if whoWin == 1:
  print('You win!')
elif whoWin == 2:
  print('CPU win!')
else:
  print("It's a tie!")
