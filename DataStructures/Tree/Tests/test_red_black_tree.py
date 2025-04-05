from DataStructures.Tree import red_black_tree as rbt
from DataStructures.Tree import rbt_node as rbt_node
from DataStructures.Utils.utils import handle_not_implemented


def compare_function_test(key, key_node):
    if key < key_node:
        return -1
    elif key > key_node:
        return 1
    else:
        return 0


def setup_tests():
    empty_tree = rbt.new_map()

    return empty_tree


def setup_three_nodes():
    three_nodes = rbt.new_map()
    node_1 = rbt_node.new_node(1, 1)
    node_3 = rbt_node.new_node(10, 10)
    node_2 = rbt_node.new_node(5, 5)

    node_1["parent"] = node_2
    node_2["left"] = node_1
    node_2["right"] = node_3
    node_2["size"] = 3
    node_3["parent"] = node_2

    three_nodes["root"] = node_2

    return three_nodes


def setup_seven_nodes():
    seven_nodes = rbt.new_map()
    node_1 = rbt_node.new_node(10, 10)
    node_2 = rbt_node.new_node(20, 20)
    node_3 = rbt_node.new_node(30, 30)
    node_4 = rbt_node.new_node(40, 40)
    node_5 = rbt_node.new_node(50, 50)
    node_6 = rbt_node.new_node(60, 60)
    node_7 = rbt_node.new_node(70, 70)

    node_2["left"] = node_1
    node_2["right"] = node_3
    node_2["size"] = 3

    node_6["left"] = node_5
    node_6["right"] = node_7
    node_6["size"] = 3

    node_4["left"] = node_2
    node_4["right"] = node_6
    node_4["size"] = 7

    seven_nodes["root"] = node_4

    return seven_nodes


@handle_not_implemented
def test_new_map():
    empty_rbt = rbt.new_map()

    assert empty_rbt["root"] is None


@handle_not_implemented
def test_put():
    empty_tree = rbt.new_map()
    
    result = rbt.put(empty_tree, 5, "test")
    
    assert isinstance(result, dict)
    assert "root" in result


@handle_not_implemented
def test_get():
    empty_tree = {"root": None}
    
    result = rbt.get(empty_tree, 5)
    
    assert result is None


@handle_not_implemented
def test_remove():
    empty_tree = {"root": None}
    
    result = rbt.remove(empty_tree, 5)
    
    assert isinstance(result, dict)
    assert "root" in result


@handle_not_implemented
def test_contains():
    empty_tree = {"root": None}

    result = rbt.contains(empty_tree, 10)

    assert isinstance(result, bool)


@handle_not_implemented
def test_size():
    empty_tree = {"root": None}

    result = rbt.size(empty_tree)

    assert isinstance(result, int)


@handle_not_implemented
def test_is_empty():
    empty_rbt = setup_tests()
    three_rbt = setup_three_nodes()

    # Verificar si un árbol vacío está vacío
    assert rbt.is_empty(empty_rbt)

    # Verificar si un árbol con 3 nodos está vacío
    assert not rbt.is_empty(three_rbt)


@handle_not_implemented
def test_key_set():
    empty_tree = {"root": None}

    result = rbt.key_set(empty_tree)

    # Contar los elementos manualmente sin usar single_linked
    count = 0
    current = result["first"]
    while current is not None:
        count += 1
        current = current["next"]

    assert count == 0


@handle_not_implemented
def test_value_set():
    empty_tree = {"root": None}

    result = rbt.value_set(empty_tree)

    # Contar manualmente los elementos en la lista enlazada
    count = 0
    current = result["first"]
    while current is not None:
        count += 1
        current = current["next"]

    assert count == 0


@handle_not_implemented
def test_get_min():
    empty_tree = {"root": None}
    assert rbt.get_min(empty_tree) is None

    # Insertar nodos
    tree = {"root": None}
    rbt.put(tree, 30, "A")
    rbt.put(tree, 10, "B")
    rbt.put(tree, 20, "C")
    rbt.put(tree, 5, "D")
    rbt.put(tree, 40, "E")

    # El menor valor de llave debe ser 5
    assert rbt.get_min(tree) == 5


@handle_not_implemented
def test_get_max():
    empty_tree = {"root": None}
    assert rbt.get_max(empty_tree) is None

    tree = {"root": None}
    rbt.put(tree, 15, "A")
    rbt.put(tree, 10, "B")
    rbt.put(tree, 5, "C")
    rbt.put(tree, 20, "D")

    # El máximo debería ser la llave 20
    assert rbt.get_max(tree) == 20


@handle_not_implemented
def test_delete_min():
    tree = rbt.new_map()

    # Insertamos varias llaves
    rbt.put(tree, 50, "a")
    rbt.put(tree, 30, "b")
    rbt.put(tree, 70, "c")
    rbt.put(tree, 10, "d")  
    rbt.put(tree, 40, "e")

    assert rbt.get_min(tree) == 10

    rbt.delete_min(tree)

    assert rbt.get_min(tree) == 30


@handle_not_implemented
def test_delete_max():
    # Árbol vacío
    empty_tree = {"root": None}
    rbt.delete_max(empty_tree)
    assert empty_tree["root"] is None

    # Árbol con varios elementos
    tree = {"root": None}
    rbt.put(tree, 30, "A")
    rbt.put(tree, 10, "B")
    rbt.put(tree, 40, "C")
    rbt.put(tree, 35, "D")

    # El máximo es 40, lo eliminamos
    tree = rbt.delete_max(tree)
    assert rbt.get_max(tree) == 35

    # Eliminamos otro máximo
    tree = rbt.delete_max(tree)
    assert rbt.get_max(tree) == 30


@handle_not_implemented
def test_floor():
    tree = rbt.new_map()

    # Insertar algunas llaves
    rbt.put(tree, 10, "a")
    rbt.put(tree, 20, "b")
    rbt.put(tree, 30, "c")
    rbt.put(tree, 40, "d")
    rbt.put(tree, 50, "e")

    # Casos donde la llave está en el árbol
    assert rbt.floor(tree, 10) == 10
    assert rbt.floor(tree, 20) == 20

    # Casos donde la llave no está pero existe predecesor
    assert rbt.floor(tree, 25) == 20
    assert rbt.floor(tree, 45) == 40

    # Casos extremos
    assert rbt.floor(tree, 5) is None  # menor que la mínima
    assert rbt.floor(tree, 60) == 50   # mayor que la máxima


@handle_not_implemented
def test_ceiling():
    tree = rbt.new_map()

    # Insertar algunas llaves
    rbt.put(tree, 10, "a")
    rbt.put(tree, 20, "b")
    rbt.put(tree, 30, "c")
    rbt.put(tree, 40, "d")
    rbt.put(tree, 50, "e")

    # Casos donde la llave está en el árbol
    assert rbt.ceiling(tree, 10) == 10
    assert rbt.ceiling(tree, 20) == 20

    # Casos donde la llave no está pero existe sucesor
    assert rbt.ceiling(tree, 25) == 30
    assert rbt.ceiling(tree, 45) == 50

    # Casos extremos
    assert rbt.ceiling(tree, 5) == 10    # menor que la mínima
    assert rbt.ceiling(tree, 60) is None # mayor que la máxima


@handle_not_implemented
def test_select():
    tree = rbt.new_map()
    rbt.put(tree, 10, "a")
    key = rbt.select(tree, 0)
    assert key is None or isinstance(key, (int, float, str))


@handle_not_implemented
def test_rank():
    tree = rbt.new_map()
    rbt.put(tree, 10, "a")
    r = rbt.rank(tree, 10)
    assert isinstance(r, int)


@handle_not_implemented
def test_heigh():
    tree = rbt.new_map()
    rbt.put(tree, 10, "a")
    h = rbt.height(tree)
    assert isinstance(h, int)


@handle_not_implemented
def test_keys():
    tree = rbt.new_map()
    rbt.put(tree, 10, "a")
    rbt.put(tree, 20, "b")
    keys = rbt.keys(tree, 5, 25)
    assert isinstance(keys, object)


@handle_not_implemented
def test_values():
    tree = rbt.new_map()
    rbt.put(tree, 10, "a")
    rbt.put(tree, 20, "b")
    values = rbt.values(tree, 5, 25)
    assert isinstance(values, object)