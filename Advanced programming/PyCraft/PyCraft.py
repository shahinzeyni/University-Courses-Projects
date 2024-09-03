
# from mcpi_e.minecraft import *
# from mcpi_e.block import *

# serverAddres = "mc.yasan.ac"
# player = 'Shahin'
# port = 29015
# mc = Minecraft.create(serverAddres,port,player)

# # mc.postToChat('41564')
# xp,yp,zp = mc.player.getPos()

# # for z in range(5):
# #     for x in range(5):
# #         for y in range(5):
# #             mc.setBlock(xp+x,yp+y,zp+z,GOLD_BLOCK)

# # for z in range(1, 100, 2):
# #     for y in range(1, 100, 2):
# #         for x in range(1, 100, 2):
# #             mc.setBlock(xp+x, yp+y, zp+z, GOLD_BLOCK)

# for y in range(10):
#     for x in range(10-y*2):
#         mc.setBlock(x+y+xp, y+yp,zp, GOLD_BLOCK)

# # mc.setBlock(xp,yp,zp,GOLD_BLOCK)
# x = 1

# def f_1():
#     global x
#     x = 2
#     print(x)

# f_1() #2
# print(x)



import random
n = random.randrange(0,10)
print(n)

f = 'no'

while  f == 'no' :
    a = int(input('enter:'))
    if a < n :
        print('>')
    elif a > n:
        print('<')
    else:
        print('correct')
        f = 'yes'

print('Thank you.')     