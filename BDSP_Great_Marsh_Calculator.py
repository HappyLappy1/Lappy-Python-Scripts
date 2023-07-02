# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 16:26:39 2023

@author: Lappy
"""
marsh_seq = ["Croagunk" , "Skorupi" , "Carnivine" , "Croagunk" , "Skorupi" , "Carnivine" , "Golduck" , "Croagunk" , "Skorupi" , "Carnivine" , "Roselia" , "Staravia" , "Marill" , "Azurill" , "Wooper" , "Golduck" , "Staravia" , "Croagunk" , "Skorupi" , "Carnivine" , "Quagsire" , "Bidoof" , "Bibarel" , "Wooper" , "Azurill" , "Roselia" , "Staravia" , "Croagunk" , "Skorupi" , "Carnivine" , "Roselia" , "Golduck" , "Croagunk" , "Skorupi" , "Carnivine" , "Croagunk" , "Skorupi" , "Carnivine" , "Golduck" , "Croagunk" , "Skorupi" , "Carnivine" , "Roselia" , "Staravia" , "Toxicroak" , "Drapion" , "Exeggcute" , "Golduck" , "Staravia" , "Croagunk" , "Skorupi" , "Carnivine" , "Yanma" , "Shroomish" , "Paras" , "Kangaskhan" , "Gulpin" , "Roselia" , "Staravia" , "Croagunk" , "Skorupi" , "Carnivine" , "Roselia" , "Golduck"]
# Having the natdex completely changes which mons will appear. In theory more info could be gleaned by getting one day before AND after acquiring the natdex, but that's super niche. 
is_natdex = False
# the lower 32 bits of the current group seed.
group_seed = 0xE0F3C2E0
# Marsh mons on 2 consecutive days, with day 1 having the above group seed.
marsh_1 = ["Wooper", "Bibarel", "Staravia", "Azurill", "Roselia", "Croagunk"]
marsh_2 = ["Bidoof", "Azurill", "Croagunk", "Croagunk", "Croagunk", "Golduck"]
marsh_outs_1 = []
for i in range(6):
    temp_1 = []
    for j in range(0x20):
        if marsh_1[i] == marsh_seq[j + 0x20*is_natdex]:
            temp_1.append(j)
    marsh_outs_1.append(temp_1)
marsh_seeds_1 = []
for a in marsh_outs_1[0]:
    for b in marsh_outs_1[1]:
        for c in marsh_outs_1[2]:
            for d in marsh_outs_1[3]:
                for e in marsh_outs_1[4]:
                    for f in marsh_outs_1[5]:
                        marsh_seeds_1.append(a + (b << 5) + (c << 10) + (d << 15) + (e << 20) + (f << 25))
                        marsh_seeds_1.append(a + (b << 5) + (c << 10) + (d << 15) + (e << 20) + (f << 25) + (1 << 30))
full_seeds_1 = []
uppers = []
remainders = []
for i in marsh_seeds_1:
     remainders.append((i - group_seed) % 0x7FFFFFFF)
for i in remainders:
    if i % 2 == 0:
        if (i + 0) // 2 < 0x100000000 and (i + 0) // 2 > 0: 
            uppers.append((i + 0) // 2)
        if (i + 0xFFFFFFFE) // 2 < 0x100000000 and (i + 0xFFFFFFFE) // 2 > 0: 
            uppers.append((i + 0xFFFFFFFE) // 2)
        if (i + 0x1FFFFFFFC) // 2 < 0x100000000 and (i + 0x1FFFFFFFC) // 2 > 0: 
            uppers.append((i + 0x1FFFFFFFC) // 2)        
    else:
        if (i + 0x7FFFFFFF) // 2 < 0x100000000 and (i + 0x7FFFFFFF) // 2 > 0: 
            uppers.append((i + 0x7FFFFFFF) // 2)
        if (i + 0x17FFFFFFD) // 2 < 0x100000000 and (i + 0x17FFFFFFD) // 2 > 0: 
            uppers.append((i + 0x17FFFFFFD) // 2) 
for i in uppers:
    full_seeds_1.append(i * 0x100000000 + group_seed)
marsh_outs_2 = []
for i in range(6):
    temp_1 = []
    for j in range(0x20):
        if marsh_2[i] == marsh_seq[j + 0x20*is_natdex]:
            temp_1.append(j)
    marsh_outs_2.append(temp_1)
marsh_seeds_2 = []
for a in marsh_outs_2[0]:
    for b in marsh_outs_2[1]:
        for c in marsh_outs_2[2]:
            for d in marsh_outs_2[3]:
                for e in marsh_outs_2[4]:
                    for f in marsh_outs_2[5]:
                        marsh_seeds_2.append(a + (b << 5) + (c << 10) + (d << 15) + (e << 20) + (f << 25))
                        marsh_seeds_2.append(a + (b << 5) + (c << 10) + (d << 15) + (e << 20) + (f << 25) + (1 << 30))
results = []
for i in full_seeds_1:
    if marsh_seeds_2.count(((i * 0x6C078965 + 1) & 0xFFFFFFFFFFFFFFFF) % 0x7FFFFFFF) > 0:
        print(hex(i))
        results.append(i)