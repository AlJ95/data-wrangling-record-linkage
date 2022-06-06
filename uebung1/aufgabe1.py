import re

# Soundex Cheat Sheet
rm_aeiouyhw = re.compile(r"[aeiouyhw]")
rp_bfpv = re.compile(r"[bfpv]+")
rp_cgjkqsxz = re.compile(r"[cgjkqsxz]+")
rp_dt = re.compile(r"[dt]+")
rp_l = re.compile(r"[l]+")
rp_mn = re.compile(r"[mn]+")
rp_r = re.compile(r"[r]+")


def soundex(attr_val):
    """
    Implementation of the soundex algorithm
    """
    print(f"\n\nTransform {attr_val} into Soundex-Code:\n")

    # 1. Take the first letter
    rec_bkv = attr_val[0].upper()
    print(f"1) {rec_bkv}")

    # 2. remove a, e ,i , o, u, y, h, w
    val = rm_aeiouyhw.sub('', attr_val[1:])
    print(f"2) {rec_bkv}{val}")

    # 3. replace group of letters with their numbers
    val = rp_bfpv.sub("1", val)
    val = rp_cgjkqsxz.sub("2", val)
    val = rp_dt.sub("3", val)
    val = rp_l.sub("4", val)
    val = rp_mn.sub("5", val)
    val = rp_r.sub("6", val)
    print(f"3) {rec_bkv}{val}")

    rec_bkv = f"{rec_bkv}{val}000"[:4]
    print(f"4) {rec_bkv}")

    return rec_bkv


if __name__ == "__main__":
    attr_values = ["arnold", "schwarzenegger", "jan", "albrecht"]
    for value in attr_values:
        soundex(value)

# Output:
#
# Transform arnold into Soundex-Code:
# 1) A
# 2) Arnld
# 3) A6543
# 4) A654
# Transform schwarzenegger into Soundex-Code:
# 1) S
# 2) Scrznggr
# 3) S262526
# 4) S262
# Transform jan into Soundex-Code:
# 1) J
# 2) Jn
# 3) J5
# 4) J500
# Transform albrecht into Soundex-Code:
# 1) A
# 2) Albrct
# 3) A41623
# 4) A416
