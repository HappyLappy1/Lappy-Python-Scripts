import numba

@numba.njit()
def Typhoon(seed):
    state_0 = seed # self.state[0] = seed
    state_1 = (0x6C078965 * (state_0 ^ (state_0 >> 30)) + 1) & 0xFFFFFFFF
    state_2 = (0x6C078965 * (state_1 ^ (state_1 >> 30)) + 2) & 0xFFFFFFFF
    curr_state = state_2 
    for i in range(3, 398): # 397 - 2 state changes happen between state_2 and state_397
        curr_state = (0x6C078965 * (curr_state  ^ (curr_state  >> 30)) + i) & 0xFFFFFFFF
    state_397 = curr_state
    state_398 = (0x6C078965 * (state_397 ^ (state_397 >> 30)) + 398) & 0xFFFFFFFF
    
    MAG02 = (0, 0x9908B0DF)
    # shuffle
    y = ((state_0 & 0x80000000) | (state_1 & 0x7FFFFFFF)) & 0xFFFFFFFF
    y = state_397 ^ y >> 1 ^ MAG02[y & 1]

    # twist
    y ^= (y >> 11)
    y ^= ((y << 7) & 0x9D2C5680)
    y ^= ((y << 15) & 0xEFC60000)
    y ^= (y >> 18)

    Final_State1 = y    
    MAG02 = (0, 0x9908B0DF)
    # shuffle
    y = ((state_1 & 0x80000000) | (state_2 & 0x7FFFFFFF)) & 0xFFFFFFFF
    y = state_398 ^ y >> 1 ^ MAG02[y & 1]

    # twist
    y ^= (y >> 11)
    y ^= ((y << 7) & 0x9D2C5680)
    y ^= ((y << 15) & 0xEFC60000)
    y ^= (y >> 18)
    Final_State2 = y
    return Final_State1, Final_State2
    


def getSeed(lotto1,lotto2,lotto3):
    reverse_add = 0xFC77A683
    add = 0x3039
    lotto1 <<= 16
    for low in range(0x10000):
        # run test seed through LCRNGR to get the original seed
        init = ((lotto1 | low) * 0xEEB9EB65 + reverse_add) & 0xFFFFFFFF
        # advance with ARNG
        seed = (init * 0x6c078965 + 0x1) & 0xFFFFFFFF
        # get next lotto number with seed
        test2 = ((seed * 0x41c64e6d + add) & 0xFFFFFFFF) >> 16
        # if lotto incorrect, continue in loop
        if test2 != lotto2:
            continue
        # advance with ARNG
        seed = (seed * 0x6c078965 + 0x1) & 0xFFFFFFFF
        # get next lotto number with seed
        test3 = ((seed * 0x41c64e6d + add) & 0xFFFFFFFF) >> 16
        # if lotto incorrect, continue in loop
        if test3 != lotto3:
            continue
        # otherwise return original seed
        return init
    # return None if no seed found
    return None

def GetSID(GrSeed, TID, Day, Month, DelayL, DelayH, HourL, HourH):
    Gseeds = [GrSeed] 
    for i in range (36500):
        GrSeed = (GrSeed * 0x9638806D + 0x69C77F93) & 0xFFFFFFFF 
        Gseeds.append(GrSeed)
    Gseeds_S = set(Gseeds)
    print("Done creating Gseeds")
    AA = []
    BB = []
    CCCC = []
    for i in range(0x100):
        if (((i - ((Day * Month) & 0xFF)) % 0x100) < 119):
            AA.append(i)
        if (HourL <= i <= HourH):
            BB.append(i)
    print("Done with AA and BB")
    for i in range(DelayL, DelayH):
        if ((i - DelayL) <= DelayH):
            CCCC.append(i)
    print("Done with CCCC")
    Iseeds = []
    for i in AA:
        for j in BB:
            for k in CCCC:
                Iseeds.append((i<<24)+(j<<16)+k)
    for q in Iseeds:
        GrIseed, sidtid = Typhoon(q)
        if GrIseed in Gseeds_S:
            if (sidtid & 0xFFFF == TID):
                print("SID:",sidtid >> 16, "Init. Seed:", hex(q))
GetSID(getSeed(23267,30516,23187),9129,1,9,5000,65535,0,23)
GetSID(
    getSeed(int(input("Lotto 1:")), 
            int(input("Lotto 2:")),
            int(input("Lotto 3:"))),
    int(input("TID:")),
    int(input("Day:")),
    int(input("Month:")),
    int(input("DelayL:")),
    int(input("DelayH:")),
    int(input("HourL:")),
    int(input("HourH:")))
