from comparison import *

inps = [{"val1": "jones", "val2": "johnson"},
        {"val1": "michelle", "val2": "michael"},
        {"val1": "shackleford", "val2": "shackelford"},
        {"val1": "jan", "val2": "naj"},
        {"val1": "18.02.1995", "val2": "19.02.1995"},
        {"val1": "17.03.1994", "val2": "18.04.1993"},
        {"val1": "02315", "val2": "12315"},
        {"val1": "02315", "val2": "02314"},
        {"val1": "0152370231216", "val2": "0152370221216"},
        {"val1": "0152370231216", "val2": "0152271224216"},]

print("\n1a)")
for i, inp in enumerate(inps):
    print(f"{i + 1}. {inp['val1']}/{inp['val2']}: {jaccard_comp(**inp)}")

print("\n1b)")
for i, inp in enumerate(inps):
    print(f"{i + 1}. {inp['val1']}/{inp['val2']}: {dice_comp(**inp)}")

print("\n1c)")
for i, inp in enumerate(inps):
    print(f"{i + 1}. {inp['val1']}/{inp['val2']}: {bag_dist_sim_comp(**inp)}")

print("\n2a)")
for i, inp in enumerate(inps):
    print(f"{i + 1}. {inp['val1']}/{inp['val2']}: {jaro_winkler_comp(**inp)}")

print("\n2b)")
for i, inp in enumerate(inps):
    print(f"{i + 1}. {inp['val1']}/{inp['val2']}: {edit_dist_sim_comp(**inp)}")