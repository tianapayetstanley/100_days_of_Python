line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
ABC = str(position[0]).lower()
num = int(position[1])
abc = ["a","b","c"]
letter_index = abc.index(ABC)
num_index = num - 1
map[num_index][letter_index]=("X")


  



# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")