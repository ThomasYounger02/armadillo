
def sub_dict(dct, keys, default=None):
    '''获取字典的子集
    '''
    return dict([(key, dct.get(key, default)) for key in keys])

def sub_list(list_full, list_to_drop):
    '''从原list_full列表中减去list_to_drop部分
    '''
    list_to_remain = list(set(list_full) - set(list_to_drop))
    return list_to_remain