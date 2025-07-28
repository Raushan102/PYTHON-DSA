#https://leetcode.com/problems/robot-return-to-origin/
def judgeCircle( moves):
    ud=0 # track up and down
    rl=0 # track left anf right

    for item in moves:
        if item == "U": # track up moves
            ud+=1
        elif item=="D": # track down moves
            ud-=1
        elif item=="L": # track left moves
            rl+=1
        else:            # track right moves
            rl-=1
    if ud== 0 and rl==0: # check weather we are at initial position or not
        return True
    else:
        return False



print(judgeCircle("LL"))