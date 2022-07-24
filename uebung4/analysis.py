import pandas as pd

results = pd.read_excel("./Results_Record_Linkage.xlsx")

dataset_names = ["clean", "little-dirty", "very-dirty"]
parameters = ["blocking_func", "comp_func", "classification_func", "sim_threshold"]

grouped_results = {}
for name in dataset_names:
    res = results.query(f"dataset == '{name}'").groupby(parameters, as_index=False).mean().sort_values("f_measure")
    grouped_results[name] = res
    print(f"{name}: \n\n{res}\n------------------------------------------------------")

# weight = 0.5
weight = 0.7
weight_cond = f"sim_threshold== {weight}"

blocking_func = "slkBlocking"
# blocking_func = "phoneticBlocking"
blocking_cond = f"blocking_func == '{blocking_func}'"

grouped_results2 = {}
for name in dataset_names:
    res = results\
        .query(f"dataset == '{name}'") \
        .query(f"{weight_cond}") \
        .query(f"{blocking_cond}") \
        .groupby(parameters, as_index=False).mean().sort_values("f_measure") \
        .filter(["comp_func", "classification_func", "f_measure"])
    grouped_results2[name] = res
    print(f"{name}: \n\n{res}\n------------------------------------------------------")

# -------------------------------------------------------------------------------------------

# Time Analysis

print("Blocking")
print(results.groupby(["dataset", "records", "blocking_func"], as_index=False).mean().filter(["dataset", "records", "blocking_func",
                                                                            "blocking_time"]).sort_values("blocking_time"))
print("\n\n")
print("Comparison")
print(results.groupby(["comp_func"], as_index=False).mean().filter(["comp_func",
                                                                              "comparison_time"]).sort_values("comparison_time"))
print("\n\n")
print("Classification")
print(results.groupby(["dataset", "records", "classification_func"], as_index=False).mean().filter(["dataset", "records",
                                                                                  "classification_func",
                                                                                  "classification_time"]).sort_values("classification_time"))
print("\n\n")

