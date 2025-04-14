from DataStructures.List import single_linked_list as sl

def new_map():
    return {'key': None, 'value': None, 'left': None, 'right': None}

def put(my_rbt, key, value):
    if my_rbt is None:
        return {'key': key, 'value': value, 'left': None, 'right': None}
    if my_rbt['key'] is None:
        my_rbt['key'] = key
        my_rbt['value'] = value
        return my_rbt
    if key < my_rbt['key']:
        my_rbt['left'] = put(my_rbt['left'], key, value)
    elif key > my_rbt['key']:
        my_rbt['right'] = put(my_rbt['right'], key, value)
    else:
        my_rbt['value'] = value
    return my_rbt


def insert_node(root, key, value):
    if root is None:
        root = new_map()
        root['key'] = key
        root['value'] = value
    elif key < root['key']:
        root['left'] = insert_node(root['left'], key, value)
    elif key > root['key']:
        root['right'] = insert_node(root['right'], key, value)
    else:
        root['value'] = value
    return root

def get(my_rbt, key):
    if my_rbt is None or my_rbt['key'] is None:
        return None
    if key < my_rbt['key']:
        return get(my_rbt['left'], key)
    elif key > my_rbt['key']:
        return get(my_rbt['right'], key)
    else:
        return my_rbt['value']

def get_node(root, key):
    if root is None:
        return None
    if key < root['key']:
        return get_node(root['left'], key)
    elif key > root['key']:
        return get_node(root['right'], key)
    else:
        return root
    
def remove(my_rbt, key):
    if my_rbt is None:
        return None
    if key < my_rbt['key']:
        my_rbt['left'] = remove(my_rbt['left'], key)
    elif key > my_rbt['key']:
        my_rbt['right'] = remove(my_rbt['right'], key)
    else:
        if my_rbt['left'] is None and my_rbt['right'] is None:
            return None
        elif my_rbt['left'] is None:
            return my_rbt['right']
        elif my_rbt['right'] is None:
            return my_rbt['left']
        else:
            min_node = my_rbt['right']
            while min_node['left'] is not None:
                min_node = min_node['left']
            my_rbt['key'] = min_node['key']
            my_rbt['value'] = min_node['value']
            my_rbt['right'] = remove(my_rbt['right'], min_node['key'])
            return my_rbt    

def remove_node(root, key):
    if root is None:
        return None
    if key < root['key']:
        root['left'] = remove_node(root['left'], key)
    elif key > root['key']:
        root['right'] = remove_node(root['right'], key)
    else:
        if root['left'] is None and root['right'] is None:
            return None
        elif root['left'] is None:
            return root['right']
        elif root['right'] is None:
            return root['left']
        else:
            min_node = root['right']
            while min_node['left'] is not None:
                min_node = min_node['left']
            root['key'] = min_node['key']
            root['value'] = min_node['value']
            root['right'] = remove_node(root['right'], min_node['key'])
            return root
        
def height(my_rbt):
    if my_rbt is None or my_rbt['key'] is None:
        return 0
    left_height = height(my_rbt['left'])
    right_height = height(my_rbt['right'])
    return max(left_height, right_height) + 1

def size(my_rbt):
    if my_rbt is None or my_rbt['key'] is None:
        return 0
    left_size = size(my_rbt['left'])
    right_size = size(my_rbt['right'])
    return 1 + left_size + right_size

def left_key(my_rbt):
    if my_rbt is None:
        return None
    if my_rbt['left'] is None:
        return my_rbt['key']
    return left_key(my_rbt['left'])

def right_key(my_rbt):
    if my_rbt is None:
        return None
    if my_rbt['right'] is None:
        return my_rbt['key']
    return right_key(my_rbt['right'])

def values(my_bst, key_initial, key_final):
    result = {'elements': []}
    values_range(my_bst, key_initial, key_final, result)
    return result

def values_range(root, key_initial, key_final, list_value):
    if root is None or root.get('key') is None:
        return
    if root['key'] > key_initial:
        values_range(root['left'], key_initial, key_final, list_value)
    if key_initial <= root['key'] <= key_final:
        sl.add_last(list_value, root['value'])
    if root['key'] < key_final:
        values_range(root['right'], key_initial, key_final, list_value)