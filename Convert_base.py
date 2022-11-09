def get_key(key):
    block_1 = key[0:5]
    block_2 = key[5:10]
    block_3 = key[10:15]
    block_4 = key[15:]

    block_1 = int(block_1, 16)
    block_2 = int(block_2, 16)
    block_3 = int(block_3, 16)  

    key = str(str(block_1) + str(block_2) + str(block_3) + str(block_4))

    return key