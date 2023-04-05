# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 12:53:08 2023
"""

def XDRNG(seed):
    return (((seed * 0x343FD) + 0x00269EC3) & 0xFFFFFFFF)
def XDRNGR(seed):
    return (((seed * 0xB9B33155) + 0xA170F641) & 0xFFFFFFFF)

TID = int(input("What is your TID: "))
IVs = input("What are the IVs of your Eevee (separate by \"/\"): ")
IVs = IVs.split("/")

IV_1 = int(IVs[0].strip()) + int(IVs[1].strip())*32 + int(IVs[2].strip())*1024
IV_2 = int(IVs[5].strip()) + int(IVs[3].strip())*32 + int(IVs[4].strip())*1024

seed_list = []
for i in range(65536):
    seed = (IV_1 << 16) + i
    if (XDRNG(seed) >> 16) & 0x7FFF == IV_2:
        seed_list.append(seed)
        seed_list.append(seed ^ 0x80000000)
sids = []
for s in seed_list:
    advance = 12
    sheed = s
    while advance > 0 and (sheed >> 16) != TID:
        
        sid = sheed >> 16
        sheed = XDRNGR(sheed)
        advance = advance - 1
    if (sheed >> 16) == TID:
        sids.append(sid)
print(sids)
