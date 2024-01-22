thickness = int(input()) #This must be an odd number
c = 'A'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness+6)+c+(c*i).ljust(thickness+8))

# #Top Pillars
# for i in range(thickness+5):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*4))
# #Middle Belt
# for i in range((thickness+1)//2):
#     print((c*thickness*5).center(thickness*6))

# #Bottom Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    
    
# #Bottom Cone
# for i in range(thickness):
#     print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))a5
4
