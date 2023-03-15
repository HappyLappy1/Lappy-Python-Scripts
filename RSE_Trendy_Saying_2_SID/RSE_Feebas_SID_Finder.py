# Majority of this done by Shao.
# I (Lappy) just made it look pretty, added user inputs, and made an infographic.
# Infographic:
# https://github.com/HappyLappy1/Lappy-Python-Scripts/blob/main/RSE_Trendy_Saying_2_SID/RSE_Feebas_Tiles_Index.png
class PokeRNG:
    """Standard LCRNG used in RSE"""

    add = 0x6073
    mult = 0x41C64E6D

    def __init__(self, seed: int) -> None:
        self.seed: int = seed & 0xFFFFFFFF
        self.prev_mult: int = pow(self.mult, -1, 2**32)
        self.prev_add: int = (self.add * self.prev_mult) & 0xFFFFFFFF

    def next(self) -> int:
        """Advance the LCRNG and return the next seed"""
        self.seed = (self.seed * self.mult + self.add) & 0xFFFFFFFF
        return self.seed

    def prev(self) -> int:
        """Advance the LCRNG backwards and return the previous seed"""
        self.seed = (self.seed * self.prev_mult + self.prev_add) & 0xFFFFFFFF
        return self.seed

    def advance(self, adv: int) -> None:
        """Advance the LCRNG in either direction"""
        if adv >= 0:
            for _ in range(adv):
                self.next()
        else:
            for _ in range(-adv):
                self.prev()

    def next_u16(self) -> int:
        """Advance the LCRNG and return the next 16-bit high"""
        return self.next() >> 16

    def prev_u16(self) -> int:
        """Advance the LCRNG backwards and return the previous 16-bit high"""
        return self.prev() >> 16

    def next_rand(self, maximum: int) -> int:
        """Advance the LCRNG and return the next rand [0, maximum)"""
        return self.next_u16() % maximum

    def prev_rand(self, maximum: int) -> int:
        """Advance the LCRNG backwards return the previous rand [0, maximum)"""
        return self.prev_u16() % maximum


class MRNG(PokeRNG):
    """Secondary RNG used in RSE"""

    add = 0x3039


def generate_feebas_seed(seed: int) -> int:
    """Generate feebas seed from rng state"""
    rng = PokeRNG(seed)
    trends = []
    for _ in range(5):
        rng.advance(4)
        rand = rng.next_rand(98)
        if rand > 50:
            rand = rng.next_rand(98)
            if rand > 80:
                rand = rng.next_rand(98)
        max_trend = rand + 30
        trend = rng.next_rand(rand + 1) + 30
        rand = rng.next_u16()
        trends.append(((trend, max_trend), rand))
    feebas_trend = trends.pop(0)
    # only need to sort the first index
    for trend in trends:
        if (trend[0] > feebas_trend[0]) or (
            trend[0] == feebas_trend[0] and rng.next_rand(2)
        ):
            feebas_trend = trend
    return feebas_trend[1]


def generate_feebas_spots(seed: int):
    """Generate feebas spots from feebas seed"""
    spots = set()
    rng = MRNG(seed)
    # generate 6 spots
    while len(spots) < 6:
        spot = rng.next_rand(447)
        if spot == 0:
            spot = 447
        # inaccessible tiles that are skipped over
        if spot >= 4:
            spots.add(spot)
    return spots


def emerald_sid_from_spots(
    tid: int, known_spots: set, min_advances: int, max_advances: int
):
    """Search for Emerald SID based on known feebas spots"""
    rng = PokeRNG(tid)
    rng.advance(min_advances)
    results_found = False
    for advance in range(min_advances, max_advances):
        go = PokeRNG(rng.seed)
        sid_3 = go.next_u16()
        sid_2 = go.next_u16()
        go.advance(2)  # 2 vblanks
        test_spots = generate_feebas_spots(generate_feebas_seed(go.seed))
        if all(known_spot in test_spots for known_spot in known_spots):
            print(
                f"SID: {sid_3} matches your feebas seed "
                f"on advance {advance} with 3 Vblanks and spots {test_spots}"
            )
            print(
                f"SID: {sid_2} matches your feebas seed "
                f"on advance {advance + 1} with 2 Vblanks and spots {test_spots}"
            )
            results_found = True
        rng.next()

    if not results_found:
        print("No Results found!")


def rs_sid_from_spots(
    tid: int,
    known_spots: set,
    min_advances: int,
    max_advances: int,
):
    """Search for Ruby/Sapphire SID based on known feebas spots"""
    rng = PokeRNG(0x5A0)
    rng.advance(min_advances)
    results_found = False
    for advance in range(min_advances, max_advances):
        go = PokeRNG(rng.seed)
        sid = go.next_u16()
        if tid == go.next_u16():
            go.next()
            test_spots = generate_feebas_spots(generate_feebas_seed(go.next()))
            if all(spot in test_spots for spot in known_spots):
                print(
                    f"SID: {sid} is consistent on "
                    f"advance {advance} with 2 Vblanks and spots {test_spots}"
                )
                results_found = True
            test_spots = generate_feebas_spots(generate_feebas_seed(go.next()))
            if all(spot in test_spots for spot in known_spots):
                print(
                    f"SID: {sid} matches your feebas seed "
                    f"on advance {advance - 3} with 3 Vblanks and spots {test_spots}"
                )
                results_found = True
        rng.next()
    if not results_found:
        print("No Results found!")


print(
    "Tiles 1, 2, and 3 are inaccesible water tiles. "
    "However, the game intentionally rerolls them if they are ever selected."
)
print(
    "Tiles 105, 119, 132 and 144 are land tiles the player cannot fish on. "
    "The game can generate feebas on these tiles"
)
print(
    "Tiles 296, 297 and 298 are inaccessible water tiles that can contain feebas. "
    "The game can generate feebas on these tiles."
)

tid = int(input("Trainer ID: "))
feebas_tiles = {
    int(tile.strip())
    for tile in input(
        "Known Feebas Tile Indices Separated by Commas (See infographic for conversion): "
    ).split(",")
}
min_advances = int(input("Minimum Advances: "))
max_advances = int(input("Maximum Advances: "))
if (
    input(
        "Which Game Version are you attempting to find the Secret ID of? "
        "Emerald = 1, Ruby/Sapphire = 0: "
    )
    == "1"
):
    emerald_sid_from_spots(tid, feebas_tiles, min_advances, max_advances)
else:
    rs_sid_from_spots(tid, feebas_tiles, min_advances, max_advances)
