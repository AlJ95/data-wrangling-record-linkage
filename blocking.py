""" Module with functionalities for blocking based on a dictionary of records,
    where a blocking function must return a dictionary with block identifiers
    as keys and values being sets or lists of record identifiers in that block.
"""

import re

# =============================================================================

def noBlocking(rec_dict):
    """A function which does no blocking but simply puts all records from the
       given dictionary into one block.

       Parameter Description:
         rec_dict : Dictionary that holds the record identifiers as keys and
                    corresponding list of record values
    """

    print("Run 'no' blocking:")
    print('  Number of records to be blocked: ' + str(len(rec_dict)))
    print('')

    rec_id_list = list(rec_dict.keys())

    block_dict = {'all_rec': rec_id_list}

    return block_dict


# -----------------------------------------------------------------------------

def simpleBlocking(rec_dict, blk_attr_list):
    """Build the blocking index data structure (dictionary) to store blocking
       key values (BKV) as keys and the corresponding list of record identifiers.

       A blocking is implemented that simply concatenates attribute values.

       Parameter Description:
         rec_dict      : Dictionary that holds the record identifiers as keys
                         and corresponding list of record values
         blk_attr_list : List of blocking key attributes to use

       This method returns a dictionary with blocking key values as its keys and
       list of record identifiers as its values (one list for each block).

       Examples:
         If the blocking is based on 'postcode' then:
           block_dict = {'2000': [rec1_id, rec2_id, rec3_id, ...],
                         '2600': [rec4_id, rec5_id, ...],
                           ...
                        }
         while if the blocking is based on 'postcode' and 'gender' then:
           block_dict = {'2000f': [rec1_id, rec3_id, ...],
                         '2000m': [rec2_id, ...],
                         '2600f': [rec5_id, ...],
                         '2600m': [rec4_id, ...],
                          ...
                        }
    """

    block_dict = {}  # The dictionary with blocks to be generated and returned

    print('Run simple blocking:')
    print('  List of blocking key attributes: ' + str(blk_attr_list))
    print('  Number of records to be blocked: ' + str(len(rec_dict)))
    print('')

    for (rec_id, rec_values) in rec_dict.items():

        rec_bkv = ''  # Initialise the blocking key value for this record

        # Process selected blocking attributes
        #
        for attr in blk_attr_list:
            attr_val = rec_values[attr]
            rec_bkv += attr_val

        # Insert the blocking key value and record into blocking dictionary
        #
        if (rec_bkv in block_dict):  # Block key value in block index

            # Only need to add the record
            #
            rec_id_list = block_dict[rec_bkv]
            rec_id_list.append(rec_id)

        else:  # Block key value not in block index

            # Create a new block and add the record identifier
            #
            rec_id_list = [rec_id]

        block_dict[rec_bkv] = rec_id_list  # Store the new block

    return block_dict


# -----------------------------------------------------------------------------

def phoneticBlocking(rec_dict, blk_attr_list):
    """Build the blocking index data structure (dictionary) to store blocking
       key values (BKV) as keys and the corresponding list of record identifiers.

       A blocking is implemented that concatenates Soundex encoded values of
       attribute values.

       Parameter Description:
         rec_dict      : Dictionary that holds the record identifiers as keys
                         and corresponding list of record values
         blk_attr_list : List of blocking key attributes to use

       This method returns a dictionary with blocking key values as its keys and
       list of record identifiers as its values (one list for each block).
    """

    block_dict = {}  # The dictionary with blocks to be generated and returned

    # Soundex Cheat Sheet
    rm_aeiouyhw = re.compile(r"[aeiouyhw]")
    rp_bfpv = re.compile(r"[bfpv]+")
    rp_cgjkqsxz = re.compile(r"[cgjkqsxz]+")
    rp_dt = re.compile(r"[dt]+")
    rp_l = re.compile(r"[l]+")
    rp_mn = re.compile(r"[mn]+")
    rp_r = re.compile(r"[r]+")


    print('Run phonetic blocking:')
    print('  List of blocking key attributes: ' + str(blk_attr_list))
    print('  Number of records to be blocked: ' + str(len(rec_dict)))
    print('')

    for (rec_id, rec_values) in rec_dict.items():

        rec_bkv = ''  # Initialise the blocking key value for this record

        # Process selected blocking attributes
        #
        for attr in blk_attr_list:
            attr_val: str = rec_values[attr]

            # *********** Implement Soundex function here *********

            # Add your code here
            # 1. return 4 0's if value is not empty else
            # This is important for indexing attr_val with index 0 after soundex procedure
            if attr_val == "":
                rec_bkv += "0000"
                continue

            # 2. remove a, e ,i , o, u, y, h, w
            val = rm_aeiouyhw.sub('', attr_val[1:])

            # 3. replace group of letters with their numbers
            val = rp_bfpv.sub("1", val)
            val = rp_cgjkqsxz.sub("2", val)
            val = rp_dt.sub("3", val)
            val = rp_l.sub("4", val)
            val = rp_mn.sub("5", val)
            val = rp_r.sub("6", val)

            rec_bkv += f"{attr_val[0].upper()}{val}000"[:4]

            # Also think about how to handle empty attribute values

            # ************ End of your Soundex code *********************************

        # Insert the blocking key value and record into blocking dictionary
        #
        if (rec_bkv in block_dict):  # Block key value in block index

            # Only need to add the record
            #
            rec_id_list = block_dict[rec_bkv]
            rec_id_list.append(rec_id)

        else:  # Block key value not in block index

            # Create a new block and add the record identifier
            #
            rec_id_list = [rec_id]

        block_dict[rec_bkv] = rec_id_list  # Store the new block

    return block_dict


# -----------------------------------------------------------------------------

def slkBlocking(rec_dict, fam_name_attr_ind, giv_name_attr_ind,
                dob_attr_ind, gender_attr_ind):
    """Build the blocking index data structure (dictionary) to store blocking
       key values (BKV) as keys and the corresponding list of record identifiers.

       This function should implement the statistical linkage key (SLK-581)
       blocking approach as used in real-world linkage applications:

       http://www.aihw.gov.au/WorkArea/DownloadAsset.aspx?id=60129551915

       A SLK-581 blocking key is the based on the concatenation of:
       - 3 letters of family name
       - 2 letters of given name
       - Date of birth
       - Sex

       Parameter Description:
         rec_dict          : Dictionary that holds the record identifiers as
                             keys and corresponding list of record values
         fam_name_attr_ind : The number (index) of the attribute that contains
                             family name (last name)
         giv_name_attr_ind : The number (index) of the attribute that contains
                             given name (first name)
         dob_attr_ind      : The number (index) of the attribute that contains
                             date of birth
         gender_attr_ind   : The number (index) of the attribute that contains
                             gender (sex)

       This method returns a dictionary with blocking key values as its keys and
       list of record identifiers as its values (one list for each block).
    """

    block_dict = {}  # The dictionary with blocks to be generated and returned

    print('Run SLK-581 blocking:')
    print('  Number of records to be blocked: ' + str(len(rec_dict)))
    print('')

    for (rec_id, rec_values) in rec_dict.items():

        rec_bkv = ''  # Initialise the blocking key value for this record

        # *********** Implement SLK-581 function here ***********

        # Add your code here
        # Coding of family name and given name
        if rec_values[fam_name_attr_ind]:
            fam_name_coding = f"{rec_values[fam_name_attr_ind][1:3]}{rec_values[fam_name_attr_ind][:4][3:]}22"[:3]
        else:
            fam_name_coding = "999"

        if rec_values[giv_name_attr_ind]:
            given_name_coding = f"{rec_values[giv_name_attr_ind][1:3]}2"[:2]
        else:
            given_name_coding = "99"

        # Could not find a replacement for missing values
        dd, mm, yyyy = rec_values[dob_attr_ind].split('/')
        dd = f"0{dd}" if len(dd) == 1 else dd
        mm = f"0{mm}" if len(mm) == 1 else mm

        if rec_values[gender_attr_ind] == "m":
            gender_coding = "1"
        elif rec_values[gender_attr_ind] == "w":
            gender_coding = "2"
        else:
            gender_coding = "9"

        rec_bkv = f"{fam_name_coding}{given_name_coding}{dd}{mm}{yyyy}{gender_coding}"

        # ************ End of your SLK-581 code ***********************************

        # Insert the blocking key value and record into blocking dictionary
        #
        if rec_bkv in block_dict:  # Block key value in block index

            # Only need to add the record
            #
            rec_id_list = block_dict[rec_bkv]
            rec_id_list.append(rec_id)

        else:  # Block key value not in block index

            # Create a new block and add the record identifier
            #
            rec_id_list = [rec_id]

        block_dict[rec_bkv] = rec_id_list  # Store the new block

    return block_dict


# -----------------------------------------------------------------------------

# Extra task if you have time:
# - Implement canopy clustering based blocking as described in the lectures
#   and the Data Matching book

# -----------------------------------------------------------------------------

def printBlockStatistics(blockA_dict, blockB_dict):
    """Calculate and print some basic statistics about the generated blocks
    """

    print('Statistics of the generated blocks:')

    numA_blocks = len(blockA_dict)
    numB_blocks = len(blockB_dict)

    block_sizeA_list = []
    for rec_id_list in blockA_dict.values():  # Loop over all blocks
        block_sizeA_list.append(len(rec_id_list))

    block_sizeB_list = []
    for rec_id_list in blockB_dict.values():  # Loop over all blocks
        block_sizeB_list.append(len(rec_id_list))

    print('Dataset A number of blocks generated: %d' % (numA_blocks))
    print('    Minimum block size: %d' % (min(block_sizeA_list)))
    print('    Average block size: %.2f' % \
          (float(sum(block_sizeA_list)) / len(block_sizeA_list)))
    print('    Maximum block size: %d' % (max(block_sizeA_list)))
    print('')

    print('Dataset B number of blocks generated: %d' % (numB_blocks))
    print('    Minimum block size: %d' % (min(block_sizeB_list)))
    print('    Average block size: %.2f' % \
          (float(sum(block_sizeB_list)) / len(block_sizeB_list)))
    print('    Maximum block size: %d' % (max(block_sizeB_list)))
    print('')

# -----------------------------------------------------------------------------

# End of program.
