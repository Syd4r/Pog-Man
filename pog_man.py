import random
#import termcolor
import time
#bugs/things to do
#turn the movement into a function for crying out loud..no/when i do this, also do the same for enemies wwwwwwaaaaaaaaa
while True:
    Alive = True
    score = 0
    num_of_enemies = 3
    thing = 5
    extra_life = 0
    saved_items = []
    current_items = []
    player_last_pos = 4
    multiplier_increased = 1
    live_chance = 0
    reroll = False
    #list of things needed to do
    #add more items
    # passive items
    #make more uniquness to the levels
    def enemy_moves (enemy_pos, last_saved, enemy_stunned, stuns_left, score, thing):
        global current_items
        ways_to_go = []
        ways = []
        dist = 0
        dire = "f"
        do = False
        rand = random.randint(1, 10)
        if moved == True:
            if (cells[enemy_pos] == 2) and (enemy_stunned == False):
                score += 50
                enemy_stunned = True
                stuns_left = stun_num
                last_saved = 4
            elif enemy_stunned == True:
                if stuns_left == 0:
                    if invincibility > 0 and cells[enemy_pos] == 2:
                        score += 50
                        stuns_left = stun_num
                    else:
                        cells[enemy_pos] = 3
                        enemy_stunned = False
                else:
                    stuns_left -= 1
            elif (rand < 5+thing):
                if not (cells[enemy_pos - 19] == 1 or cells[enemy_pos - 19] == 3 or cells[enemy_pos - 19] == 9):
                    if cells[enemy_pos - 19] == 2 and invincibility > 0:
                        pass
                    else:
                        do = True
                        continue1 = False
                        continue2 = False
                        ways_to_go.append("w")
                        enemy_r_temp = enemy_pos - 19
                        current_temp = current_pos
                        while True:
                            if enemy_r_temp > 18:
                                enemy_r_temp -= 19
                                dist += 1
                            else:
                                continue1 = True
                            if current_temp > 18:
                                current_temp -= 19
                                dist -= 1
                            else:
                                continue2 = True
                            if continue1 == True and continue2 == True:
                                dist = abs(dist)
                                dist += abs(enemy_r_temp - current_temp)
                                ways.append(dist)
                                break
                dist = 0
                if not (cells[enemy_pos - 1] == 1 or cells[enemy_pos - 1] == 3 or cells[enemy_pos - 1] == 9):
                    if cells[enemy_pos - 1] == 2 and invincibility > 0:
                        pass
                    else:
                        do = True
                        continue1 = False
                        continue2 = False
                        ways_to_go.append("a")
                        enemy_r_temp = enemy_pos - 1
                        current_temp = current_pos
                        while True:
                            if enemy_r_temp > 18:
                                enemy_r_temp -= 19
                                dist += 1
                            else:
                                continue1 = True
                            if current_temp > 18:
                                current_temp -= 19
                                dist -= 1
                            else:
                                continue2 = True
                            if continue1 == True and continue2 == True:
                                dist = abs(dist)
                                dist += abs(enemy_r_temp - current_temp)
                                ways.append(dist)
                                break
                dist = 0
                if not (cells[enemy_pos + 19] == 1 or cells[enemy_pos + 19] == 3 or cells[enemy_pos + 19] == 9):
                    if cells[enemy_pos + 19] == 2 and invincibility > 0:
                        pass
                    else:
                        do = True
                        continue1 = False
                        continue2 = False
                        ways_to_go.append("s")
                        enemy_r_temp = enemy_pos + 19
                        current_temp = current_pos
                        while True:
                            if enemy_r_temp > 18:
                                enemy_r_temp -= 19
                                dist += 1
                            else:
                                continue1 = True
                            if current_temp > 18:
                                current_temp -= 19
                                dist -= 1
                            else:
                                continue2 = True
                            if continue1 == True and continue2 == True:
                                dist = abs(dist)
                                dist += abs(enemy_r_temp - current_temp)
                                ways.append(dist)
                                break
                dist = 0
                if not (cells[enemy_pos + 1] == 1 or cells[enemy_pos + 1] == 3 or cells[enemy_pos + 1] == 9):
                    if cells[enemy_pos + 1] == 2 and invincibility > 0:
                        pass
                    else:
                        do = True
                        continue1 = False
                        continue2 = False
                        ways_to_go.append("d")
                        enemy_r_temp = enemy_pos + 1
                        current_temp = current_pos
                        while True:
                            if enemy_r_temp > 18:
                                enemy_r_temp -= 19
                                dist += 1
                            else:
                                continue1 = True
                            if current_temp > 18:
                                current_temp -= 19
                                dist -= 1
                            else:
                                continue2 = True
                            if continue1 == True and continue2 == True:
                                dist = abs(dist)
                                dist += abs(enemy_r_temp - current_temp)
                                ways.append(dist)
                                break
                if do == True:
                    lowest = 100000000
                    highest = 0
                    for i in range(len(ways)):
                        if ways[i] < lowest:
                            lowest = ways[i]
                    for i in range(len(ways)):
                        ways[i] -= (lowest - 1)
                    for i in range(len(ways)):
                        if ways[i] > highest:
                            highest = ways[i]
                    for i in range(len(ways)):
                        ways[i] = ((highest + 1) - ways[i])
                    rand = random.randint(1, sum(ways))
                    for i in range(len(ways)):
                        if ways[i] >= rand:
                            dire = ways_to_go[i]
                            break
                        else:
                            ways[i + 1] += ways[i]
                if dire == "w":
                    cells[enemy_pos] = last_saved
                    enemy_pos -= 19
                    last_saved = cells[enemy_pos]
                    cells[enemy_pos] = 3
                if dire == "a":
                    cells[enemy_pos] = last_saved
                    enemy_pos -= 1
                    last_saved = cells[enemy_pos]
                    cells[enemy_pos] = 3
                if dire == "s":
                    cells[enemy_pos] = last_saved
                    enemy_pos += 19
                    last_saved = cells[enemy_pos]
                    cells[enemy_pos] = 3
                if dire == "d":
                    cells[enemy_pos] = last_saved
                    enemy_pos += 1
                    last_saved = cells[enemy_pos]
                    cells[enemy_pos] = 3
                if last_saved ==2:
                    last_saved = 0
        if last_saved == 7:
            last_saved = 4
            enemy_stunned = True
            stuns_left += 10000
        return enemy_pos, last_saved, enemy_stunned, stuns_left, score
    def choose_tele_use():
        global current_pos
        global cells
        while True:
            choose_1 = input("How far down do you want to move?: ")
            choose_2 = input("How far right do you want to move?: ")
            choose = (int(choose_1)-1)*19 + (int(choose_2)-1)
            if cells[int(choose)] == 0 or cells[int(choose)] == 4:
                cells[current_pos] = 4
                current_pos = int(choose)
                cells[int(choose)] = 2
                break
    def random_tele_use():
        global current_pos
        global cells
        while True:
            rand = random.randint(1,len(cells))
            if (cells[rand-1] == 0) or (cells[rand-1] == 4):
                cells[current_pos] = 4
                current_pos = rand-1
                cells[rand-1] = 2
                break
    def random_power_use():
        global cells
        while True:
            rand = random.randint(1, len(cells))
            if cells[rand-1] == 0 or cells[rand-1] == 4:
                cells[rand-1] = 5
                break
    def stun_all_use():
        global enemyList
        for i in range(num_of_enemies):
            enemyList[i].stuns += 1
            enemyList[i].stunned = True
    def stun_one_use():
        global enemyList
        end = False
        while True:
            dis_1 = input("How far down is the enemy?: ")
            dis_2 = input("How far to the right is the enemy?: ")
            for i in range(num_of_enemies):
                if enemyList[i].position == ((int(dis_1)-1)*19) + (int(dis_2)-1):
                    enemyList[i].stunned = True
                    enemyList[i].stuns = 10
                    end = True
                    break
            if end == True:
                break
    def get_invi_use():
        global invincibility
        invincibility += 10
    def move_all_use():
        global enemyList
        for i in range(num_of_enemies):
            while True:
                rand = random.randint(1,len(cells))
                if cells[rand-1] == 0 or cells[rand-1] == 4:
                    cells[enemyList[i].position] = enemyList[i].previous
                    enemyList[i].position = rand-1
                    cells[enemyList[i].position] = 3
                    break
    def move_one_use():
        global cells
        global enemyList
        done = False
        while True:
            dis_1 = input("How far down is the enemy?: ")
            dis_2 = input("How far to the right is the enemy?: ")
            for i in range(num_of_enemies):
                if enemyList[i].position == ((int(dis_1) - 1) * 19) + (int(dis_2) - 1):
                    while True:
                        choose_1 = input("How far down do you want to move it?: ")
                        choose_2 = input("How far right do you want to move it?: ")
                        choose = (int(choose_1) - 1) * 19 + (int(choose_2) - 1)
                        if cells[int(choose)] == 0 or cells[int(choose)] == 4:
                            cells[enemyList[i].position] = enemyList[i].previous
                            enemyList[i].position = choose
                            cells[enemyList[i].position] = 3
                            done = True
                            break
                    break
            if done == True:
                break
    def eat_one_use():
        global cells
        global enemyList
        done = False
        while True:
            dis_1 = input("How far down is the enemy?: ")
            dis_2 = input("How far to the right is the enemy?: ")
            for i in range(num_of_enemies):
                if enemyList[i].position == ((int(dis_1) - 1) * 19) + (int(dis_2) - 1):
                    enemyList[i].stunned = True
                    enemyList[i].stuns = 10000000000
                    cells[enemyList[i].position] = enemyList[i].previous
                    done = True
                    break
            if done == True:
                break
    def pass_turn_use():
        global moved
        moved = True
    def eat_dot_use():
        global cells
        while True:
            rand = random.randint(1, len(cells))
            if cells[rand-1] == 0:
                cells[rand-1] = 4
                break
    def add_life_use():
        global extra_life
        extra_life += 1
    def go_next_use():
        global cells
        global score
        for i in range(len(cells)):
            if cells[i] == 0:
                cells[i] = 4
        score -= 1818
    def restart_lvl_use():
        global cells
        global current_pos
        global enemyList
        global invincibility
        invincibility = 0
        for i in range(num_of_enemies):
            enemyList[i].previous = 0
            enemyList[i].stuns = 0
            enemyList[i].stunned = False
        cells = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,0, 1, 1, 5, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 5, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0,1, 0, 0, 0, 0, 1, 9, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 9, 1, 9, 9, 1, 0, 1, 0, 0, 0, 0, 0,0, 0, 1, 0, 1, 9, 9, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 3,3, 3, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 9, 9, 1, 0, 1, 0,0, 0, 0, 0, 0, 0, 1, 0, 1, 9, 9, 1, 9, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 9, 1, 0, 0, 0, 0,0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 5, 0,1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 5, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1,0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0,1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,9, 9, 9]
        current_pos = 293
        enemyList[0].position = 179
        enemyList[1].position = 180
        enemyList[2].position = 181
        if num_of_enemies > 3:
            enemyList[3].position = 20
            cells[20] = 3
            if num_of_enemies > 4:
                enemyList[4].position = 36
                cells[36] = 3
                if num_of_enemies > 5:
                    enemyList[5].position = len(cells) - 21
                    cells[len(cells) - 21] = 3
                    if num_of_enemies > 6:
                        enemyList[6].position = len(cells) - 37
                        cells[len(cells) - 37] = 3
                        if num_of_enemies > 7:
                            enemyList[7].position = 161
                            cells[161] = 3
    def recharge_all_use():
        global current_items
        for i in range(len(current_items)):
            if not (current_items[i].id == recharge_all_use or current_items[i].id == recharge_one_use):
                if current_items[i].wait > 0:
                    current_items[i].turns = 1
                else:
                    if current_items[i].charges < 1:
                        current_items[i].charges = 1
    def recharge_one_use():
        global current_items
        print("")
        for i in range(len(current_items)):
            print(str(i + 1))
            print(current_items[i].name + " (Level: " + str(current_items[i].level) + ")")
            if current_items[i].wait > 0:
                print(current_items[i].desc + str(int(current_items[i].wait)) + " turns.")
                if current_items[i].turns == 1:
                    print("Ready to Use")
                else:
                    print(str(int(current_items[i].turns - 1)) + " turns until ready.")
            else:
                print(current_items[i].desc + " (" + str(current_items[i].charges) + " use)")
            print("")
        item_choose = input("Which item do you want to recharge 1-" + str(len(current_items)) + "?: ")
        for i in range(len(current_items)):
            if item_choose == other_keys[i]:
                if not (current_items[i].id == recharge_all_use or current_items[i].id == recharge_one_use):
                    if current_items[i].wait > 0:
                        current_items[i].turns = 1
                    else:
                        if current_items[i].charges < 1:
                            current_items[i].charges = current_items[i].level
    def level_all_use():
        global current_items
        for i in range (len(current_items)):
            if not (current_items[i].id == level_all_use or current_items[i].id == level_one_use):
                if current_items[i].level < 3:
                    current_items[i].level += 1
                    if current_items[i].wait > 0:
                        current_items[i].wait = (wait_time[item_ids.index(current_items[i].id)] * 2) / (current_items[i].level + 1)
                        if current_items[i].wait < current_items[i].turns:
                            current_items[i].turns = current_items[i].wait
                    else:
                        current_items[i].charges += 1
    def level_one_use():
        global current_items
        print("")
        for i in range(len(current_items)):
            print(str(i + 1))
            print(current_items[i].name + " (Level: " + str(current_items[i].level) + ")")
            if current_items[i].wait > 0:
                print(current_items[i].desc + str(int(current_items[i].wait)) + " turns.")
                if current_items[i].turns == 1:
                    print("Ready to Use")
                else:
                    print(str(int(current_items[i].turns - 1)) + " turns until ready.")
            else:
                print(current_items[i].desc + " (" + str(current_items[i].charges) + " use)")
            print("")
        item_choose = input("Which item do you want to level 1-" + str(len(current_items)) + "?: ")
        for i in range(len(current_items)):
            if item_choose == other_keys[i]:
                if not (current_items[i].id == level_all_use or current_items[i].id == level_one_use):
                    current_items[i].level += 1
                    if current_items[i].wait > 0:
                        current_items[i].wait = (wait_time[item_ids.index(current_items[i].id)] * 2) / (current_items[i].level + 1)
                        if current_items[i].wait < current_items[i].turns:
                            current_items[i].turns = current_items[i].wait
                    else:
                        current_items[i].charges += 1
    def double_point_use():
        global multiplier
        multiplier = 2
    def be_intang_use():
        global intang
        intang += 10
    def spawn_fruit_use():
        global cells
        while True:
            rand = random.randint(0,len(cells)-1)
            if cells[rand] == 0 or cells[rand] ==4:
                cells[rand] = 6
                break
    def gain_magnet_use():
        global magnet
        magnet += 20
    def put_trap_use():
        global player_last_pos
        player_last_pos = 7
    def put_wall_use():
        global player_last_pos
        player_last_pos = 1
    def worse_enemy_passive(level):
        global thing
        thing -= int(0.5*level)
    def longer_inv_passive(level):
        global invincibility_num
        invincibility_num += 5*level
    def longer_stun_passive(level):
        global stun_num
        stun_num += 3*level
    def more_points_passive(level):
        global multiplier_increased
        global multiplier
        multiplier_increased += 0.1*level
        multiplier = multiplier_increased*multiplier
    def might_live_passive(level):
        global live_chance
        live_chance += 2*level
    def reroll_passive(level):
        global reroll
        reroll = True
        level = level
    #a
    #passive items
    #can reroll items
    class Enemy():
        def __init__(self, under, isStunned, stunsleft):
            self.position = 0
            self.previous = under
            self.stunned = isStunned
            self.stuns = stunsleft
    class Item():
        def __init__(self, name, desc, wait, id, level, charges, turns):
            self.name = name
            self.desc = desc
            self.wait = wait
            self.id = id
            self.level = level
            self.charges = charges
            self.turns = turns
    items = ["Place A Wall MU","Place A Wall SU","Place Trap MU","Place Trap SU","Gain Magnet MU","Gain Magnet SU","Spawn Fruit MU","Spawn Fruit SU","Go Through Walls MU","Go Through Walls SU","Double Points For Stage MU","Double Points For Stage SU","Level Up One Item MU","Level Up One Item SU","Level Up All Items MU","Level Up All Items SU","Recharge One Item MU","Recharge One Item SU","Recharge All Items MU", "Recharge All Items SU","Restart Level MU","Restart Level SU","Skip Stage MU", "Skip Stage SU","Get an Extra Life MU", "Get an Extra Life SU", "Choose Teleport MU", "Choose Teleport SU", "Random Teleport MU", "Random Teleport SU", "Random Power Pellet MU", "Random Power Pellet SU", "Stun all enemies MU", "Stun all enemies SU", "Stun One Enemy MU", "Stun One Enemy SU", "Become Invincible MU", "Become Invincible SU", "Move Enemies Randomly MU", "Move Enemies Randomly SU", "Move One Enemy MU", "Move One Enemy SU", "Eat One Enemy MU", "Eat One Enemy SU", "Pass Turn MU", "Pass Turn SU", "Eat One Dot MU", "Eat One Dot SU"]
    item_desc = ["Place a wall on the space you are now with a cooldown of ","Place a wall on the space you are now once","Puts a trap on the ground that can kill you and enemies with a cooldown of ","Puts a trap on the ground that can kill you and enemies once","Get a magnet that gets dots around you for 20 turns with a cooldown of ","Get a magnet that gets dots around you for 20 turns once","Spawn a fruit randomly that gives you 100 points with a cooldown of ",'Spawn a fruit randomly that gives you 100 points once',"Be able to pass through walls for 10 turns with a cooldown of ","Be able to pass through walls for 10 turns once","Doubles the amount of points you get in a stage with a cooldown of ",'Doubles the amount of points you get in a stage once',"Increases the level of one selected item with a cooldown of ","Increases the level of one selected item once","Increases the level of all items (can't go over 3) with a cooldown of ","Increases the level of all items (can't go over 3) once","Fully recharges one MU or SU item with a cooldown of ","Fully recharges one MU or SU item once","Recharge all MU and SU items (SU only get 1 charge despite level) with a cooldown of ", "Recharge all MU and SU items (SU only get 1 charge despite level) once","Reset current level to the start with a cooldown of ","Reset current level to the start once","Go directly to the next stage, but gain no points with a cooldown of ", "Go directly to the next stage, but gain no points once","Gain 1 extra life which revives you with a cooldown of ", "Gain 1 extra life which revives you once", "Teleport anywhere you want with a cooldown of ", "Teleport anywhere you want once", "Teleport randomly with a cooldown of ", "Teleport randomly once", "Randomly spawn a power pellet with a cooldown of ", "Randomly spawn a power pellet once", "Stuns every enemy for 2 turns with a cooldown of ", "Stuns every enemy for 2 turns once", "Stun a selected enemy for 10 turns with a cooldown of ", "Stun a selected enemy for 10 turns once", "Become invincible for 10 turns with a cooldown of ", "Become invincible for 10 turns once", "Move all enemies to a random place with a cooldown of ", "Move all enemies to a random place once", "Choose where to move one enemy with a cooldown of ", "Choose where to move one enemy once", "Eat one enemy with a cooldown of ", "Eat one enemy once", "Pass a turn with a cooldown of ", "Pass a turn once", "Eat one dot with a cooldown of ", "Eat one dot once"]
    wait_time = [250,0,200,0,200,0,200,0,300,0,1000,0,1000,0,2000,0,1000,0,3000,0,2000,0,3000,0,2000,0,300,0,150,0,250,0,200,0,120,0,250,0,150,0,100,0,500,0,30,0, 60, 0]
    item_ids = [put_wall_use,put_wall_use,put_trap_use,put_trap_use,gain_magnet_use,gain_magnet_use,spawn_fruit_use,spawn_fruit_use,be_intang_use,be_intang_use,double_point_use,double_point_use,level_one_use,level_one_use,level_all_use,level_all_use,recharge_one_use, recharge_one_use, recharge_all_use, recharge_all_use, restart_lvl_use,restart_lvl_use,go_next_use,go_next_use,add_life_use,add_life_use, choose_tele_use,choose_tele_use,random_tele_use,random_tele_use,random_power_use,random_power_use,stun_all_use,stun_all_use,stun_one_use,stun_one_use,get_invi_use,get_invi_use,move_all_use,move_all_use,move_one_use,move_one_use,eat_one_use,eat_one_use,pass_turn_use,pass_turn_use, eat_dot_use, eat_dot_use]
    items_passive = ["Make Enemies Worse","Be Invincible Longer","Stun Enemies Longer","Gain More Points","Have A Revive Chance","Can Reroll"]
    item_desc_passive = ["Enemys has a 5% x level to not move", "You stay invincible 5 x level more turns","You stun enemies 3 x level more turns", "You gain 10% x level more points", "You have a 2% x level chance to revive on death", "You are able to reroll item choices once"]
    item_ids_passive = [worse_enemy_passive,longer_inv_passive,longer_stun_passive,more_points_passive,might_live_passive,reroll_passive]
    other_keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
    def instructions():
        print("Hello, Welcome to Pog-Man, here's some instructions on how to play.")
        print("A board will show up, you are the black dot, the enemies are the red dots, the dots you want to eat are blue, and special power dots are purple.")
        print("The goal of this game is to eat all of the blue dots in a stage, there are 10 stages in the game which get progressively harder.")
        print("To get stronger, you get items at the start of every stage. There are rechargable items that never run out signified with the MU and others that have a specified amount of uses signified by SU.")
        print("Each item has a 1, 2 and 3 level, where 3 is the best. You can use these items by going into the item menu and selecting the item you want to use.")
        print("The way to move is w a s d, where w is up, a is left, s is down, and d is right, also i is the item menu key.")
        print("Finally, there are some items that need you to put in coordinates, to use them, first enter how far down from the top the pixel is, and then how far right it is, for example the middle enemy on stage 1 starts at 10,10")
        print("Good Luck playing, there is a score that is kept track of, try to get the high score!")
        print("")
        continuee = input("Press Enter to Continue")
        print("")
    for p in range (10):
        if Alive == False:
            break
        cells = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,0, 1, 1, 5, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 5, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0,1, 0, 0, 0, 0, 1, 9, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 9, 1, 9, 9, 1, 0, 1, 0, 0, 0, 0, 0,0, 0, 1, 0, 1, 9, 9, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 3,3, 3, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 9, 9, 1, 0, 1, 0,0, 0, 0, 0, 0, 0, 1, 0, 1, 9, 9, 1, 9, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 9, 1, 0, 0, 0, 0,0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 5, 0,1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 5, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1,0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0,1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,9, 9, 9]
        num_turns = 0
        magnet = 0
        multiplier = 1*multiplier_increased
        intang = 0
        invincibility = 0
        invincibility_num = 20 - (p)
        stun_num = 10 - int(p/2)
        picked_item = []
        if (p+1) % 2 == 0:
            num_of_enemies += 1
        rand = random.randint(1,30)
        enemyList = []
        for i in range(num_of_enemies):
            enemyList.append(Enemy(0, False, 0))
        enemyList[0].position = 179
        enemyList[1].position = 180
        enemyList[2].position = 181
        if num_of_enemies > 3:
            enemyList[3].position = 20
            cells[20] = 3
            if num_of_enemies > 4:
                enemyList[4].position = 36
                cells[36] = 3
                if num_of_enemies > 5:
                    enemyList[5].position = len(cells) - 21
                    cells[len(cells)-21] = 3
                    if num_of_enemies > 6:
                        enemyList[6].position = len(cells) - 37
                        cells[len(cells)-37] = 3
                        if num_of_enemies > 7:
                            enemyList[7].position = 161
                            cells[161] = 3
        while True:
            choose_item = []
            for i in range(3):
                while True:
                    rand = random.randint(0,len(items)-1)
                    if rand not in picked_item and rand not in saved_items:
                        rand2 = random.randint(1, 11)
                        if rand2 < 8:
                            level = 1
                        elif rand2 < 11:
                            level = 2
                        else:
                            level = 3
                        choose_item.append(Item(items[rand], item_desc[rand], wait_time[rand], item_ids[rand], level, 0, 1) )
                        print("Item "+str(i+1)+": "+str(choose_item[i].name)+" (Level: "+str(level)+")")
                        choose_item[i].wait = (choose_item[i].wait * 2) / (level + 1)
                        if choose_item[i].wait > 0:
                            print(choose_item[i].desc+str(int(choose_item[i].wait))+" turns.")
                        else:
                            print(choose_item[i].desc+" ("+str(level)+" use)")
                            choose_item[i].charges = level
                        print("")
                        picked_item.append(rand)
                        break
            if reroll == True:
                print("Reroll the items with r")
            pick_item = input("Which item do you want?: ")
            if pick_item == "r":
                print()
                pass
            elif pick_item == "1" or pick_item == "2" or pick_item == "3":
                saved_items.append(picked_item[int(pick_item)-1])
                current_items.append(choose_item[int(pick_item)-1])
                break
            else:
                break
        while Alive:
            restart = False
            if invincibility > 0:
                invincibility -= 1
            moved = False
            num_turns += 1
            rand = random.randint(1,500)
            if rand == 1:
                cells[218] = 6
            rand = random.randint(1,2000)
            if rand == 1:
                while True:
                    rand = random.randint(0,len(cells)-1)
                    if (cells[rand] == 0) or (cells[rand] == 4):
                        cells[rand] = 8
                        break
            if intang > 0:
                intang -= 1
            for i in range(len(cells)):
                if cells[i] == 1 or cells[i] == 9:
                    print(u"\u001b[38;5;0m█",end='')
                elif cells[i] == 0:
                    print(u"\u001b[38;5;20m█",end='')
                elif cells[i] == 2:
                    if invincibility > 0:
                        print(u"\u001b[38;5;226m█",end='')
                    else:
                        print(u"\u001b[38;5;8m█",end='')
                    current_pos = i
                elif cells[i] == 3:
                    print(u"\u001b[38;5;1m█",end='')
                elif cells[i] == 4:
                    print(u"\u001b[38;5;15m█",end='')
                elif cells[i] == 5:
                    print(u"\u001b[38;5;13m█",end='')
                elif cells[i] == 6:
                    print(u"\u001b[38;5;2m█",end='')
                elif cells[i] == 7:
                    print(u"\u001b[38;5;240m█",end='')
                else:
                    print(u"\u001b[38;5;220m█",end='')
                if i % 19 == 18:
                    print(u"\u001b[38;5;7m "+str(int((i/19)+1)))
            if cells.count(2) == 0:
                if extra_life > 0:
                    extra_life -= 1
                    cells[current_pos] = 4
                    current_pos = 293
                    cells[current_pos] = 2
                elif live_chance > 0:
                    rand = random.randint(1,100)
                    if rand < live_chance:
                        cells[current_pos] = 4
                        current_pos = 293
                        cells[current_pos] = 2
                    else:
                        print("You Died")
                        Alive = False
                        break
                else:
                    print("You Died")
                    Alive = False
                    break
            if cells.count(0) == 0:
                print("You Win")
                break
            while True:
                move = input("Where do you want to move? w a s d (i for items, h for help): ")
                if move == "win":
                    invincibility = 10000
                if move == "win2":
                    for i in range (len(cells)):
                        if cells[i] == 0:
                            cells[i] = 4
                if move == "i":
                    for i in range (len(current_items)):
                        print(str(i+1))
                        print(current_items[i].name+" (Level: "+str(current_items[i].level)+")")
                        if current_items[i].wait > 0:
                            print(current_items[i].desc+str(int(current_items[i].wait))+" turns.")
                            if current_items[i].turns == 1:
                                print ("Ready to Use")
                            else:
                                print(str(int(current_items[i].turns-1))+" turns until ready.")
                        else:
                            print(current_items[i].desc+" ("+ str(current_items[i].charges)+" use)")
                        print("")
                    item_choose = input("Which item do you want to choose 1-"+str(len(current_items))+"?: ")
                    for i in range (len(current_items)):
                        if item_choose == other_keys[i]:
                            if current_items[i].wait > 0:
                                if current_items[i].turns <= 1:
                                    current_items[i].id()
                                    current_items[i].turns += current_items[i].wait
                                else:
                                    print("Not Ready Yet")
                                    time.sleep(1.2)
                            else:
                                if current_items[i].charges > 0:
                                    current_items[i].id()
                                    current_items[i].charges -= 1
                                else:
                                    print("No Uses Remaining")
                                    time.sleep(1.2)
                if move == "h":
                    instructions()
                if player_last_pos == 0 or player_last_pos == 3 or player_last_pos == 5 or player_last_pos == 6:
                    player_last_pos = 4
                if move =="w":
                    if cells[current_pos - 19] == 6:
                        score += 100*multiplier
                    if cells[current_pos -19] == 5:
                        invincibility += invincibility_num
                    if cells[current_pos -19] == 3 or cells[current_pos-19] == 7:
                        if invincibility > 0:
                            pass
                        else:
                            if extra_life > 0:
                                extra_life -= 1
                                cells[current_pos] = 4
                                current_pos = 293
                                cells[current_pos] = 2
                            elif live_chance > 0:
                                rand = random.randint(1, 100)
                                if rand < live_chance:
                                    cells[current_pos] = 4
                                    current_pos = 293
                                    cells[current_pos] = 2
                                else:
                                    print("You Died")
                                    Alive = False
                                    break
                            else:
                                print("You Died")
                                Alive = False
                                break
                    if (not (cells[current_pos - 19] == 1 or cells[current_pos - 19] == 9)) or (intang > 0 and cells[current_pos-19]==1):
                        cells[current_pos] = player_last_pos
                        player_last_pos = cells[current_pos-19]
                        cells[current_pos-19] = 2
                        moved = True
                if move =="a":
                    if current_pos == 171:
                        cells[current_pos] = 4
                        cells[189] = 2
                        moved = True
                    if cells[current_pos - 1] == 6:
                        score += 100*multiplier
                    if cells[current_pos - 1] == 5:
                        invincibility += invincibility_num
                    if cells[current_pos - 1] == 3 or cells[current_pos-1] == 7:
                        if invincibility > 0:
                            pass
                        else:
                            if extra_life > 0:
                                extra_life -= 1
                                cells[current_pos] = 4
                                current_pos = 293
                                cells[current_pos] = 2
                            elif live_chance > 0:
                                rand = random.randint(1, 100)
                                if rand < live_chance:
                                    cells[current_pos] = 4
                                    current_pos = 293
                                    cells[current_pos] = 2
                                else:
                                    print("You Died")
                                    Alive = False
                                    break
                            else:
                                print("You Died")
                                Alive = False
                                break
                    if (not (cells[current_pos -1] == 1 or cells[current_pos - 1] == 9)) or (intang > 0 and cells[current_pos-1]==1):
                        cells[current_pos] = player_last_pos
                        player_last_pos = cells[current_pos - 1]
                        cells[current_pos - 1] = 2
                        moved = True
                if move =="s":
                    if cells[current_pos + 19] == 6:
                        score += 100*multiplier
                    if cells[current_pos + 19] == 5:
                        invincibility += invincibility_num
                    if cells[current_pos + 19] == 3 or cells[current_pos+19] == 7:
                        if invincibility > 0:
                            pass
                        else:
                            if extra_life > 0:
                                extra_life -= 1
                                cells[current_pos] = 4
                                current_pos = 293
                                cells[current_pos] = 2
                            elif live_chance > 0:
                                rand = random.randint(1, 100)
                                if rand < live_chance:
                                    cells[current_pos] = 4
                                    current_pos = 293
                                    cells[current_pos] = 2
                                else:
                                    print("You Died")
                                    Alive = False
                                    break
                            else:
                                print("You Died")
                                Alive = False
                                break
                    if (not (cells[current_pos+19] == 1 or cells[current_pos + 19] == 9)) or (intang > 0 and cells[current_pos+19]==1):
                        cells[current_pos] = player_last_pos
                        player_last_pos = cells[current_pos + 19]
                        cells[current_pos + 19] = 2
                        moved = True
                if move =="d":
                    if current_pos == 189:
                        cells[current_pos] = 4
                        cells[171] = 2
                        moved = True
                    if cells[current_pos +1] == 6:
                        score += 100*multiplier
                    if cells[current_pos +1] == 5:
                        invincibility += invincibility_num
                    if cells[current_pos +1] == 3 or cells[current_pos+1] == 7:
                        if invincibility > 0:
                            pass
                        else:
                            if extra_life > 0:
                                extra_life -= 1
                                cells[current_pos] = 4
                                current_pos = 293
                                cells[current_pos] = 2
                            elif live_chance > 0:
                                rand = random.randint(1, 100)
                                if rand < live_chance:
                                    cells[current_pos] = 4
                                    current_pos = 293
                                    cells[current_pos] = 2
                                else:
                                    print("You Died")
                                    Alive = False
                                    break
                            else:
                                print("You Died")
                                Alive = False
                                break
                    if (not (cells[current_pos+1] == 1 or cells[current_pos + 1] == 9)) or (intang > 0 and cells[current_pos+1]==1):
                        cells[current_pos] = player_last_pos
                        player_last_pos = cells[current_pos + 1]
                        cells[current_pos + 1] = 2
                        moved = True
                if moved == True:
                    for i in range(len(current_items)):
                        if current_items[i].wait > 0 and not current_items[i].turns <= 1:
                            current_items[i].turns -= 1
                if player_last_pos == 8:
                    player_last_pos = 4
                    print()
                    print("You just picked up a treasure chest, inside was this beautiful passive item!")
                    rand = random.randint(0,len(items_passive)-1)
                    rand2 = random.randint(1, 10)
                    if rand2 == 10:
                        passive_level = 2
                    else:
                        passive_level = 1
                    print(items_passive[rand]+" Level: "+str(passive_level))
                    print(item_desc_passive[rand])
                    passive_pickup = input("Input 1 to pick up the item and anything else to skip: ")
                    if passive_pickup == "1":
                        item_ids_passive[rand](passive_level)
                        print(items_passive[rand]+" has been activated!")
                for i in range(num_of_enemies):
                    enemy_ai = [enemy_moves(enemyList[i].position, enemyList[i].previous, enemyList[i].stunned, enemyList[i].stuns, score, thing)]
                    enemyList[i].position = enemy_ai[0][0]
                    enemyList[i].previous = enemy_ai[0][1]
                    enemyList[i].stunned = enemy_ai[0][2]
                    enemyList[i].stuns = enemy_ai[0][3]
                    score = enemy_ai[0][4]
                if cells.count(2) == 0:
                    if extra_life > 0:
                        extra_life -= 1
                        cells[current_pos] = 4
                        current_pos = 293
                        cells[current_pos] = 2
                    else:
                        Alive = False
                if moved == True:
                    if magnet > 0:
                        if cells[current_pos-19] == 0:
                            cells[current_pos - 19] = 4
                        if cells[current_pos - 1] == 0:
                            cells[current_pos - 1] = 4
                        if cells[current_pos+19] == 0:
                            cells[current_pos + 19] = 4
                        if cells[current_pos + 1] == 0:
                            cells[current_pos + 1] = 4
                        magnet -= 1
                break
        score += 10*(182-cells.count(0))*multiplier
        score -= (50*(4-cells.count(5)))/multiplier
        score -= (100*(1-cells.count(2)))/multiplier
        score -= num_turns/multiplier
        stage_num = p + 1
        if Alive == True:
            print("You just completed Stage "+ str(stage_num)+".")
            print("Your score is "+str(int(score))+".")
            next_stage = input("Hit 'enter' when you're ready to go to the next stage")
            print("")
    if Alive == False:
        score -= 100
    else:
        print("Congratulations, You Win!")
    score = int(score)
    old_scores = open("scores.txt", "r+")
    score_list = [float(num) for num in old_scores.read().split()]
    high_score = max(score_list)
    print("Your score was "+str(score)+".")
    print("The high score was "+str(high_score)+".")
    old_scores.write("\n"+str(score))
    print()
    continuation = input("Do you wan to play again?('quit' to end): ")
    print()
    if continuation == "quit":
        break