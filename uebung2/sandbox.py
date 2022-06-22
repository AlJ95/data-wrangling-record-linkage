from comparison import *

inps = [{"val1": "jones", "val2": "johnson"},
        {"val1": "michelle", "val2": "michael"},
        {"val1": "shackleford", "val2": "shackelford"},
        {"val1": "jan", "val2": "naj"}]

print("1a)")
for i, inp in enumerate(inps):
    print(f"{i + 1}. {inp['val1']}/{inp['val2']}: {jaccard_comp(**inp)}")

print("1b)")
for i, inp in enumerate(inps):
    print(f"{i + 1}. {inp['val1']}/{inp['val2']}: {dice_comp(**inp)}")

print("1c)")
for i, inp in enumerate(inps):
    print(f"{i + 1}. {inp['val1']}/{inp['val2']}: {bag_dist_sim_comp(**inp)}")

print("2a)")
for i, inp in enumerate(inps):
    print(f"{i + 1}. {inp['val1']}/{inp['val2']}: {jaro_winkler_comp(**inp)}")

print("2b)")
for i, inp in enumerate(inps):
    print(f"{i + 1}. {inp['val1']}/{inp['val2']}: {edit_dist_sim_comp(**inp)}")