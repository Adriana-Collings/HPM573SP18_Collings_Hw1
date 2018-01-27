yours = ["Yale", "MIT", "Berkeley"]
mine = ["ColoradoState", "Yale", "Princeton"]
ours1 = yours+mine
ours2 = []
ours2.append(mine)
ours2.append(yours)
print("ours1:", ours1)
print("ours2:", ours2)
# These differ in that for ours1, it is one whole list that has been combined
# and for ours2, the two lists still maintain their own properties
# and the order is different

mine[1]="Harvard"
print("ours1:", ours1)
print("ours2:", ours2)
# this changes ours2 because as said above when you append the lists like we did
# for ours2 the lists still maintain their own properties but when you concatenate
# the lists like we did for ours1, ours1 becomes its own list that would
# have to be manipulated in the same way 'mine' was manipulated
