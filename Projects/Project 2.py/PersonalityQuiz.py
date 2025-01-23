# Beginning:
sports_points = 0
board_points = 0



# Middle:
answer = input ("On a weekend would you rather A) Play sports all day, or B) Play Boardgames?")
if answer == "A":
    sports_points += 1   
elif answer == "B":
    board_points += 1  


answer = input ("What would you want to play Professionally A) Basketball, B) Soccer/Football?")
if answer == "A":
    sports_points += 1
if answer == "B":
    sports_points += 1
  

answer = input ("Would you rather be A) in a group, B) alone?")
if answer == "A":
    sports_points += 1
if answer == "B":
    board_points += 1


answer = input ("Which board game do you prefer A) Monopoly, B) Any card game?")
if answer == "A":
    board_points += 1
if answer == "B":
    board_points += 1

answer = input ("Would you rather A) Go outside, B) Stay inside?")
if answer == "A":
    sports_points += 1
if answer == "B":
    board_points += 1


answer = input ("Would you rather A) Work out, B) Play video games?")
if answer == "A":
    sports_points += 1
if answer == "B":
    board_points += 1


answer = input ("Would you rather be A) Relaxed, B) Energized?")
if answer == "A":
    sports_points += 1
if answer == "B":
    board_points += 1


answer = input ("Would you rather A) Play any EA sports game, B) Play Shooter games?")
if answer == "A":
    sports_points += 1
if answer == "B":
    board_points += 1


answer = input ("Would you rather A) Spend time with family, B) Spend time with friends?")
if answer == "B":
    sports_points += 1
if answer == "A":
    board_points += 1


answer = input ("Would you rather A) watch Ted Lasso, B) Watch Lab rats?")
if answer == "A":
    sports_points += 1
if answer == "B":
    board_points += 1


# End:
percent_sports = sports_points/10
percent_board = board_points/10
if sports_points > board_points:
    print ("You are a Sports person by")
    print(percent_sports/0.01)
if board_points > sports_points:
    print ("You are a board game person by")
    print(percent_board/0.01)
elif sports_points == board_points:
    print ("You are a 50/50 mix!")
    
    


