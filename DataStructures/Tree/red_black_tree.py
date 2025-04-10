def new_map():
    return {'key': None, 'value': None, 'left': None, 'right': None}

def put(my_rbt, key, value):
    if my_rbt is None:
        my_rbt = new_map()
    if key < my_rbt['key']:
        if my_rbt['left'] is None:
            my_rbt['left'] = new_map()
            put(my_rbt['left'], key, value)
        else:
            put(my_rbt['left'], key, value)
    elif key > my_rbt['key']:
        if my_rbt['right'] is None:
            my_rbt['right'] = new_map()
            put(my_rbt['right'], key, value)
        else:
            put(my_rbt['right'], key, value)
    else:
        my_rbt['value'] = value
        
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
    if my_rbt is None:
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