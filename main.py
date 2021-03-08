# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player_that_also_scored = "Marco van Basten"
player_that_scored = "Ruud Gullit"
goal_1 = 32
goal_2 = 54
scorers = (player_that_scored + " " +
           str(goal_1) + " " + "and" + " " + player_that_also_scored + " " + str(goal_2))


report = (f"{player_that_scored} scored in the {goal_1}nd minute \n {player_that_also_scored} scored in the {goal_2}th minute")
print(report)

player = "kees kist"
x = player.find("kees")


first_name_slice = slice(0, 4)
first_name = (player[first_name_slice])

y = player.find("kist")

last_name_slice = slice(5, 9)
last_name = (player[last_name_slice])


name_short = first_name[0] + last_name

chant = (first_name + "!")*3
print(chant)
