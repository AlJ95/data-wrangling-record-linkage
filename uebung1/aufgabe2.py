from blocking import simpleBlocking, phoneticBlocking, printBlockStatistics
from loadDataset import load_data_set

if __name__ == "__main__":
    # 2) a)
    rect_dict = {"r0001": ["christina"], "r0002": ["kirstyn"], "r0003": ["allyson"], "r0004": ["alisen"]}
    blk_attr_list = [0]

    codes = phoneticBlocking(rect_dict, blk_attr_list)
    print(f"Results are: {codes}")

    # 2) b)
    attrA_list = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11]
    attrB_list = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11]
    blocking_attrA_list = [3, 4]
    blocking_attrB_list = [3, 4]
    recA_dict = load_data_set("../datasets/clean-A-1000.csv", 0, attrA_list, True)
    recB_dict = load_data_set("../datasets/little-dirty-A-1000.csv", 0, attrB_list, True)

    blockA_dict = phoneticBlocking(recA_dict, blocking_attrA_list)
    blockB_dict = phoneticBlocking(recB_dict, blocking_attrB_list)

    printBlockStatistics(blockA_dict, blockB_dict)
