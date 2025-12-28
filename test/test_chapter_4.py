from source.mainfest import (
    ch_4_queue_fifo_lifo,
    ch_4_queue_ops,
    ch_4_queue_display,
    ch_4_linked_list,
    ch_4_loops,
    ch_4_list_traversal,
)


def test_queue_fifo_lifo():
    assert ch_4_queue_fifo_lifo.run('1', '2') == "ENQUEUE 1\nENQUEUE 2\nFRONT 1"
    assert ch_4_queue_fifo_lifo.run('10', '20', '30', 'dequeue', '40') == "ENQUEUE 10\nENQUEUE 20\nENQUEUE 30\nDEQUEUE 10\nENQUEUE 40\nFRONT 20"


def test_queue_ops():
    assert ch_4_queue_ops.run('2', '1', '2') == '2'
    assert ch_4_queue_ops.run('5', '10', '20', '30', '40', '50') == '20 30 40 50'


def test_queue_display():
    assert ch_4_queue_display.run('3', '1', '2', '3') == '1 2 3'
    assert ch_4_queue_display.run('5', '1', '2', '3', '4', '5') == '1 2 3 4 5'
    assert ch_4_queue_display.run('5', '31', '22', '13', '46', '54') == '31 22 13 46 54'


def test_linked_list():
    assert ch_4_linked_list.run('2', '1', '2') == '1 2'
    assert ch_4_linked_list.run('5', '1', '2', '3', '4', '5') == '1 2 3 4 5'
    assert ch_4_linked_list.run('5', '31', '22', '13', '46', '54') == '31 22 13 46 54'


def test_loops():
    assert ch_4_loops.run('2') == '1 2'
    assert ch_4_loops.run('5') == '1 2 3 4 5'
    assert ch_4_loops.run('10') == '1 2 3 4 5 6 7 8 9 10'


def test_list_traversal():
    assert ch_4_list_traversal.run('2', '1', '2') == '1 2'
    assert ch_4_list_traversal.run('5', '1', '2', '3', '4', '5') == '1 2 3 4 5'
    assert ch_4_list_traversal.run('5', '31', '22', '13', '46', '54') == '31 22 13 46 54'