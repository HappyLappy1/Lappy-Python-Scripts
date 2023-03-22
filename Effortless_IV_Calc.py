# -*- coding: utf-8 -*-
print(
    "This tool is only accurate for gens 3-5. base stats changed in gen 6+, as did the iv judge."
)


def stats_to_ivs(species, level, nature, stats):
    file = open("pokemon_stats_reference.txt","r")
    file_text = file.read()
    file.close()
    file_text = file_text.split("\n")
    base = []
    for i in file_text:
        temp = i.split()
        if temp[0].strip() == species:
            for j in range(1,7):
                base.append(int(temp[j]))
    file_1 = open("pokemon_nature_reference.txt","r")
    file_1_text = file_1.read()
    file_1.close()
    file_1_text = file_1_text.split("\n")
    nature_s = []
    for i in file_1_text:
        temp = i.split()
        if temp[0].strip() == nature:
            for j in range(1,6):
                nature_s.append(int(temp[j]))
    print(base)
    print(nature_s)
    v_max = []
    v_min = []
    mini = 94
    maxi = 0
    for v in range(95):
        if stats[0] == ((((2 * base[0] + v) * level) // 100) + level + 10):
            mini = min(mini, v)
            maxi = max(maxi, v)
    v_max.append(maxi)
    v_min.append(mini)
    for s in range(1, 6):
        mini = 94
        maxi = 0
        for v in range(95):
            if nature_s[s - 1] == 0:
                if stats[s] == ((((2 * base[s] + v) * level) // 100) + 5):
                    mini = min(mini, v)
                    maxi = max(maxi, v)
            else:
                if stats[s] == (
                    (((((2 * base[s] + v) * level) // 100) + 5) * nature_s[s - 1]) // 10
                ):
                    mini = min(mini, v)
                    maxi = max(maxi, v)
        v_max.append(maxi)
        v_min.append(mini)
    print(v_max, v_min)
    min_ivs = [0, 0, 0, 0, 0, 0]
    max_ivs = [31, 31, 31, 31, 31, 31]
    best_ivs = [0, 0, 0, 0, 0, 0]
    characteristic = input("characteristic, leave blank if unknown: ")
    characteristic = characteristic.lower()
    know_char = 0
    char_stat = 7
    if characteristic != "":
        know_char = 1
        char_txts = [
            "loves to eat",
            "often dozes off",
            "often scatters things",
            "scatters things often",
            "likes to relax",
            "proud of its power",
            "likes to thrash about",
            "a little quick tempered",
            "likes to fight",
            "quick tempered",
            "sturdy body",
            "capable of taking hits",
            "highly persistent",
            "good endurance",
            "good perseverance",
            "highly curious",
            "mischievous",
            "thoroughly cunning",
            "often lost in thought",
            "very finicky",
            "strong willed",
            "somewhat vain",
            "strongly defiant",
            "hates to lose",
            "somewhat stubborn",
            "likes to run",
            "alert to sounds",
            "impetuous and silly",
            "somewhat of a clown",
            "quick to flee",
            "takes plenty of siestas",
            "nods off a lot",
        ]
        char_stats = [
            0,
            0,
            0,
            0,
            0,
            1,
            1,
            1,
            1,
            1,
            2,
            2,
            2,
            2,
            2,
            3,
            3,
            3,
            3,
            3,
            4,
            4,
            4,
            4,
            4,
            5,
            5,
            5,
            5,
            5,
            0,
            0,
        ]
        char_Mod = [
            0,
            1,
            2,
            3,
            4,
            0,
            1,
            2,
            3,
            4,
            0,
            1,
            2,
            3,
            4,
            0,
            1,
            2,
            3,
            4,
            0,
            1,
            2,
            3,
            4,
            0,
            1,
            2,
            3,
            4,
            2,
            3,
        ]
        for c in range(len(char_txts)):
            if characteristic == char_txts[c]:
                min_ivs[char_stats[c]] = char_Mod[c]
                best_ivs[char_stats[c]] = 1
                char_stat = char_stats[c]
                for m in range(6):
                    max_ivs[m] = max((char_Mod[c] + 30) % 32, (char_Mod[c] + 25) % 32)
    print("MAX", max_ivs, "MIN", min_ivs)
    # iv judge
    know_judge = 0
    if int(input("Do you have access to the iv judge? 1 = Yes, 0 = No: ")) == 1:
        know_judge = 1
        bs_string = input(
            "When talking to the iv judge, Which are your best ivs? Submit your answer in a format like this: 0/1/0/1/0/1, where 1 = Yes, 0 = No for the ivs in the order hp/ATK/DEF/SPA/SPD/SPE: "
        )
        best_stats = bs_string.split("/")
        for i in range(6):
            best_stats[i] = int(best_stats[i])
        peak_iv = input(
            "How good does the iv judge say your best iv is? (Using Bulbapedia stats judge phrases): "
        )
        peak_iv = peak_iv.lower()
        peak_ivs_txt = [
            "relatively good",
            "rather decent",
            "quite impressive",
            "very good",
            "good",
            "outstanding",
            "fantastic",
            "flawless",
            "can't be better",
            "cant be better",
            "can't be beat",
            "cant be beat",
        ]
        peak_ivs_min = [0, 0, 16, 16, 16, 26, 26, 31, 31, 31, 31, 31]
        peak_ivs_max = [15, 15, 25, 25, 25, 30, 30, 31, 31, 31, 31, 31]
        for p in range(len(peak_ivs_txt)):
            if peak_iv == peak_ivs_txt[p]:
                for b in range(6):
                    if best_stats[b] == 1:
                        min_ivs[b] = peak_ivs_min[p] + (
                            ((min_ivs[b] % 5) - (peak_ivs_min[p] % 5)) % 5
                        ) * (b == char_stat)
                        max_ivs[b] = peak_ivs_max[p] - (
                            ((peak_ivs_max[p] % 5) - (max_ivs[b] % 5)) % 5
                        ) * (know_char)
                    else:
                        max_ivs[b] = (
                            peak_ivs_max[p]
                            - (((peak_ivs_max[p] % 5) - (max_ivs[b] % 5)) % 5)
                            * (know_char)
                            - (1 - best_stats[b])
                        )
        print("MAX", max_ivs, "MIN", min_ivs)
        sum_iv = input(
            "How good does the iv judge say your iv total is? (Using Bulbapedia stats judge phrases): "
        )
        sum_iv = sum_iv.lower()
        sum_ivs_txt = [
            "average",
            "rather decent",
            "better-than-average",
            "better than average",
            "above-average",
            "above average",
            "quite impressive",
            "relatively superior",
            "outstanding",
        ]
        sum_ivs_min = [0, 0, 91, 91, 91, 91, 121, 121, 151]
        sum_ivs_max = [90, 90, 120, 120, 120, 120, 150, 150, 186]
        for s in range(len(sum_ivs_txt)):
            if sum_iv == sum_ivs_txt[s]:
                sum_iv_min = sum_ivs_min[s]
                sum_iv_max = sum_ivs_max[s]
    # v_min / max to ivs
    print("MAX", max_ivs, "MIN", min_ivs)
    for o in range(6):
        if v_min[o] > 63:
            min_ivs[o] = max(v_min[o] - 63, min_ivs[o], 0)
            max_ivs[o] = min(max_ivs[o], 31)
        else:
            min_ivs[o] = max(min_ivs[o], 0)
            max_ivs[o] = min(v_max[o], max_ivs[o], 31)
    print("MAX", max_ivs, "MIN", min_ivs)
    know_hidden_power = 0
    if int(input("able to find hidden power type? 1 = Yes, 0 = No: ")) == 1:
        know_hidden_power = 1
        hidden_power_type = input("hidden power type: ")
        hidden_power_type = hidden_power_type.lower()
        hidden_power_types_txt = [
            "fighting",
            "flying",
            "poison",
            "ground",
            "rock",
            "bug",
            "ghost",
            "steel",
            "fire",
            "water",
            "grass",
            "electric",
            "psychic",
            "ice",
            "dragon",
            "dark",
        ]
        hidden_power_all_bitfields = []
        for h in range(len(hidden_power_types_txt)):
            if hidden_power_type == hidden_power_types_txt[h]:
                for H in range(64):
                    if H * 5 // 21 == h:
                        hidden_power_all_bitfields.append(H)
        hidden_power_xo = []
        hidden_power_bitfields = []
        wack_iv_order = [0, 1, 2, 5, 3, 4]
        for i in range(6):
            if min_ivs[wack_iv_order[i]] == max_ivs[wack_iv_order[i]]:
                for j in range(len(hidden_power_all_bitfields)):
                    if (min_ivs[wack_iv_order[i]] & 1) == (
                        (hidden_power_all_bitfields[j] >> i) & 1
                    ):
                        hidden_power_bitfields.append(hidden_power_all_bitfields[j])

        for y in range(6):
            unique = []
            for f in range(len(hidden_power_bitfields)):
                unique.append((hidden_power_bitfields[f] >> y) & 1)
            unique_1 = set(unique)
            if len(unique_1) == 1:
                hidden_power_xo.append(unique[0])
            else:
                hidden_power_xo.append(2)
        # hp, ATK, DEF, SPA, SPE, SPD
        for o in range(6):
            if (min_ivs[wack_iv_order[o]] & 1 != ((hidden_power_xo[o]) & 1)) and (
                hidden_power_xo[o] < 2
            ):
                min_ivs[wack_iv_order[o]] = (
                    min_ivs[wack_iv_order[o]]
                    + 1
                    + 4 * (best_ivs[wack_iv_order[o]] or best_stats[wack_iv_order[o]])
                )
            if (max_ivs[wack_iv_order[o]] & 1 != ((hidden_power_xo[o]) & 1)) and (
                hidden_power_xo[o] < 2
            ):
                max_ivs[wack_iv_order[o]] = (
                    max_ivs[wack_iv_order[o]]
                    - 1
                    - 4 * (best_ivs[wack_iv_order[o]] or best_stats[wack_iv_order[o]])
                )
    wack_hp_order = [0, 1, 2, 4, 5, 3]
    if know_judge:
        for i in range(6):
            # Check if a min_iv and 5 max_ivs is above the minimum iv total.
            if sum(max_ivs[0:i] + max_ivs[i + 1 : 6], min_ivs[i]) < sum_iv_min:
                # If not, raise that minimum.
                temp = sum_iv_min - sum(max_ivs[0:i] + max_ivs[i + 1 : 6])
                if i == char_stat:
                    if know_hidden_power == 1:
                        if hidden_power_xo[wack_hp_order[i]] < 2:
                            min_ivs[i] = temp + (((min_ivs[i] % 10) - (temp % 10)) % 10)
                        else:
                            min_ivs[i] = temp + (((min_ivs[i] % 5) - (temp % 5)) % 5)
                    else:
                        min_ivs[i] = temp + (((min_ivs[i] % 5) - (temp % 5)) % 5)
                elif know_hidden_power == 1:
                    if hidden_power_xo[wack_hp_order[i]] < 2:
                        min_ivs[i] = temp + (((min_ivs[i] % 2) - (temp % 2)) % 2)
                    else:
                        min_ivs[i] = temp
                else:
                    min_ivs[i] = temp
            # Check if a max_iv and 5 min_ivs is below the maximum iv total.
        for i in range(6):
            if sum(min_ivs[0:i] + min_ivs[i + 1 : 6], max_ivs[i]) > sum_iv_max:
                # If not, lower that maximum.
                temp = sum_iv_max - sum(min_ivs[0:i] + min_ivs[i + 1 : 6])
                if i == char_stat:
                    if know_hidden_power == 1:
                        if hidden_power_xo[wack_hp_order[i]] < 2:
                            max_ivs[i] = temp - (((max_ivs[i] % 10) - (temp % 10) % 10))
                        else:
                            max_ivs[i] = temp - (((max_ivs[i] % 5) - (temp % 5) % 5))
                    else:
                        max_ivs[i] = temp - (((max_ivs[i] % 5) - (temp % 5) % 5))
                elif know_hidden_power == 1:
                    if hidden_power_xo[wack_hp_order[i]] < 2:
                        temp = temp - ((max_ivs[i] % 2) - (temp % 2) % 2)
                        max_ivs[i] = max_ivs[i] - (max_ivs[char_stat] < temp)
                    else:
                        max_ivs[i] = temp
                else:
                    max_ivs[i] = temp
    print(min_ivs, max_ivs)
    try:
        effort_ribbon = int(
            input(
                "Qualifies for effort ribbon? Yes = 1, No = 0, leave blank if unknown: "
            )
        )
    except:
        effort_ribbon = ""
    min_evs = []
    max_evs = []

    # Convert ivs to evs using v_max and v_min.
    for i in range(6):
        min_evs.append(max((v_min[i] - max_ivs[i]) * 4, 0))
        max_evs.append(min(max(v_max[i] - min_ivs[i], 0) * 4 + 3, 255))
    print(max_evs, min_evs)
    # How much info can we squeeze out of the evs using vitamins and the effort ribbon? Too much for me to keep straight lmao
    if effort_ribbon != 1:
        print(
            "\nThis next step will require you to buy/use up to 10 vitamins at a time, but you will be able to reset to before you purchased them afterward."
        )
        # If the player cannot buy more than n vitamins, we want to know that before we start calcs. This assumes the player is able to buy vitamins, which might be a bad assumption.
        afford_vitamin = int(
            input(
                "How many of a single type of vitamin can you afford, if you sell your items? Please check, and input a number higher than 10 if possible: "
            )
        )
        # vitamins fail after their individual ev is at or above 100. They will also fail if the pokemon has max evs.
        print(
            "For the next step, attempt to feed as many of an ev-boosting of vitamin as you can to your pokemon, and take note of how many it took for the mon to refuse more."
            + (effort_ribbon == 0) * " Then, check the effort ribbon again."
            + " Once you do, reset the game and attempt for the other 5 vitamin types."
        )
        vitamin_string = input(
            'With the evs it currently has, how many of each type of vitamin will your pokemon accept (resetting in between types)? \nSubmit your answer if a format like this, "1/2/3/4/5/6" \nFor the vitamins hp-Up/Protein/Iron/Calcium/Zinc/Carbos: '
        )
        vitamins = vitamin_string.split("/")
        for i in range(6):
            vitamins[i] = int(vitamins[i])
        if effort_ribbon == 0:
            # effort_ribbon NOT obtained, therefore effort judge available.
            # Use effort_ribbon to determine if the individual cap triggered, or if the pokemon hit 510 total evs.
            effort_vitamin_string = input(
                'Which of the vitamins caused your pokemon to receive the effort ribbon?\nSubmit your answer in a format like this, "0/1/0/1/0/1", where 1 = Yes, 0 = No. \nFor the vitamins hp-Up/Protein/Iron/Calcium/Zinc/Carbos: '
            )
            effort_vitamins = effort_vitamin_string.split("/")
            for i in range(6):
                effort_vitamins[i] = int(effort_vitamins[i])
            print(effort_vitamins)
            if effort_vitamin_string != "0/0/0/0/0/0":
                # No need for cross vitamins if we already hit the global ev cap.
                for i in range(6):
                    cross_vitamin = 0
                    cross_vitamin = max(vitamins[i] * effort_vitamins[i], cross_vitamin)
    
            else:
                # Can we hit the global ev cap?
                cross_vitamin = input(
                    "Now attempt to feed your pokemon "
                    + str(min(sum(vitamins), afford_vitamin))
                    + " total vitamins. \nInput the number of total vitamins your pokemon would consume before refusing more. Then check the effort ribbon. \nLeave blank if it gobbled up every single vitamin you could buy and still doesn't qualify for the effort ribbon': "
                )
            if cross_vitamin == "":
                # We never hit the global ev cap, and therefore don't know how few total evs the pokemon could have.
                sum_ev_min = 0
                cross_vitamin = min(sum(vitamins), afford_vitamin)
            else:
                # We hit the global ev cap, and therefore know the pokemon must have at least this many evs
                sum_ev_min = 510 - int(cross_vitamin) * 10
            # Keep in mind, a vitamin will provide less than 10 of an ev to not exceed the individual 100 ev cap.
            # Worst-case scenario, this means each unique vitamin type fed could give +1 once instead of +10.
            # This means our max ev sum is slightly high in most cases, the logic to fix that is rarely necessary and stupidly complicated.
            total = 0
            for i in range(6):
                total = total + (vitamins[i] > 0)
            sum_ev_max = 510 - int(cross_vitamin) * 10 + 9 * total
            uncapped_vitamins = []
            # Which evs did we potentially not hit the Individual Cap for?
            # This could happen if the Global ev cap is hit first, or if the player can't afford enough vitamins
            for i in range(6):
                uncapped_vitamins.append(
                    (effort_vitamins[i] or 1 * (vitamins[i] >= afford_vitamin))
                )
        elif effort_ribbon == "":
            # effort_ribbon status unknown, therefore effort judge NOT available
            # Therefore we always need to do cross_vitamins
            cross_vitamin = input(
                "Now attempt to feed your pokemon "
                + str(min(sum(vitamins), afford_vitamin))
                + " total vitamins of different types. \nInput the number of total vitamins your pokemon would consume before refusing more: "
            )
            total = 0
            for i in range(6):
                total = total + (vitamins[i] > 0)
            if cross_vitamin == "":
                # Potentially didn't hit global ev cap. Safe assumption is that we didn't.
                sum_ev_min = 0
                # cross vitamin isn't an int, therefore we use the max vitamins input
                cross_vitamin = min(sum(vitamins), afford_vitamin)
            else:
                # We hit the global ev cap!
                sum_ev_min = 510 - int(cross_vitamin) * 10
            sum_ev_max = 510 - int(cross_vitamin) * 10 + 9 * total
            # Unless we hit a global cap with cross vitamins, we can only confirm we hit the individual ev cap for some of the evs.
            # The highest vitamin proves that any ev cap hit below it got hit.
            uncapped_vitamins = []
            # Python doesn't like it when I multiply lists by constants, or lists by lists...
            vitamin_max = cross_vitamin + 0
            for i in range(6):
                vitamin_max = max(vitamins[i], vitamin_max)
            for i in range(6):
                uncapped_vitamins.append(
                    (vitamins[i] >= vitamin_max) or (vitamins[i] >= afford_vitamin)
                )
        for i in range(6):
            if vitamins[i] == 0:
                max_evs[i] = min(255, max_evs[i])
            else:
                max_evs[i] = min(109 - vitamins[i] * 10, max_evs[i])
            if uncapped_vitamins[i] == 1:
                min_evs[i] = max(0, min_evs[i])
            else:
                min_evs[i] = max(100 - vitamins[i] * 10, min_evs[i])
    if effort_ribbon != "":
        if effort_ribbon == 1:
            sum_ev_min = 510
            sum_ev_max = 510
        else:
            sum_ev_min = max(0, sum_ev_min)
            sum_ev_max = min(510, sum_ev_max)
        print(max_evs, min_evs)
        for i in range(6):
            # Check if a min_ev and 5 max_evs is above the minimum ev total.
            if sum(max_evs[0:6], min_evs[i]) - max_evs[i] < sum_ev_min:
                # If not, raise that minimum.
                temp = sum_ev_min - sum(max_evs[0:6], -max_evs[i])
                min_evs[i] = max(temp, 0)
        print(min_evs)
        # Check if a max_ev and 5 min_evs is below the maximum ev total.
        for i in range(6):
            if sum(min_evs[0:6], max_evs[i]) - min_evs[i] > sum_ev_max:
                # If not, raise that maximum.
                temp = sum_ev_max - sum(min_evs[0:6], -min_evs[i])
                max_evs[i] = min(max(temp, 0), 255)
        print(max_evs)
        for i in range(6):
            temp = max(v_min[i] - (max_evs[i] // 4), min_ivs[i], 0)
            if i == char_stat:
                if know_hidden_power == 1:
                    if hidden_power_xo[wack_hp_order[i]] < 2:
                        min_ivs[i] = temp + (((min_ivs[i] % 10) - (temp % 10)) % 10)
                    else:
                        min_ivs[i] = temp + (((min_ivs[i] % 5) - (temp % 5)) % 5)
                else:
                    min_ivs[i] = temp + (((min_ivs[i] % 5) - (temp % 5)) % 5)
            elif know_hidden_power == 1:
                if hidden_power_xo[wack_hp_order[i]] < 2:
                    min_ivs[i] = temp + (((min_ivs[i] % 2) - (temp % 2)) % 2)
                else:
                    min_ivs[i] = temp
            else:
                min_ivs[i] = temp

        temp = min(max(v_max[i] - (min_evs[i] // 4), 0), max_ivs[i], 31)
        if temp != max_ivs[i]:
            if i == char_stat:
                if know_hidden_power == 1:
                    if hidden_power_xo[wack_hp_order[i]] < 2:
                        max_ivs[i] = temp - (((max_ivs[i] % 10) - (temp % 10) % 10))
                    else:
                        max_ivs[i] = temp - (((max_ivs[i] % 5) - (temp % 5) % 5))
                else:
                    max_ivs[i] = temp - (((max_ivs[i] % 5) - (temp % 5) % 5))
            elif know_hidden_power == 1:
                if hidden_power_xo[wack_hp_order[i]] < 2:
                    max_ivs[i] = temp - ((max_ivs[i] % 2) - (temp % 2) % 2)
                else:
                    max_ivs[i] = temp
            else:
                max_ivs[i] = temp
    print(max_evs, min_evs)
    print("max ivs:", max_ivs, "min ivs:", min_ivs)
# Ez Test Code
stats = [244, 179, 133, 137, 161, 118]
stats_to_ivs("Swampert", 68, "Gentle", stats)
def FindIVs(species):
    stats = [
        int(input("hp stat: ")),
        int(input("atk stat: ")),
        int(input("def stat: ")),
        int(input("spa stat: ")),
        int(input("SpD stat: ")),
        int(input("spe stat: ")),
    ]
    
    return stats_to_ivs(species, int(input("level: ")), input("nature: "), stats)
# FindIVs()
