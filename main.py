from play2 import ClipObj, play

# Create ClipObj array
a = ClipObj(0, .33, 1)
b = ClipObj(-1, .33, 0)
c = ClipObj(0, .33, 0)

arr= [a, b, c, b]
arr2= [a, b, a, b]
arr = arr + arr2
arr = arr*4

fouronthefloor = [c, b, c, b, c, b, c, b]
fourbyfour = fouronthefloor*4

play(fourbyfour)