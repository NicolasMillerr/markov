from markov.linked_list import (
    LinkedList,
    Node,
)


def test_set_value():
    linked_list = LinkedList()
    linked_list.insert_at_head(10)
    assert isinstance(linked_list.head, Node)
    assert linked_list.head.value == 10
    linked_list.insert_at_head(20)
    assert linked_list.head.value == 20


def test_length():
    linked_list = LinkedList()
    assert len(linked_list) == 0
    linked_list.insert_at_head(10)
    assert len(linked_list) == 1

    linked_list[0] = 20
    assert len(linked_list) == 1

    linked_list.insert_at_key(0, 10)
    assert len(linked_list) == 2
    assert linked_list[0] == 10


def test_acces_with_index():
    ll = LinkedList.linked_list_from_list([10, 20])
    assert ll[0].value == 10

    assert ll[1].value == 20

    ll[1] = 3
    assert ll[1] == 3
