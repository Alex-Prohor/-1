disk = 1.44
Kb_disk = disk * 1024
b_disk = Kb_disk * 1024

stranic = 100
Str_stranic = 50
Koll_sim_str = 25
Ves_simvola = 4

ves_str = Ves_simvola * Koll_sim_str
ves_stranic = ves_str * Str_stranic
ves_knigi = ves_stranic * stranic

koll_knig = b_disk  / ves_knigi

print("Количество книг, помещающихся на дискету:", round(koll_knig) )
