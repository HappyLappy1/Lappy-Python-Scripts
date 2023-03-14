# Majority of this done by Shao. I (Lappy) just made it look pretty, added user inputs, and made an infographic.
# Infographic: https://github.com/HappyLappy1/Lappy-Python-Scripts/blob/main/RSE_Trendy_Saying_2_SID/RSE_Feebas_Tiles_Index.png
def advance(seed):
    return (0x41C64E6D * seed + 0x00006073) & 0xFFFFFFFF

def prev(seed):
    return (seed*0xeeb9eb65+0xa3561a1)& 0xFFFFFFFF

def iso_2(seed):
    return (1103515245 * (seed) + 12345) & 0xFFFFFFFF

class NewGameRNG:
    def __init__(self, seed):
        self.seed = seed
        self.trends = []
        self.populate_trends()
        self.feebas_seed = self.trends[0][2]
        
    def random(self):
        self.seed = (0x41C64E6D * self.seed + 0x00006073) & 0xFFFFFFFF
        return self.seed >> 16
    
    def should_swap(self, a, b):
        if a[0] > b[0]:
            return True
        elif a[0] < b[0]:
            return False
        elif a[1] > b[1]:
            return True
        elif a[1] < b[1]:
            return False
        else:
            return self.random() & 1
        
    def populate_trends(self):
        self.trends = []
        for i in range(5):
            self.random() # Call to generate first word, no impact
            self.random() # Call to decide which group second word comes from, no impact
            self.random() # Call to generate second group, no impact
            g = self.random() & 1 # Call to decide whether trend is gaining trendiness, no impact
            # Enter SeedTrendRNG
            rand = self.random() % 98
            if rand > 50:
                rand = self.random() % 98
                if rand > 80:
                    rand = self.random() % 98
            maxtrend = rand+30
            trend = ((self.random()) % (rand+1)) + 30
            rand = self.random()
            self.trends.append((trend, maxtrend, rand, g))
        # Now need to sort the trends
        for i in range(5):
            for j in range(i+1, 5):
                if (self.should_swap(self.trends[j], self.trends[i])):
                    temp = self.trends[i]
                    self.trends[i] = self.trends[j]
                    self.trends[j] = temp
            
def Feebas_Spots(seed):
    spots = []
    i=0
    while i < 6:
        seed = iso_2(seed)
        rand = (seed >> 16) % 447
        if rand == 0:
            rand == 447
        if rand >= 4:
            spots.append(rand)
            i+=1
    return spots
            
def EmeraldSearch(TID, feebas_seed, min_advances, max_advances):          
    init_seed = TID
    advances = 0
    while (advances < min_advances):
        init_seed = advance(init_seed)
        advances+=1
    while(advances <= max_advances):
        trends = NewGameRNG(init_seed)
        if trends.feebas_seed == feebas_seed:
            two = prev(prev(init_seed))
            three = prev(two)
            SIDtwo = two >> 16
            SIDthree = three >> 16
            print(f"SID: {SIDtwo} matches your feebas seed on advance {advances-3} with 2 Vblanks") 
            print(f"SID: {SIDthree} matches your feebas seed on advance {advances-4} with 3 Vblanks")
        advances+=1
        init_seed = advance(init_seed)

def RSSearch(TID, feebas_seed, min_advances, max_advances, game_seed = 0x5A0):
    init_seed = game_seed
    advances = 0
    while (advances < min_advances):
        init_seed = advance(init_seed)
        advances+=1
    while (advances <= max_advances):
        if TID == (init_seed >> 16):
            dewford_seed = advance(advance(init_seed))
            if NewGameRNG(dewford_seed).feebas_seed == feebas_seed:
                SID = prev(init_seed) >> 16
                print(f"SID: {SID} matches your feebas seed on advance {advances-2} with 2 Vblanks")
            dewford_seed = advance(dewford_seed)
            if NewGameRNG(dewford_seed).feebas_seed == feebas_seed:
                SID = prev(init_seed) >> 16
                print(f"SID: {SID} matches your feebas seed on advance {advances-3}")
        advances+=1
        init_seed = advance(init_seed)        

    
def Emerald_SID_From_Spots(TID, spots, min_advances, max_advances):
    printed_anything = False
    init_seed = TID
    advances = 0
    while (advances < min_advances):
        init_seed = advance(init_seed)
        advances+=1
    while(advances <= max_advances):
        feebas_spots = Feebas_Spots(NewGameRNG(init_seed).feebas_seed)
        if all(spot in feebas_spots for spot in spots):
            two = prev(prev(init_seed))
            three = prev(two)
            SIDtwo = two >> 16
            SIDthree = three >> 16
            print(f"SID: {SIDtwo} matches your feebas seed on advance {advances-3} with 2 Vblanks and spots {feebas_spots}") 
            print(f"SID: {SIDthree} matches your feebas seed on advance {advances-4} with 3 Vblanks and spots {feebas_spots}")
            printed_anything = True
        advances+=1
        init_seed = advance(init_seed)
    if not printed_anything:
        print("No Results found!")
        
def RS_SID_From_Spots(TID, spots, min_advances, max_advances, game_seed = 0x5A0):
    printed_anything = False
    init_seed = game_seed
    advances = 0
    while (advances < min_advances):
        init_seed = advance(init_seed)
        advances+=1
    while (advances <= max_advances):
        if TID == (init_seed >> 16):
            dewford_seed = advance(advance(init_seed))
            feebas_spots = Feebas_Spots(NewGameRNG(dewford_seed).feebas_seed)
            if all(spot in feebas_spots for spot in spots):
                SID = prev(init_seed) >> 16
                print(f"SID: {SID} is consistent on advance {advances-2} with 2 Vblanks and spots {feebas_spots}")
                printed_anything = True
            dewford_seed = advance(dewford_seed)
            feebas_spots = Feebas_Spots(NewGameRNG(dewford_seed).feebas_seed)
            if all(spot in feebas_spots for spot in spots):
                SID = prev(init_seed) >> 16
                print(f"SID: {SID} matches your feebas seed on advance {advances-3} with 3 Vblanks and spots {feebas_spots}")
                printed_anything = True
        advances+=1
        init_seed = advance(init_seed)
    if not printed_anything:
        print("No Results found!")
        
print("Tiles 1, 2, and 3 are inaccesible water tiles. However, the game intentionally rerolls them if they are ever selected.")
print("Tiles 105, 119, 132 and 144 are land tiles the player cannot fish on. The game can generate feebas on these tiles")
print("Tiles 296, 297 and 298 are inaccessible water tiles that can contain feebas. The game can generate feebas on these tiles.")

tid = int(input("Trainer ID: "))
feebas_tiles = input("Known Feebas Tile Indices Separated by Commas (See infographic for conversion): ").split(",")
min_advances = int(input("Minimum Advances: "))
max_advances = int(input("Maximum Advances: "))
for i in range(len(feebas_tiles)):
    feebas_tiles[i] = int(feebas_tiles[i].strip())
if input("Which Game Version are you attempting to find the Secret ID of? Emerald = 1, Ruby/Sapphire = 0") == "1":
    Emerald_SID_From_Spots(tid, feebas_tiles, min_advances, max_advances)
else:
    RS_SID_From_Spots(tid, feebas_tiles, min_advances, max_advances)
