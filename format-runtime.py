#String formating
w="welcome {} to {} servicepack".format("Anwar",34)
print(w)

w="welcome {1} to {0} servicepack".format("Anwar",34)
print(w)

w="welcome {a:^10} to {b:>5} servicepack".format(a=35,b=20)
print(w) 