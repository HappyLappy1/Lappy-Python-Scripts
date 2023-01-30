# -*- coding: utf-8 -*-
print("This tool is only accurate for gens 3-5. Base Stats changed in gen 6+, as did the IV Judge.")
def Stats2TVs(Species, Level, Nature, Stats):
    Species_List = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree", "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot", "Rattata", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok", "Pikachu", "Raichu", "Sandshrew", "Sandslash", "Nidoran♀", "Nidorina", "Nidoqueen", "Nidoran♂", "Nidorino", "Nidoking", "Clefairy", "Clefable", "Vulpix", "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat", "Golbat", "Oddish", "Gloom", "Vileplume", "Paras", "Parasect", "Venonat", "Venomoth", "Diglett", "Dugtrio", "Meowth", "Persian", "Psyduck", "Golduck", "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag", "Poliwhirl", "Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop", "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel", "Tentacool", "Tentacruel", "Geodude", "Graveler", "Golem", "Ponyta", "Rapidash", "Slowpoke", "Slowbro", "Magnemite", "Magneton", "Farfetch'd", "Doduo", "Dodrio", "Seel", "Dewgong", "Grimer", "Muk", "Shellder", "Cloyster", "Gastly", "Haunter", "Gengar", "Onix", "Drowzee", "Hypno", "Krabby", "Kingler", "Voltorb", "Electrode", "Exeggcute", "Exeggutor", "Cubone", "Marowak", "Hitmonlee", "Hitmonchan", "Lickitung", "Koffing", "Weezing", "Rhyhorn", "Rhydon", "Chansey", "Tangela", "Kangaskhan", "Horsea", "Seadra", "Goldeen", "Seaking", "Staryu", "Starmie", "Mr. Mime", "Scyther", "Jynx", "Electabuzz", "Magmar", "Pinsir", "Tauros", "Magikarp", "Gyarados", "Lapras", "Ditto", "Eevee", "Vaporeon", "Jolteon", "Flareon", "Porygon", "Omanyte", "Omastar", "Kabuto", "Kabutops", "Aerodactyl", "Snorlax", "Articuno", "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite", "Mewtwo", "Mew", "Chikorita", "Bayleef", "Meganium", "Cyndaquil", "Quilava", "Typhlosion", "Totodile", "Croconaw", "Feraligatr", "Sentret", "Furret", "Hoothoot", "Noctowl", "Ledyba", "Ledian", "Spinarak", "Ariados", "Crobat", "Chinchou", "Lanturn", "Pichu", "Cleffa", "Igglybuff", "Togepi", "Togetic", "Natu", "Xatu", "Mareep", "Flaaffy", "Ampharos", "Bellossom", "Marill", "Azumarill", "Sudowoodo", "Politoed", "Hoppip", "Skiploom", "Jumpluff", "Aipom", "Sunkern", "Sunflora", "Yanma", "Wooper", "Quagsire", "Espeon", "Umbreon", "Murkrow", "Slowking", "Misdreavus", "Unown", "Wobbuffet", "Girafarig", "Pineco", "Forretress", "Dunsparce", "Gligar", "Steelix", "Snubbull", "Granbull", "Qwilfish", "Scizor", "Shuckle", "Heracross", "Sneasel", "Teddiursa", "Ursaring", "Slugma", "Magcargo", "Swinub", "Piloswine", "Corsola", "Remoraid", "Octillery", "Delibird", "Mantine", "Skarmory", "Houndour", "Houndoom", "Kingdra", "Phanpy", "Donphan", "Porygon2", "Stantler", "Smeargle", "Tyrogue", "Hitmontop", "Smoochum", "Elekid", "Magby", "Miltank", "Blissey", "Raikou", "Entei", "Suicune", "Larvitar", "Pupitar", "Tyranitar", "Lugia", "Ho-Oh", "Celebi", "Treecko", "Grovyle", "Sceptile", "Torchic", "Combusken", "Blaziken", "Mudkip", "Marshtomp", "Swampert", "Poochyena", "Mightyena", "Zigzagoon", "Linoone", "Wurmple", "Silcoon", "Beautifly", "Cascoon", "Dustox", "Lotad", "Lombre", "Ludicolo", "Seedot", "Nuzleaf", "Shiftry", "Taillow", "Swellow", "Wingull", "Pelipper", "Ralts", "Kirlia", "Gardevoir", "Surskit", "Masquerain", "Shroomish", "Breloom", "Slakoth", "Vigoroth", "Slaking", "Nincada", "Ninjask", "Shedinja", "Whismur", "Loudred", "Exploud", "Makuhita", "Hariyama", "Azurill", "Nosepass", "Skitty", "Delcatty", "Sableye", "Mawile", "Aron", "Lairon", "Aggron", "Meditite", "Medicham", "Electrike", "Manectric", "Plusle", "Minun", "Volbeat", "Illumise", "Roselia", "Gulpin", "Swalot", "Carvanha", "Sharpedo", "Wailmer", "Wailord", "Numel", "Camerupt", "Torkoal", "Spoink", "Grumpig", "Spinda", "Trapinch", "Vibrava", "Flygon", "Cacnea", "Cacturne", "Swablu", "Altaria", "Zangoose", "Seviper", "Lunatone", "Solrock", "Barboach", "Whiscash", "Corphish", "Crawdaunt", "Baltoy", "Claydol", "Lileep", "Cradily", "Anorith", "Armaldo", "Feebas", "Milotic", "Castform", "Kecleon", "Shuppet", "Banette", "Duskull", "Dusclops", "Tropius", "Chimecho", "Absol", "Wynaut", "Snorunt", "Glalie", "Spheal", "Sealeo", "Walrein", "Clamperl", "Huntail", "Gorebyss", "Relicanth", "Luvdisc", "Bagon", "Shelgon", "Salamence", "Beldum", "Metang", "Metagross", "Regirock", "Regice", "Registeel", "Latias", "Latios", "Kyogre", "Groudon", "Rayquaza", "Jirachi", "Deoxys (Normal Forme)", "Deoxys (Attack Forme)", "Deoxys (Defense Forme)", "Deoxys (Speed Forme)", "Turtwig", "Grotle", "Torterra", "Chimchar", "Monferno", "Infernape", "Piplup", "Prinplup", "Empoleon", "Starly", "Staravia", "Staraptor", "Bidoof", "Bibarel", "Kricketot", "Kricketune", "Shinx", "Luxio", "Luxray", "Budew", "Roserade", "Cranidos", "Rampardos", "Shieldon", "Bastiodon", "Burmy", "Wormadam (Plant Cloak)", "Wormadam (Sandy Cloak)", "Wormadam (Trash Cloak)", "Mothim", "Combee", "Vespiquen", "Pachirisu", "Buizel", "Floatzel", "Cherubi", "Cherrim", "Shellos", "Gastrodon", "Ambipom", "Drifloon", "Drifblim", "Buneary", "Lopunny", "Mismagius", "Honchkrow", "Glameow", "Purugly", "Chingling", "Stunky", "Skuntank", "Bronzor", "Bronzong", "Bonsly", "Mime Jr.", "Happiny", "Chatot", "Spiritomb", "Gible", "Gabite", "Garchomp", "Munchlax", "Riolu", "Lucario", "Hippopotas", "Hippowdon", "Skorupi", "Drapion", "Croagunk", "Toxicroak", "Carnivine", "Finneon", "Lumineon", "Mantyke", "Snover", "Abomasnow", "Weavile", "Magnezone", "Lickilicky", "Rhyperior", "Tangrowth", "Electivire", "Magmortar", "Togekiss", "Yanmega", "Leafeon", "Glaceon", "Gliscor", "Mamoswine", "Porygon-Z", "Gallade", "Probopass", "Dusknoir", "Froslass", "Rotom", "Rotom (Heat Rotom)", "Rotom (Wash Rotom)", "Rotom (Frost Rotom)", "Rotom (Fan Rotom)", "Rotom (Mow Rotom)", "Uxie", "Mesprit", "Azelf", "Dialga", "Palkia", "Heatran", "Regigigas", "Giratina (Altered Forme)", "Giratina (Origin Forme)", "Cresselia", "Phione", "Manaphy", "Darkrai", "Shaymin (Land Forme)", "Shaymin (Sky Forme)", "Arceus"]
    HP_List = [45, 60, 80, 39, 58, 78, 44, 59, 79, 45, 50, 60, 40, 45, 65, 40, 63, 83, 30, 55, 40, 65, 35, 60, 35, 60, 50, 75, 55, 70, 90, 46, 61, 81, 70, 95, 38, 73, 115, 140, 40, 75, 45, 60, 75, 35, 60, 60, 70, 10, 35, 40, 65, 50, 80, 40, 65, 55, 90, 40, 65, 90, 25, 40, 55, 70, 80, 90, 50, 65, 80, 40, 80, 40, 55, 80, 50, 65, 90, 95, 25, 50, 52, 35, 60, 65, 90, 80, 105, 30, 50, 30, 45, 60, 35, 60, 85, 30, 55, 40, 60, 60, 95, 50, 60, 50, 50, 90, 40, 65, 80, 105, 250, 65, 105, 30, 55, 45, 80, 30, 60, 40, 70, 65, 65, 65, 65, 75, 20, 95, 130, 48, 55, 130, 65, 65, 65, 35, 70, 30, 60, 80, 160, 90, 90, 90, 41, 61, 91, 106, 100, 45, 60, 80, 39, 58, 78, 50, 65, 85, 35, 85, 60, 100, 40, 55, 40, 70, 85, 75, 125, 20, 50, 90, 35, 55, 40, 65, 55, 70, 90, 75, 70, 100, 70, 90, 35, 55, 75, 55, 30, 75, 65, 55, 95, 65, 95, 60, 95, 60, 48, 190, 70, 50, 75, 100, 65, 75, 60, 90, 65, 70, 20, 80, 55, 60, 90, 40, 50, 50, 100, 55, 35, 75, 45, 65, 65, 45, 75, 75, 90, 90, 85, 73, 55, 35, 50, 45, 45, 45, 95, 255, 90, 115, 100, 50, 70, 100, 106, 106, 100, 40, 50, 70, 45, 60, 80, 50, 70, 100, 35, 70, 38, 78, 45, 50, 60, 50, 60, 40, 60, 80, 40, 70, 90, 40, 60, 40, 60, 28, 38, 68, 40, 70, 60, 60, 60, 80, 150, 31, 61, 1, 64, 84, 104, 72, 144, 50, 30, 50, 70, 50, 50, 50, 60, 70, 30, 60, 40, 70, 60, 60, 65, 65, 50, 70, 100, 45, 70, 130, 170, 60, 70, 70, 60, 80, 60, 45, 50, 80, 50, 70, 45, 75, 73, 73, 70, 70, 50, 110, 43, 63, 40, 60, 66, 86, 45, 75, 20, 95, 70, 60, 44, 64, 20, 40, 99, 65, 65, 95, 50, 80, 70, 90, 110, 35, 55, 55, 100, 43, 45, 65, 95, 40, 60, 80, 80, 80, 80, 80, 80, 100, 100, 105, 100, 50, 50, 50, 50, 55, 75, 95, 44, 64, 76, 53, 64, 84, 40, 55, 85, 59, 79, 37, 77, 45, 60, 80, 40, 60, 67, 97, 30, 60, 40, 60, 60, 60, 70, 30, 70, 60, 55, 85, 45, 70, 76, 111, 75, 90, 150, 55, 65, 60, 100, 49, 71, 45, 63, 103, 57, 67, 50, 20, 100, 76, 50, 58, 68, 108, 135, 40, 70, 68, 108, 40, 70, 48, 83, 74, 49, 69, 45, 60, 90, 70, 70, 110, 115, 100, 75, 75, 85, 86, 65, 65, 75, 110, 85, 68, 60, 45, 70, 50, 50, 50, 50, 50, 50, 75, 80, 75, 100, 90, 91, 110, 150, 150, 120, 80, 100, 70, 100, 100, 120]
    Atk_List = [49, 62, 82, 52, 64, 84, 48, 63, 83, 30, 20, 45, 35, 25, 80, 45, 60, 80, 56, 81, 60, 90, 60, 85, 55, 90, 75, 100, 47, 62, 82, 57, 72, 92, 45, 70, 41, 76, 45, 70, 45, 80, 50, 65, 80, 70, 95, 55, 65, 55, 80, 45, 70, 52, 82, 80, 105, 70, 110, 50, 65, 85, 20, 35, 50, 80, 100, 130, 75, 90, 105, 40, 70, 80, 95, 110, 85, 100, 65, 75, 35, 60, 65, 85, 110, 45, 70, 80, 105, 65, 95, 35, 50, 65, 45, 48, 73, 105, 130, 30, 50, 40, 95, 50, 80, 120, 105, 55, 65, 90, 85, 130, 5, 55, 95, 40, 65, 67, 92, 45, 75, 45, 110, 50, 83, 95, 125, 100, 10, 125, 85, 48, 55, 65, 65, 130, 60, 40, 60, 80, 115, 105, 110, 85, 90, 100, 64, 84, 134, 110, 100, 49, 62, 82, 52, 64, 84, 65, 80, 105, 46, 76, 30, 50, 20, 35, 60, 90, 90, 38, 58, 40, 25, 30, 20, 40, 50, 75, 40, 55, 75, 80, 20, 50, 100, 75, 35, 45, 55, 70, 30, 75, 65, 45, 85, 65, 65, 85, 75, 60, 72, 33, 80, 65, 90, 70, 75, 85, 80, 120, 95, 130, 10, 125, 95, 80, 130, 40, 50, 50, 100, 55, 65, 105, 55, 40, 80, 60, 90, 95, 60, 120, 80, 95, 20, 35, 95, 30, 63, 75, 80, 10, 85, 115, 75, 64, 84, 134, 90, 130, 100, 45, 65, 85, 60, 85, 120, 70, 85, 110, 55, 90, 30, 70, 45, 35, 70, 35, 50, 30, 50, 70, 40, 70, 100, 55, 85, 30, 50, 25, 35, 65, 30, 60, 40, 130, 60, 80, 160, 45, 90, 90, 51, 71, 91, 60, 120, 20, 45, 45, 65, 75, 85, 70, 90, 110, 40, 60, 45, 75, 50, 40, 73, 47, 60, 43, 73, 90, 120, 70, 90, 60, 100, 85, 25, 45, 60, 100, 70, 100, 85, 115, 40, 70, 115, 100, 55, 95, 48, 78, 80, 120, 40, 70, 41, 81, 95, 125, 15, 60, 70, 90, 75, 115, 40, 70, 68, 50, 130, 23, 50, 80, 40, 60, 80, 64, 104, 84, 90, 30, 75, 95, 135, 55, 75, 135, 100, 50, 75, 80, 90, 100, 150, 150, 100, 150, 180, 70, 95, 68, 89, 109, 58, 78, 104, 51, 66, 86, 55, 75, 120, 45, 85, 25, 85, 65, 85, 120, 30, 70, 125, 165, 42, 52, 29, 59, 79, 69, 94, 30, 80, 45, 65, 105, 35, 60, 48, 83, 100, 50, 80, 66, 76, 60, 125, 55, 82, 30, 63, 93, 24, 89, 80, 25, 5, 65, 92, 70, 90, 130, 85, 70, 110, 72, 112, 50, 90, 61, 106, 100, 49, 69, 20, 62, 92, 120, 70, 85, 140, 100, 123, 95, 50, 76, 110, 60, 95, 130, 80, 125, 55, 100, 80, 50, 65, 65, 65, 65, 65, 75, 105, 125, 120, 120, 90, 160, 100, 120, 70, 80, 100, 90, 100, 103, 120]
    Def_List = [49, 63, 83, 43, 58, 78, 65, 80, 100, 35, 55, 50, 30, 50, 40, 40, 55, 75, 35, 60, 30, 65, 44, 69, 30, 55, 85, 110, 52, 67, 87, 40, 57, 77, 48, 73, 40, 75, 20, 45, 35, 70, 55, 70, 85, 55, 80, 50, 60, 25, 50, 35, 60, 48, 78, 35, 60, 45, 80, 40, 65, 95, 15, 30, 45, 50, 70, 80, 35, 50, 65, 35, 65, 100, 115, 130, 55, 70, 65, 110, 70, 95, 55, 45, 70, 55, 80, 50, 75, 100, 180, 30, 45, 60, 160, 45, 70, 90, 115, 50, 70, 80, 85, 95, 110, 53, 79, 75, 95, 120, 95, 120, 5, 115, 80, 70, 95, 60, 65, 55, 85, 65, 80, 35, 57, 57, 100, 95, 55, 79, 80, 48, 50, 60, 60, 60, 70, 100, 125, 90, 105, 65, 65, 100, 85, 90, 45, 65, 95, 90, 100, 65, 80, 100, 43, 58, 78, 64, 80, 100, 34, 64, 30, 50, 30, 50, 40, 70, 80, 38, 58, 15, 28, 15, 65, 85, 45, 70, 40, 55, 75, 85, 50, 80, 115, 75, 40, 50, 70, 55, 30, 55, 45, 45, 85, 60, 110, 42, 80, 60, 48, 58, 65, 90, 140, 70, 105, 200, 50, 75, 75, 100, 230, 75, 55, 50, 75, 40, 120, 40, 80, 85, 35, 75, 45, 70, 140, 30, 50, 95, 60, 120, 90, 62, 35, 35, 95, 15, 37, 37, 105, 10, 75, 85, 115, 50, 70, 110, 130, 90, 100, 35, 45, 65, 40, 60, 70, 50, 70, 90, 35, 70, 41, 61, 35, 55, 50, 55, 70, 30, 50, 70, 50, 40, 60, 30, 60, 30, 100, 25, 35, 65, 32, 62, 60, 80, 60, 80, 100, 90, 45, 45, 23, 43, 63, 30, 60, 40, 135, 45, 65, 75, 85, 100, 140, 180, 55, 75, 40, 60, 40, 50, 55, 55, 45, 53, 83, 20, 40, 35, 45, 40, 70, 140, 35, 65, 60, 45, 50, 80, 40, 60, 60, 90, 60, 60, 65, 85, 43, 73, 65, 85, 55, 105, 77, 97, 50, 100, 20, 79, 70, 70, 35, 65, 90, 130, 83, 70, 60, 48, 50, 80, 50, 70, 90, 85, 105, 105, 130, 55, 60, 100, 80, 80, 100, 130, 200, 100, 150, 90, 80, 90, 140, 90, 100, 50, 20, 160, 90, 64, 85, 105, 44, 52, 71, 53, 68, 88, 30, 50, 70, 40, 60, 41, 51, 34, 49, 79, 35, 55, 40, 60, 118, 168, 45, 85, 105, 95, 50, 42, 102, 70, 35, 55, 45, 70, 48, 68, 66, 34, 44, 44, 84, 60, 52, 42, 64, 50, 47, 67, 86, 116, 95, 45, 5, 45, 108, 45, 65, 95, 40, 40, 70, 78, 118, 90, 110, 40, 65, 72, 56, 76, 50, 50, 75, 65, 115, 95, 130, 125, 67, 67, 95, 86, 130, 110, 125, 80, 70, 65, 145, 135, 70, 77, 107, 107, 107, 107, 107, 130, 105, 70, 120, 100, 106, 110, 120, 100, 120, 80, 100, 90, 100, 75, 120]
    Spa_List = [65, 80, 100, 60, 80, 109, 50, 65, 85, 20, 25, 80, 20, 25, 45, 35, 50, 70, 25, 50, 31, 61, 40, 65, 50, 90, 20, 45, 40, 55, 75, 40, 55, 85, 60, 85, 50, 81, 45, 75, 30, 65, 75, 85, 100, 45, 60, 40, 90, 35, 50, 40, 65, 65, 95, 35, 60, 70, 100, 40, 50, 70, 105, 120, 135, 35, 50, 65, 70, 85, 100, 50, 80, 30, 45, 55, 65, 80, 40, 100, 95, 120, 58, 35, 60, 45, 70, 40, 65, 45, 85, 100, 115, 130, 30, 43, 73, 25, 50, 55, 80, 60, 125, 40, 50, 35, 35, 60, 60, 85, 30, 45, 35, 100, 40, 70, 95, 35, 65, 70, 100, 100, 55, 115, 95, 100, 55, 40, 15, 60, 85, 48, 45, 110, 110, 95, 85, 90, 115, 55, 65, 60, 65, 95, 125, 125, 50, 70, 100, 154, 100, 49, 63, 83, 60, 80, 109, 44, 59, 79, 35, 45, 36, 76, 40, 55, 40, 60, 70, 56, 76, 35, 45, 40, 40, 80, 70, 95, 65, 80, 115, 90, 20, 50, 30, 90, 35, 45, 55, 40, 30, 105, 75, 25, 65, 130, 60, 85, 100, 85, 72, 33, 90, 35, 60, 65, 35, 55, 40, 60, 55, 55, 10, 40, 35, 50, 75, 70, 80, 30, 60, 65, 65, 105, 65, 80, 40, 80, 110, 95, 40, 60, 105, 85, 20, 35, 35, 85, 65, 70, 40, 75, 115, 90, 90, 45, 65, 95, 90, 110, 100, 65, 85, 105, 70, 85, 110, 50, 60, 85, 30, 60, 30, 50, 20, 25, 90, 25, 50, 40, 60, 90, 30, 60, 90, 30, 50, 55, 85, 45, 65, 125, 50, 80, 40, 60, 35, 55, 95, 30, 50, 30, 51, 71, 91, 20, 40, 20, 45, 35, 55, 65, 55, 40, 50, 60, 40, 60, 65, 105, 85, 75, 47, 73, 100, 43, 73, 65, 95, 70, 90, 65, 105, 85, 70, 90, 60, 45, 50, 80, 85, 115, 40, 70, 60, 100, 95, 55, 46, 76, 50, 90, 40, 70, 61, 81, 40, 70, 10, 100, 70, 60, 63, 83, 30, 60, 72, 95, 75, 23, 50, 80, 55, 75, 95, 74, 94, 114, 45, 40, 40, 60, 110, 35, 55, 95, 50, 100, 75, 110, 130, 150, 100, 150, 100, 150, 180, 70, 95, 45, 55, 75, 58, 78, 104, 61, 81, 111, 30, 40, 50, 35, 55, 25, 55, 40, 60, 95, 50, 125, 30, 65, 42, 47, 29, 79, 59, 69, 94, 30, 80, 45, 60, 85, 62, 87, 57, 92, 60, 60, 90, 44, 54, 105, 105, 42, 64, 65, 41, 71, 24, 79, 10, 70, 15, 92, 92, 40, 50, 80, 40, 35, 115, 38, 68, 30, 60, 61, 86, 90, 49, 69, 60, 62, 92, 45, 130, 80, 55, 110, 95, 125, 120, 116, 60, 130, 45, 70, 135, 65, 75, 65, 80, 95, 105, 105, 105, 105, 105, 75, 105, 125, 150, 150, 130, 80, 100, 120, 75, 80, 100, 135, 100, 120, 120]
    Spd_List = [65, 80, 100, 50, 65, 85, 64, 80, 105, 20, 25, 80, 20, 25, 80, 35, 50, 70, 35, 70, 31, 61, 54, 79, 40, 80, 30, 55, 40, 55, 85, 40, 55, 75, 65, 90, 65, 100, 25, 50, 40, 75, 65, 75, 90, 55, 80, 55, 75, 45, 70, 40, 65, 50, 80, 45, 70, 50, 80, 40, 50, 90, 55, 70, 85, 35, 60, 85, 30, 45, 60, 100, 120, 30, 45, 65, 65, 80, 40, 80, 55, 70, 62, 35, 60, 70, 95, 50, 100, 25, 45, 35, 55, 75, 45, 90, 115, 25, 50, 55, 80, 45, 65, 50, 80, 110, 110, 75, 45, 70, 30, 45, 105, 40, 80, 25, 45, 50, 80, 55, 85, 120, 80, 95, 85, 85, 70, 70, 20, 100, 95, 48, 65, 95, 95, 110, 75, 55, 70, 45, 70, 75, 110, 125, 90, 85, 50, 70, 100, 90, 100, 65, 80, 100, 50, 65, 85, 48, 63, 83, 45, 55, 56, 96, 80, 110, 40, 60, 80, 56, 76, 35, 55, 20, 65, 105, 45, 70, 45, 60, 90, 100, 50, 80, 65, 100, 55, 65, 85, 55, 30, 85, 45, 25, 65, 95, 130, 42, 110, 85, 48, 58, 65, 35, 60, 65, 65, 65, 40, 60, 55, 80, 230, 95, 75, 50, 75, 40, 80, 30, 60, 85, 35, 75, 45, 140, 70, 50, 80, 95, 40, 60, 95, 65, 45, 35, 110, 65, 55, 55, 70, 135, 100, 75, 115, 50, 70, 100, 154, 154, 100, 55, 65, 85, 50, 60, 70, 50, 70, 90, 30, 60, 41, 61, 30, 25, 50, 25, 90, 50, 70, 100, 30, 40, 60, 30, 50, 30, 70, 35, 55, 115, 52, 82, 60, 60, 35, 55, 65, 30, 50, 30, 23, 43, 63, 30, 60, 40, 90, 35, 55, 65, 55, 40, 50, 60, 55, 75, 40, 60, 75, 85, 75, 75, 80, 53, 83, 20, 40, 35, 45, 45, 75, 70, 80, 110, 60, 45, 50, 80, 40, 60, 75, 105, 60, 60, 85, 65, 41, 71, 35, 55, 70, 120, 87, 107, 50, 80, 55, 125, 70, 120, 33, 63, 90, 130, 87, 80, 60, 48, 50, 80, 50, 70, 90, 55, 75, 75, 65, 65, 30, 50, 80, 60, 80, 90, 100, 200, 150, 130, 110, 140, 90, 90, 100, 50, 20, 160, 90, 55, 65, 85, 44, 52, 71, 56, 76, 101, 30, 40, 50, 40, 60, 41, 51, 34, 49, 79, 70, 105, 30, 50, 88, 138, 45, 105, 85, 95, 50, 42, 102, 90, 30, 50, 53, 78, 62, 82, 66, 44, 54, 56, 96, 105, 52, 37, 59, 50, 41, 61, 86, 116, 45, 90, 65, 42, 108, 45, 55, 85, 85, 40, 70, 42, 72, 55, 75, 40, 65, 72, 61, 86, 120, 60, 85, 85, 90, 95, 55, 50, 85, 95, 115, 56, 65, 95, 75, 60, 75, 115, 150, 135, 70, 77, 107, 107, 107, 107, 107, 130, 105, 70, 100, 120, 106, 110, 120, 100, 130, 80, 100, 90, 100, 75, 120]
    Spe_List = [45, 60, 80, 65, 80, 100, 43, 58, 78, 45, 30, 70, 50, 35, 75, 56, 71, 91, 72, 97, 70, 100, 55, 80, 90, 100, 40, 65, 41, 56, 76, 50, 65, 85, 35, 60, 65, 100, 20, 45, 55, 90, 30, 40, 50, 25, 30, 45, 90, 95, 120, 90, 115, 55, 85, 70, 95, 60, 95, 90, 90, 70, 90, 105, 120, 35, 45, 55, 40, 55, 70, 70, 100, 20, 35, 45, 90, 105, 15, 30, 45, 70, 60, 75, 100, 45, 70, 25, 50, 40, 70, 80, 95, 110, 70, 42, 67, 50, 75, 100, 140, 40, 55, 35, 45, 87, 76, 30, 35, 60, 25, 40, 50, 60, 90, 60, 85, 63, 68, 85, 115, 90, 105, 95, 105, 93, 85, 110, 80, 81, 60, 48, 55, 65, 130, 65, 40, 35, 55, 55, 80, 130, 30, 85, 100, 90, 50, 70, 80, 130, 100, 45, 60, 80, 65, 80, 100, 43, 58, 78, 20, 90, 50, 70, 55, 85, 30, 40, 130, 67, 67, 60, 15, 15, 20, 40, 70, 95, 35, 45, 55, 50, 40, 50, 30, 70, 50, 80, 110, 85, 30, 30, 95, 15, 35, 110, 65, 91, 30, 85, 48, 33, 85, 15, 40, 45, 85, 30, 30, 45, 85, 65, 5, 85, 115, 40, 55, 20, 30, 50, 50, 35, 65, 45, 75, 70, 70, 65, 95, 85, 40, 50, 60, 85, 75, 35, 70, 65, 95, 83, 100, 55, 115, 100, 85, 41, 51, 61, 110, 90, 100, 70, 95, 120, 45, 55, 80, 40, 50, 60, 35, 70, 60, 100, 20, 15, 65, 15, 65, 30, 50, 70, 30, 60, 80, 85, 125, 85, 65, 40, 50, 80, 65, 60, 35, 70, 30, 90, 100, 40, 160, 40, 28, 48, 68, 25, 50, 20, 30, 50, 70, 50, 50, 30, 40, 50, 60, 80, 65, 105, 95, 95, 85, 85, 65, 40, 55, 65, 95, 60, 60, 35, 40, 20, 60, 80, 60, 10, 70, 100, 35, 55, 50, 80, 90, 65, 70, 70, 60, 60, 35, 55, 55, 75, 23, 43, 75, 45, 80, 81, 70, 40, 45, 65, 25, 25, 51, 65, 75, 23, 50, 80, 25, 45, 65, 32, 52, 52, 55, 97, 50, 50, 100, 30, 50, 70, 50, 50, 50, 110, 110, 90, 90, 95, 100, 150, 150, 90, 180, 31, 36, 56, 61, 81, 108, 40, 50, 60, 60, 80, 100, 31, 71, 25, 65, 45, 60, 70, 55, 90, 58, 58, 30, 30, 36, 36, 36, 36, 66, 70, 40, 95, 85, 115, 35, 85, 34, 39, 115, 70, 80, 85, 105, 105, 71, 85, 112, 45, 74, 84, 23, 33, 10, 60, 30, 91, 35, 42, 82, 102, 5, 60, 90, 32, 47, 65, 95, 50, 85, 46, 66, 91, 50, 40, 60, 125, 60, 50, 40, 50, 95, 83, 80, 95, 95, 65, 95, 80, 90, 80, 40, 45, 110, 91, 86, 86, 86, 86, 86, 95, 80, 115, 90, 100, 77, 100, 90, 90, 85, 80, 100, 125, 100, 127, 120]
    for i in range(len(Species_List)):
        if Species == Species_List[i]:
            Base = [HP_List[i], Atk_List[i], Def_List[i], Spa_List[i], Spd_List[i], Spe_List[i]]
    Nature_List = ["Hardy", "Lonely", "Brave", "Adamant", "Naughty", "Bold", "Docile", "Relaxed", "Impish", "Lax", "Timid", "Hasty", "Serious", "Jolly", "Naive", "Modest", "Mild", "Quiet", "Bashful", "Rash", "Calm", "Gentle", "Sassy", "Careful", "Quirky"]
    Nature_Atk = [0, 11, 11, 11, 11, 9, 0, 0, 0, 0, 9, 0, 0, 0, 0, 9, 0, 0, 0, 0, 9, 0, 0, 0, 0]
    Nature_Def = [0, 9, 0, 0, 0, 11, 0, 11, 11, 11, 0, 9, 0, 0, 0, 0, 9, 0, 0, 0, 0, 9, 0, 0, 0]
    Nature_Spa = [0, 0, 0, 9, 0, 0, 0, 0, 9, 0, 0, 0, 0, 9, 0, 11, 11, 11, 0, 11, 0, 0, 0, 9, 0]
    Nature_Spd = [0, 0, 0, 0, 9, 0, 0, 0, 0, 9, 0, 0, 0, 0, 9, 0, 0, 0, 0, 9, 11, 11, 11, 11, 0]
    Nature_Spe = [0, 0, 9, 0, 0, 0, 0, 9, 0, 0, 11, 11, 0, 11, 11, 0, 0, 9, 0, 0, 0, 0, 9, 0, 0]
    for i in range(len(Nature_List)):
        if Nature == Nature_List[i]:  
            Nature_S = [Nature_Atk[i],Nature_Def[i],Nature_Spa[i],Nature_Spd[i],Nature_Spe[i]]
    for i in range(len(Nature_List)):
        if Nature == Nature_List[i]:  
            Nature_S = [Nature_Atk[i],Nature_Def[i],Nature_Spa[i],Nature_Spd[i],Nature_Spe[i]]
    V_Max = []
    V_Min = []
    mini = 94
    maxi = 0
    for v in range(95):
        if Stats[0] == ((((2*Base[0] + v) * Level) // 100) + Level + 10):
            mini = min(mini,v)
            maxi = max(maxi,v)
    V_Max.append(maxi)
    V_Min.append(mini)

    for s in range(1,6):
        mini = 94
        maxi = 0
        for v in range(95):
            if Nature_S[s-1] == 0:    
                if Stats[s] == ((((2*Base[s] + v) * Level) // 100) + 5):
                    mini = min(mini,v)
                    maxi = max(maxi,v)                    
            else:
                if Stats[s] == ((((((2*Base[s] + v) * Level) // 100) + 5) * Nature_S[s-1]) // 10):
                    mini = min(mini,v)
                    maxi = max(maxi,v)
        V_Max.append(maxi)
        V_Min.append(mini)
    print(V_Max,V_Min)
    Min_IVs = [0,0,0,0,0,0]
    Max_IVs = [31,31,31,31,31,31]
    Best_IVs = [0,0,0,0,0,0]
    Characteristic = input("Characteristic, leave blank if unknown: ")
    Characteristic = Characteristic.lower()
    Know_Char = 0
    Char_Stat = 7
    if Characteristic != "":
        Know_Char = 1
        Char_txts = ["loves to eat", "often dozes off", "often scatters things", "scatters things often", "likes to relax", "proud of its power", "likes to thrash about", "a little quick tempered", "likes to fight", "quick tempered", "sturdy body", "capable of taking hits", "highly persistent", "good endurance", "good perseverance", "highly curious", "mischievous", "thoroughly cunning", "often lost in thought", "very finicky", "strong willed", "somewhat vain", "strongly defiant", "hates to lose", "somewhat stubborn", "likes to run", "alert to sounds", "impetuous and silly", "somewhat of a clown", "quick to flee", "takes plenty of siestas", "nods off a lot"]
        Char_Stats = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 0, 0]
        Char_Mod = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 2, 3]
        for c in range(len(Char_txts)):
            if Characteristic == Char_txts[c]:
                Min_IVs[Char_Stats[c]] = Char_Mod[c]
                Best_IVs[Char_Stats[c]] = 1
                Char_Stat = Char_Stats[c]
                for m in range(6):
                    Max_IVs[m] = max((Char_Mod[c] + 30) % 32, (Char_Mod[c] + 25) % 32)
    print("MAX", Max_IVs,"MIN",Min_IVs)
    #IV Judge
    Know_Judge = 0
    if int(input("Do you have access to the IV Judge? 1 = Yes, 0 = No: ")) == 1:
        Know_Judge = 1
        BS_String = input("When talking to the IV judge, Which are your best IVs? Submit your answer in a format like this: 0/1/0/1/0/1, where 1 = Yes, 0 = No for the IVs in the order HP/ATK/DEF/SPA/SPD/SPE: ")
        Best_Stats = BS_String.split("/")
        for i in range(6):
            Best_Stats[i] = int(Best_Stats[i])
        Peak_IV = input("How good does the IV Judge say your best IV is? (Using Bulbapedia Stats Judge phrases): ")
        Peak_IV = Peak_IV.lower()
        Peak_IVs_txt = ["relatively good", "rather decent", "quite impressive", "very good", "good", "outstanding", "fantastic", "flawless", "can't be better", "cant be better", "can't be beat", "cant be beat"]
        Peak_IVs_min = [0, 0, 16, 16, 16, 26, 26, 31, 31, 31, 31, 31] 
        Peak_IVs_max = [15, 15, 25, 25, 25, 30, 30, 31, 31, 31, 31, 31]
        for p in range(len(Peak_IVs_txt)):
            if Peak_IV == Peak_IVs_txt[p]:
                for b in range(6):
                    if Best_Stats[b] == 1:
                        Min_IVs[b] = Peak_IVs_min[p] + (((Min_IVs[b] % 5) - (Peak_IVs_min[p] % 5)) % 5)*(b == Char_Stat)
                        Max_IVs[b] = Peak_IVs_max[p] - (((Peak_IVs_max[p] % 5) - (Max_IVs[b] % 5)) % 5)*(Know_Char)
                    else:
                        Max_IVs[b] = Peak_IVs_max[p] - (((Peak_IVs_max[p] % 5) - (Max_IVs[b] % 5)) % 5)*(Know_Char) -  (1-Best_Stats[b])
        print("MAX", Max_IVs,"MIN",Min_IVs)
        Sum_IV = input("How good does the IV Judge say your IV total is? (Using Bulbapedia Stats Judge phrases): ")
        Sum_IV = Sum_IV.lower()
        Sum_IVs_txt = ["average", "rather decent", "better-than-average", "better than average", "above-average", "above average", "quite impressive", "relatively superior", "outstanding"]
        Sum_IVs_min = [0, 0, 91, 91, 91, 91, 121, 121, 151]
        Sum_IVs_max = [90, 90, 120, 120, 120, 120, 150, 150, 186]
        for s in range(len(Sum_IVs_txt)):
            if Sum_IV == Sum_IVs_txt[s]:
                Sum_IV_Min = Sum_IVs_min[s]
                Sum_IV_Max = Sum_IVs_max[s]
# V_Min / Max to IVs
    print("MAX", Max_IVs,"MIN",Min_IVs)
    for o in range(6):
        if V_Min[o] > 63:
            Min_IVs[o] = max(V_Min[o] - 63, Min_IVs[o], 0)
            Max_IVs[o] = min(Max_IVs[o], 31)
        else:
            Min_IVs[o] = max(Min_IVs[o], 0)
            Max_IVs[o] = min(V_Max[o],Max_IVs[o], 31)
    print("MAX", Max_IVs,"MIN",Min_IVs)
    Know_Hidden_Power = 0
    if int(input("able to find hidden power type? 1 = Yes, 0 = No: ")) == 1:
        Know_Hidden_Power = 1
        Hidden_Power_Type = input("Hidden Power Type: ")
        Hidden_Power_Type = Hidden_Power_Type.lower()
        Hidden_Power_Types_txt = ["fighting", "flying", "poison", "ground", "rock", "bug", "ghost", "steel", "fire", "water", "grass", "electric", "psychic", "ice", "dragon", "dark"]
        Hidden_Power_all_bitfields = []         
        for h in range(len(Hidden_Power_Types_txt)):
            if Hidden_Power_Type == Hidden_Power_Types_txt[h]:
                for H in range(64):
                    if H * 5 // 21 == h:
                        Hidden_Power_all_bitfields.append(H)
        Hidden_Power_XO = []
        Hidden_Power_bitfields = []
        Wack_IV_order = [0, 1, 2, 5, 3, 4]
        for i in range(6):
            if Min_IVs[Wack_IV_order[i]] == Max_IVs[Wack_IV_order[i]]:
                for j in range(len(Hidden_Power_all_bitfields)):
                    if (Min_IVs[Wack_IV_order[i]] & 1) == ((Hidden_Power_all_bitfields[j] >> i) & 1):
                        Hidden_Power_bitfields.append(Hidden_Power_all_bitfields[j])

        for y in range(6):
            Unique = []
            for f in range(len(Hidden_Power_bitfields)):
                Unique.append((Hidden_Power_bitfields[f] >> y) & 1)
            Unique1 = set(Unique)
            if len(Unique1) == 1:
                Hidden_Power_XO.append(Unique[0])
            else:
                Hidden_Power_XO.append(2)                   
        # HP, ATK, DEF, SPA, SPE, SPD
        for o in range(6):
                if (Min_IVs[Wack_IV_order[o]] & 1 != ((Hidden_Power_XO[o]) & 1)) and (Hidden_Power_XO[o] < 2):
                    Min_IVs[Wack_IV_order[o]] = (Min_IVs[Wack_IV_order[o]] + 1 + 4*(Best_IVs[Wack_IV_order[o]] or Best_Stats[Wack_IV_order[o]]))
                if (Max_IVs[Wack_IV_order[o]] & 1 != ((Hidden_Power_XO[o]) & 1)) and (Hidden_Power_XO[o] < 2):
                    Max_IVs[Wack_IV_order[o]] = (Max_IVs[Wack_IV_order[o]] - 1 - 4*(Best_IVs[Wack_IV_order[o]] or Best_Stats[Wack_IV_order[o]]))
    print(Min_IVs, Max_IVs)
    Wack_HP_Order = [0,1,2,4,5,3]
    if Know_Judge: 
        for i in range(6):
            # Check if a Min_IV and 5 Max_IVs is above the Minimum IV total.
            if sum(Max_IVs[0:i]+Max_IVs[i+1:6],Min_IVs[i]) < Sum_IV_Min:
                # If not, raise that minimum.
                Temp = Sum_IV_Min - sum(Max_IVs[0:i]+Max_IVs[i+1:6])
                if i == Char_Stat:
                    if Know_Hidden_Power == 1:
                        if Hidden_Power_XO[Wack_HP_Order[i]] < 2: 
                            Min_IVs[i] = Temp + (((Min_IVs[i] % 10) - (Temp % 10)) % 10)        
                        else:
                            Min_IVs[i] = Temp + (((Min_IVs[i] % 5) - (Temp % 5)) % 5)
                    else:
                        Min_IVs[i] = Temp + (((Min_IVs[i] % 5) - (Temp % 5)) % 5)
                elif Know_Hidden_Power == 1:
                    if Hidden_Power_XO[Wack_HP_Order[i]] < 2:
                        Min_IVs[i] = Temp + (((Min_IVs[i] % 2) - (Temp % 2)) % 2)
                    else:
                        Min_IVs[i] = Temp
                else:
                    Min_IVs[i] = Temp
            # Check if a Max_IV and 5 Min_IVs is below the Maximum IV total.
        for i in range(6):
            if sum(Min_IVs[0:i]+Min_IVs[i+1:6],Max_IVs[i]) > Sum_IV_Max:
                # If not, lower that maximum.
                Temp = Sum_IV_Max - sum(Min_IVs[0:i]+Min_IVs[i+1:6])
                if i == Char_Stat:
                    if Know_Hidden_Power == 1: 
                        if Hidden_Power_XO[Wack_HP_Order[i]] < 2:        
                            Max_IVs[i] = Temp - (((Max_IVs[i] % 10) - (Temp % 10) % 10))
                        else:
                            Max_IVs[i] = Temp - (((Max_IVs[i] % 5) - (Temp % 5) % 5))
                    else:
                        Max_IVs[i] = Temp - (((Max_IVs[i] % 5) - (Temp % 5) % 5))
                elif Know_Hidden_Power == 1:
                    if Hidden_Power_XO[Wack_HP_Order[i]] < 2:
                        Temp = Temp - ((Max_IVs[i] % 2) - (Temp % 2) % 2) 
                        Max_IVs[i] = Max_IVs[i] - (Max_IVs[Char_Stat] < Temp)
                    else:
                        Max_IVs[i] = Temp
                else:
                    Max_IVs[i] = Temp
    print(Min_IVs, Max_IVs)
    try:
        Effort_Ribbon = int(input("Qualifies for Effort Ribbon? Yes = 1, No = 0, leave blank if unknown: "))
    except:
        Effort_Ribbon = ""
    Min_EVs = []
    Max_EVs = []
    
    # Convert IVs to EVs using V_Max and V_Min.
    for i in range(6):
        Min_EVs.append(max((V_Min[i] - Max_IVs[i])*4, 0))
        Max_EVs.append(min(max(V_Max[i] - Min_IVs[i],0)*4 + 3, 255))
    print(Max_EVs,Min_EVs)
    # How much info can we squeeze out of the EVs using Vitamins and the Effort Ribbon? Too much for me to keep straight lmao
    print("\nThis next step will require you to buy/use up to 10 vitamins at a time, but you will be able to reset to before you purchased them afterward.")
    # If the player cannot buy more than n vitamins, we want to know that before we start calcs. This assumes the player is able to buy vitamins, which might be a bad assumption.
    Afford_Vitamin = int(input("How many of a single type of vitamin can you afford, if you sell your items? Please check, and input a number higher than 10 if possible: ")) 
    # Vitamins fail after their individual EV is at or above 100. They will also fail if the pokemon has Max EVs.
    print("For the next step, attempt to feed as many of an EV-boosting of vitamin as you can to your pokemon, and take note of how many it took for the mon to refuse more." + (Effort_Ribbon==0)*" Then, check the effort ribbon again." + " Once you do, reset the game and attempt for the other 5 vitamin types.")
    Vitamin_String = input("With the EVs it currently has, how many of each type of vitamin will your pokemon accept (resetting in between types)? \nSubmit your answer if a format like this, \"1/2/3/4/5/6\" \nFor the vitamins HP-Up/Protein/Iron/Calcium/Zinc/Carbos: ")
    Vitamins = Vitamin_String.split("/")
    for i in range(6):
        Vitamins[i] = int(Vitamins[i])
    if (Effort_Ribbon==0):
        # Effort_Ribbon NOT obtained, therefore Effort Judge available. 
        # Use Effort_Ribbon to determine if the individual cap triggered, or if the pokemon hit 510 total EVs. 
        Effort_Vitamin_String = input("Which of the vitamins caused your pokemon to receive the Effort Ribbon?\nSubmit your answer in a format like this, \"0/1/0/1/0/1\", where 1 = Yes, 0 = No. \nFor the vitamins HP-Up/Protein/Iron/Calcium/Zinc/Carbos: ") 
        Effort_Vitamins = Effort_Vitamin_String.split("/")
        for i in range(6):
            Effort_Vitamins[i] = int(Effort_Vitamins[i])
        print(Effort_Vitamins)
        if Effort_Vitamin_String != "0/0/0/0/0/0":
            # No need for Cross Vitamins if we already hit the global EV cap.
            for i in range(6):
                Cross_Vitamin = 0
                Cross_Vitamin = max(Vitamins[i]*Effort_Vitamins[i],Cross_Vitamin)
            
        else:
            # Can we hit the global EV cap?  
            Cross_Vitamin = input("Now attempt to feed your pokemon " + str(min(sum(Vitamins),Afford_Vitamin)) + " total vitamins. \nInput the number of total vitamins your pokemon would consume before refusing more. Then check the effort ribbon. \nLeave blank if it gobbled up every single vitamin you could buy and still doesn't qualify for the effort ribbon': ")
        
        if Cross_Vitamin == "":
            # We never hit the global EV cap, and therefore don't know how few total EVs the pokemon could have.
            Sum_EV_Min = 0
            Cross_Vitamin = min(sum(Vitamins),Afford_Vitamin)
        else:
            # We hit the global EV cap, and therefore know the pokemon must have at least this many EVs
            Sum_EV_Min = 510-int(Cross_Vitamin)*10
        # Keep in mind, a vitamin will provide less than 10 of an EV to not exceed the individual 100 EV cap. 
        # Worst-case scenario, this means each unique Vitamin type fed could give +1 once instead of +10.
        # This means our Max EV sum is slightly high in most cases, the logic to fix that is rarely necessary and stupidly complicated.
        Total = 0
        for i in range(6):
            Total = Total + (Vitamins[i]>0)
        Sum_EV_Max = 510-int(Cross_Vitamin)*10+9*Total
        Uncapped_Vitamins = []
        # Which EVs did we potentially not hit the Individual Cap for?
        # This could happen if the Global EV cap is hit first, or if the player can't afford enough vitamins
        for i in range(6):
            Uncapped_Vitamins.append((Effort_Vitamins[i] or 1*(Vitamins[i]>=Afford_Vitamin)))
    elif (Effort_Ribbon==""):
        # Effort_Ribbon status unknown, therefore Effort Judge NOT available
        # Therefore we always need to do Cross_Vitamins 
        Cross_Vitamin = input("Now attempt to feed your pokemon " + str(min(sum(Vitamins),Afford_Vitamin)) + " total vitamins of different types. \nInput the number of total vitamins your pokemon would consume before refusing more: ")
        Total = 0
        for i in range(6):
            Total = Total + (Vitamins[i]>0)
        if Cross_Vitamin == "":
            # Potentially didn't hit global EV cap. Safe assumption is that we didn't. 
            Sum_EV_Min = 0
            # Cross Vitamin isn't an int, therefore we use the max vitamins input
            Cross_Vitamin = min(sum(Vitamins),Afford_Vitamin)
        else:
            # We hit the global EV cap!
            Sum_EV_Min = 510-int(Cross_Vitamin)*10
        Sum_EV_Max = 510-int(Cross_Vitamin)*10+9*Total
        # Unless we hit a global cap with Cross Vitamins, we can only confirm we hit the individual EV cap for some of the EVs.
        # The highest Vitamin proves that any EV cap hit below it got hit.
        Uncapped_Vitamins = []
        # Python doesn't like it when I multiply lists by constants, or lists by lists...
        Vitamin_Max = Cross_Vitamin + 0
        for i in range(6):    
            Vitamin_Max = max(Vitamins[i],Vitamin_Max)
        for i in range(6):
            Uncapped_Vitamins.append((Vitamins[i]>=Vitamin_Max) or (Vitamins[i]>=Afford_Vitamin))
    for i in range(6):
        if Vitamins[i]==0:
            Max_EVs[i]= min(255,Max_EVs[i])
        else:
            Max_EVs[i] = min(109-Vitamins[i]*10,Max_EVs[i])
        if Uncapped_Vitamins[i] == 1:
            Min_EVs[i] = max(0,Min_EVs[i])
        else:
            Min_EVs[i] = max(100-Vitamins[i]*10,Min_EVs[i])
    if Effort_Ribbon != "":
        if Effort_Ribbon == 1:
            Sum_EV_Min = 510
            Sum_EV_Max = 510
        else:
            Sum_EV_Min = max(0,Sum_EV_Min)    
            Sum_EV_Max = min(510,Sum_EV_Max)

        print(Max_EVs, Min_EVs)
        for i in range(6):
            # Check if a Min_EV and 5 Max_EVs is above the Minimum EV total.
            if sum(Max_EVs[0:6],Min_EVs[i])-Max_EVs[i] < Sum_EV_Min:
                # If not, raise that minimum.
                Temp = Sum_EV_Min - sum(Max_EVs[0:6],-Max_EVs[i])
                Min_EVs[i] = max(Temp,0)
        print(Min_EVs)
            # Check if a Max_EV and 5 Min_EVs is below the Maximum EV total.
        for i in range(6):
            if sum(Min_EVs[0:6],Max_EVs[i])-Min_EVs[i] > Sum_EV_Max:
                # If not, raise that maximum.
                Temp = Sum_EV_Max - sum(Min_EVs[0:6],-Min_EVs[i])
                Max_EVs[i] = min(max(Temp,0),255)
        print(Max_EVs)
        for i in range(6):
            Temp = max(V_Min[i] - (Max_EVs[i]//4), Min_IVs[i], 0)
            if i == Char_Stat:
                if Know_Hidden_Power == 1:
                    if Hidden_Power_XO[Wack_HP_Order[i]] < 2: 
                        Min_IVs[i] = Temp + (((Min_IVs[i] % 10) - (Temp % 10)) % 10)        
                    else:
                        Min_IVs[i] = Temp + (((Min_IVs[i] % 5) - (Temp % 5)) % 5)
                else:
                    Min_IVs[i] = Temp + (((Min_IVs[i] % 5) - (Temp % 5)) % 5)
            elif Know_Hidden_Power == 1: 
                if Hidden_Power_XO[Wack_HP_Order[i]] < 2:
                    Min_IVs[i] = Temp + (((Min_IVs[i] % 2) - (Temp % 2)) % 2)
                else:
                    Min_IVs[i] = Temp
            else:
                Min_IVs[i] = Temp
                    
            Temp = min(max(V_Max[i] - (Min_EVs[i]//4),0), Max_IVs[i], 31)
            if Temp != Max_IVs[i]:
                if i == Char_Stat:
                    if Know_Hidden_Power == 1:
                        if Hidden_Power_XO[Wack_HP_Order[i]] < 2:        
                            Max_IVs[i] = Temp - (((Max_IVs[i] % 10) - (Temp % 10) % 10))
                        else:
                            Max_IVs[i] = Temp - (((Max_IVs[i] % 5) - (Temp % 5) % 5))    
                    else:
                        Max_IVs[i] = Temp - (((Max_IVs[i] % 5) - (Temp % 5) % 5))
                elif Know_Hidden_Power == 1:
                    if Hidden_Power_XO[Wack_HP_Order[i]] < 2:
                        Max_IVs[i] = Temp - ((Max_IVs[i] % 2) - (Temp % 2) % 2)
                    else:
                        Max_IVs[i] = Temp
                else:
                    Max_IVs[i] = Temp
    print(Max_EVs, Min_EVs)
    print("Max IVs:", Max_IVs, "Min IVs:", Min_IVs)


    
    
#Stats = [133, 99, 91, 117, 86, 119]
#Stats2TVs("Typhlosion", 45, "Bashful", Stats)
Stats = [int(input("HP Stat: ")),
         int(input("Atk Stat: ")),
         int(input("Def Stat: ")),
         int(input("Spa Stat: ")),
         int(input("SpD Stat: ")),
         int(input("Spe Stat: "))]
Stats2TVs(input("Species: "),
          int(input("Level: ")),
          input("Nature: "), Stats)