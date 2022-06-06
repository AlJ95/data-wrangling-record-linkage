from blocking import simpleBlocking, phoneticBlocking, printBlockStatistics
from loadDataset import load_data_set

if __name__ == "__main__":
    # 2) a)
    rect_dict = {"r0001": ["christina"], "r0002": ["kirstyn"], "r0003": ["allyson"], "r0004": ["alisen"]}
    blk_attr_list = [0]

    codes = phoneticBlocking(rect_dict, blk_attr_list)
    print(f"Exercise 2a)\n"
          f"Results are: {codes}\n"
          f"For: {'; '.join([f'{rect}:{rect_dict[rect]}' for rect in rect_dict])}\n\n")

    # 2) b)
    # Last Name
    print("Solutions for last name:")
    attrA_list = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11]
    attrB_list = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11]
    blocking_attrA_list = [3, 4]
    blocking_attrB_list = [3, 4]
    recA_dict = load_data_set("../datasets/clean-A-1000.csv", 0, attrA_list, True)
    recB_dict = load_data_set("../datasets/little-dirty-A-1000.csv", 0, attrB_list, True)

    blockA_dict = simpleBlocking(recA_dict, blocking_attrA_list)
    blockB_dict = simpleBlocking(recB_dict, blocking_attrB_list)

    printBlockStatistics(blockA_dict, blockB_dict)
    print("---")

    blocking_attrA_list = [3]
    blocking_attrB_list = [3]
    blockA_dict = phoneticBlocking(recA_dict, blocking_attrA_list)
    blockB_dict = phoneticBlocking(recB_dict, blocking_attrB_list)

    printBlockStatistics(blockA_dict, blockB_dict)


    # First Name
    print("\n\nSolutions for first name")
    blocking_attrA_list = [1, 4]
    blocking_attrB_list = [1, 4]
    recA_dict = load_data_set("../datasets/clean-A-1000.csv", 0, attrA_list, True)
    recB_dict = load_data_set("../datasets/little-dirty-A-1000.csv", 0, attrB_list, True)

    blockA_dict = simpleBlocking(recA_dict, blocking_attrA_list)
    blockB_dict = simpleBlocking(recB_dict, blocking_attrB_list)

    printBlockStatistics(blockA_dict, blockB_dict)
    print("---")

    blocking_attrA_list = [1]
    blocking_attrB_list = [1]
    blockA_dict = phoneticBlocking(recA_dict, blocking_attrA_list)
    blockB_dict = phoneticBlocking(recB_dict, blocking_attrB_list)

    printBlockStatistics(blockA_dict, blockB_dict)

"""
2a)
christina:  C623
kirstyn:    K623
allyson:    A425
alisen:     A425


2b)

                                **Simple Blocking**

Kurze Erklärung:
    Für Simple Blocking nehme ich zusätzlich zum namen den gender, da dieser selten falsche Einträge liefert und 
    sich auch nur in sehr seltenen Fällen ändert. (Wichtig da einfaches Zusammenfügen keine Schreibfehler behandelt)

    Based on last_name & gender
    
Dataset clean-A-1000.csv number of blocks generated: 785
    Minimum block size: 1
    Average block size: 1.27
    Maximum block size: 10

Dataset little-dirty-A-1000.csv number of blocks generated: 865
    Minimum block size: 1
    Average block size: 1.16
    Maximum block size: 16



    Based on first_name & gender
    
Dataset clean-A-1000.csv number of blocks generated: 562
    Minimum block size: 1
    Average block size: 1.78
    Maximum block size: 26

Dataset little-dirty-A-1000.csv number of blocks generated: 695
    Minimum block size: 1
    Average block size: 1.44
    Maximum block size: 14

Ergebnis:
Beide Attribute listen liefern akzeptable Resultate.

Die Blockgrößen mit first_name sind größer als die Blockgrößen mit last_name. 
Dies ist unter anderem der Tatsache geschuldet, dass gewisse Vornamen oftmals mit nur einem Geschlecht aufkommen
wie zum Beispiel ("John", "m") oder ("Victoria", "f")
Durchschnittliche Blockgrößen von 1.16 und 1.27 sind außerdem sehr klein und laufen Gefahr
einige Matches durch falsche Blockzuweisung zu verpassen.

first_name + gender wäre meiner Meinung nach zu präferieren.




                                **Phonetic Blocking**
                                
Erklärung: Attribute last_name und first_name wurden ausgewählt. Die Gründe werden weiter unten in 2c) beschrieben. 

    Based on last_name
    
Dataset clean-A-1000.csv number of blocks generated: 550
    Minimum block size: 1
    Average block size: 1.82
    Maximum block size: 12

Dataset little-dirty-A-1000.csv number of blocks generated: 607
    Minimum block size: 1
    Average block size: 1.65
    Maximum block size: 17


    Based on first_name

Dataset clean-A-1000.csv number of blocks generated: 346
    Minimum block size: 1
    Average block size: 2.89
    Maximum block size: 37

Dataset little-dirty-A-1000.csv number of blocks generated: 401
    Minimum block size: 1
    Average block size: 2.49
    Maximum block size: 25

Auswertung:
Die durchschnittlichen Blockgrößen sind größer als die Blockgrößen mit SimpleBlocking. 
Dies hat zwei primäre Gründe:
    - im SimpleBlocking wurde zusätzlich das Gender benutzt. Das würde ich als geringen Faktor einstufen.
    - im phonetischen Blocking wird versucht ähnlich klingende Namen zusammenzuführen, damit die Einträge
        miteinander verglichen werden können. 
        Daher werden auch Rechtschreibfehler und versch. Schreibweisen von Namen oftmals im selben Block landen. 

Auch hier sind die Blockgrößen vom sauberen Datensatz größer als die Blockgrößen vom unsauberen Datensatz.

                                        AVG block size
Last Name: 
                    clean                   little-dirty                Difference in %
simple              1.27                    1.16                        9.48 %              
phonetic            1.82                    1.65                        10.3 %

First Name: 
                    clean                   little-dirty                Difference in %
simple              1.78                    1.44                        23.6 %
phonetic            2.89                    2.49                        16.1 %

Hier kann man noch sehr gut erkennen, dass wir mithilfe von phonetischen Blocking den Effekt von unsauberen Daten 
im Attribute first_name reduzieren konnten. 
Die sauberen Daten hatten beim einfachen Blockingverfahren ca. 23% größere Blöcke als die unsauberen, 
während die phonetischen Blöcke nur ca. 16% größer waren. 
Damit kann man behaupten, dass unsaubere Daten besser mit dem phonetischen Verfahren in Blöcken zusammengeführt werden
können, als mit dem einfachen Blockverfahren.

Für das Attribut last_name kann lässt sich diese Behauptung allerdings nicht mit den Daten belegen.


2c)
    Suitability for Phonetic Blocking
     0: rec_id
     1: first_name        - suitable
     2: middle_name       - unsuitable (Higher risk of missing values)
     3: last_name         - suitable (lower risk for change over time)
     4: gender            - unsuitable for phonetic
     5: current_age       - unsuitable in general (changes over time)
     6: birth_date        - unsuitable for phonetic
     7: street_address    - unsuitable for phonetic (also: potential high risk of change over time)
     8: suburb            - unsuitable for phonetic (also: potential high risk of change over time)
     9: postcode          - unsuitable for phonetic (also: potential high risk of change over time)
    10: state             - unsuitable for phonetic (also: potential high risk of change over time)
    11: phone             - unsuitable for phonetic (also: potential high risk of change over time)
    12: email             - unsuitable for phonetic (also: potential high risk of change over time)

    Logische Betrachtung der Attribute:
    Wie oben in der Tabelle zu sehen:
    
    Für phonetisches Blocking eignen sich prinzipiell die folgenden Attribute:
    first_name, middle_name, last_name und email, 
    da man in diesen Attributen falsch geschriebene Einträge dennoch zusammenführen kann. 
    
    Suburb, street_address und state habe ich ausgelassen, da diese Einträge
    standardisiert sein sollten. Falls die Data Exploration etwas anderes hervorbringt, sind diese allerdings dennoch
    keine guten Variante, da sie sich häufiger ändern können.
    
    middle_name hat ein erhöhtes Risiko, dass es einfach weggelassen wurde und die email kann sich schnell ändern.

    Daher sind die besten Kandidaten first_name und last_name, wobei auch last_name sich nach einer Hochzeit ändern 
    kann.






                                    ***Output***
                                    
Run phonetic blocking:
  List of blocking key attributes: [0]
  Number of records to be blocked: 4

Exercise 2a)
Results are: {'C623': ['r0001'], 'K623': ['r0002'], 'A425': ['r0003', 'r0004']}
For: r0001:['christina']; r0002:['kirstyn']; r0003:['allyson']; r0004:['alisen']


Solutions for last name:

Load data set from file: ../datasets/clean-A-1000.csv
  Header line: ['rec_id', 'first_name', 'middle_name', 'last_name', 'gender', 'current_age', 'birth_date', 'street_address', 'suburb', 'postcode', 'state', 'phone', 'email']
   [... Truncated ... ]
    phone

Load data set from file: ../datasets/little-dirty-A-1000.csv
  Header line: ['rec_id', 'first_name', 'middle_name', 'last_name', 'gender', 'current_age', 'birth_date', 'street_address', 'suburb', 'postcode', 'state', 'phone', 'email']
   [... Truncated ... ]
    phone

Run simple blocking:
  List of blocking key attributes: [3]
  Number of records to be blocked: 1000

Run simple blocking:
  List of blocking key attributes: [3]
  Number of records to be blocked: 1000

Statistics of the generated blocks:
Dataset clean-A-1000.csv number of blocks generated: 785
    Minimum block size: 1
    Average block size: 1.27
    Maximum block size: 10

Dataset little-dirty-A-1000.csv number of blocks generated: 865
    Minimum block size: 1
    Average block size: 1.16
    Maximum block size: 16

---
Run phonetic blocking:
  List of blocking key attributes: [3]
  Number of records to be blocked: 1000

Run phonetic blocking:
  List of blocking key attributes: [3]
  Number of records to be blocked: 1000

Statistics of the generated blocks:
Dataset clean-A-1000.csv number of blocks generated: 550
    Minimum block size: 1
    Average block size: 1.82
    Maximum block size: 12

Dataset little-dirty-A-1000.csv number of blocks generated: 607
    Minimum block size: 1
    Average block size: 1.65
    Maximum block size: 17



Solutions for first name
Load data set from file: ../datasets/clean-A-1000.csv
  Header line: ['rec_id', 'first_name', 'middle_name', 'last_name', 'gender', 'current_age', 'birth_date', 'street_address', 'suburb', 'postcode', 'state', 'phone', 'email']
 [... Truncated ... ]
    phone

Load data set from file: ../datasets/little-dirty-A-1000.csv
  Header line: ['rec_id', 'first_name', 'middle_name', 'last_name', 'gender', 'current_age', 'birth_date', 'street_address', 'suburb', 'postcode', 'state', 'phone', 'email']
 [... Truncated ... ]
    phone

Run simple blocking:
  List of blocking key attributes: [1]
  Number of records to be blocked: 1000

Run simple blocking:
  List of blocking key attributes: [1]
  Number of records to be blocked: 1000

Statistics of the generated blocks:
Dataset clean-A-1000.csv number of blocks generated: 562
    Minimum block size: 1
    Average block size: 1.78
    Maximum block size: 26

Dataset little-dirty-A-1000.csv number of blocks generated: 695
    Minimum block size: 1
    Average block size: 1.44
    Maximum block size: 14

---
Run phonetic blocking:
  List of blocking key attributes: [1]
  Number of records to be blocked: 1000

Run phonetic blocking:
  List of blocking key attributes: [1]
  Number of records to be blocked: 1000

Statistics of the generated blocks:
Dataset clean-A-1000.csv number of blocks generated: 346
    Minimum block size: 1
    Average block size: 2.89
    Maximum block size: 37

Dataset little-dirty-A-1000.csv number of blocks generated: 401
    Minimum block size: 1
    Average block size: 2.49
    Maximum block size: 25
"""

