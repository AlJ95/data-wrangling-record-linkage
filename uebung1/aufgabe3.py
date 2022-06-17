from blocking import slkBlocking, printBlockStatistics
from loadDataset import load_data_set

if __name__ == "__main__":
    rec_dict = {
        "r0001": ["john", "johnson", "19/05/1967", ""],
        "r0002": ["maria", "meier", "11/11/1911", ""],
        "r0003": ["al", "hu", "01/12/2012", ""],
        "r0004": ["yi", "zu", "01/10/2010", ""]}

    # 3)
    # arguments
    fam_name_attr_ind = 1
    giv_name_attr_ind = 0
    dob_attr_ind = 2
    gender_attr_ind = 3

    codes = slkBlocking(rec_dict, fam_name_attr_ind,
                        giv_name_attr_ind, dob_attr_ind,
                        gender_attr_ind)

    print(f"Exercise 3a)\n"
          f"Results are: {codes}\n")

    for code in codes:
        print(f"{code}: {codes[code]}")

    print("\nFor:")
    for rect in rec_dict:
        print(f'{rect}:{rec_dict[rect]}')

    print("\n\n\n")

    # 3 a)
    # arguments
    recA_dict = load_data_set("../datasets/clean-A-1000.csv", 0, [1, 2, 3, 4, 6, 7, 8, 9, 10, 11], True)
    recB_dict = load_data_set("../datasets/little-dirty-A-1000.csv", 0, [1, 2, 3, 4, 6, 7, 8, 9, 10, 11], True)

    fam_name_attr_ind = 3
    giv_name_attr_ind = 1
    dob_attr_ind = 6
    gender_attr_ind = 4

    blockA_dict = slkBlocking(recA_dict, fam_name_attr_ind,
                              giv_name_attr_ind, dob_attr_ind,
                              gender_attr_ind)

    blockB_dict = slkBlocking(recB_dict, fam_name_attr_ind,
                              giv_name_attr_ind, dob_attr_ind,
                              gender_attr_ind)

    printBlockStatistics(blockA_dict, blockB_dict)

"""
Run SLK-581 blocking:
  Number of records to be blocked: 4
  
Exercise 3)

    ohsoh190519679: ['r0001']
    eirar111119119: ['r0002']
    u22l2011220129: ['r0003']
    u22i2011020109: ['r0004']

    For:
    r0001:['john', 'johnson', '19/05/1967', '']
    r0002:['maria', 'meier', '11/11/1911', '']
    r0003:['al', 'hu', '01/12/2012', '']
    r0004:['yi', 'zu', '01/10/2010', '']
    
Exercise 3 a)

    Dataset clean-A-1000 number of blocks generated: 1000
        Minimum block size: 1
        Average block size: 1.00
        Maximum block size: 1

    Dataset little-dirty-A-1000 number of blocks generated: 1000
        Minimum block size: 1
        Average block size: 1.00
        Maximum block size: 1


Der Algorithmus hat nur Blöcke gebildet, welche die Größe 1 haben. 
Das kann verschiedene Ursachen haben: 

1) Wie bereits in der Vorlesung erwähnt, eignet sich der SLK Blocking Algorithmus nur für wirklich saubere Daten. 
2) Die Datensätze von 1000 records sind recht klein.
3) Gefundene gemeinsame Keys werden als die gleiche Person angesehen. Es kann also durchaus sein, dass die Datensätze 
    frei von Duplikaten sind.
    
Exercise 3 b)

Wie in der folgenden Quelle zu sehen ist, 
https://www.researchgate.net/publication/41485773_Empirical_aspects_of_record_linkage_across_multiple_data_sets_using_statistical_linkage_keys_The_experience_of_the_PIAC_cohort_study
wurde viel getestet, welche Attribute bzw. Teile von Attributen benutzt werden sollten, damit der Algorithmus 
bestmöglich funktioniert.
Dies müsste prinzipiell auch für den deutschen Raum gemacht werden, da unterschiedliche Konventionen für Vor- und 
Nachnamen den Algorithmus beeinträchtigen können.

Eine pauschale Antwort ist daher nur schwer möglich. Also lässt sich nur auf Spezialfälle wie das ä, ö, ü und ß 
verweisen, welche eventuell gesondert behandelt werden könnten. Durch die Globalisierung wird es allerdings
auch notwendig á, é, â, è, ô, ... zu behandeln. Daher wäre auch dies keine dauerhafte Möglichkeit.  
    
            **Output**
    
Load data set from file: ../datasets/clean-A-1000.csv
  Header line: ['rec_id', 'first_name', 'middle_name', 'last_name', 'gender', 'current_age', 'birth_date', 'street_address', 'suburb', 'postcode', 'state', 'phone', 'email']
   [... Truncated ... ]
    phone

Load data set from file: ../datasets/little-dirty-A-1000.csv
  Header line: ['rec_id', 'first_name', 'middle_name', 'last_name', 'gender', 'current_age', 'birth_date', 'street_address', 'suburb', 'postcode', 'state', 'phone', 'email']
   [... Truncated ... ]
    phone

Run SLK-581 blocking:
  Number of records to be blocked: 1000

Run SLK-581 blocking:
  Number of records to be blocked: 1000

Statistics of the generated blocks:
Dataset A number of blocks generated: 1000
    Minimum block size: 1
    Average block size: 1.00
    Maximum block size: 1

Dataset B number of blocks generated: 1000
    Minimum block size: 1
    Average block size: 1.00
    Maximum block size: 1
"""
