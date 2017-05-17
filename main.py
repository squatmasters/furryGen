import random

User_name = input("What is your name, my throbbing friend?")

noun1 = [ 'star', 'keyboard', 'electricity', 'calculator', 'asian', 'hersheybar', 'youtube', 'sister', 'politician', 'smallchild' ]
body1 = [ 'face', 'elbow', 'tooth', 'arm', 'navel', 'throat', 'knife', 'eye', 'regret', 'toenail', 'asian' ]
noun2 = [ 'paper', 'skin', 'asian', 'number', 'lcd', 'lsd', 'profile', 'regret', 'mistake' ]
anim1 = [ 'cat', 'beaver', 'beaver', 'beaver', 'beaver', 'beaver', 'beaver', 'beaver', 'beaver', 'beaver', 'beaver', 'beaver', 'beaver', 'beaver', 'beaver', 'beaver', 'asian', 'starfish', 'waterbear' ]

io = random.randint(0, len(noun1)-1)
ip = random.randint(0, len(body1)-1)
il = random.randint(0, len(noun2)-1)
ik = random.randint(0, len(anim1)-1)





print("you're furry name is" , User_name, "the", noun1[io] + body1[ip] , noun2[il] + anim1[ik])
