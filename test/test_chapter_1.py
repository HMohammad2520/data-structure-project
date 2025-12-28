from source.mainfest import (
    ch_1_factorial,
    ch_1_matrix_add,
    ch_1_bubble_sort,
    ch_1_linear_search,
    ch_1_max_element,
    ch_1_fibonacci,
    ch_1_hanoi_tower,
)


def test_factorial():
    assert ch_1_factorial.run('1') == '1'
    assert ch_1_factorial.run('2') == '2'
    assert ch_1_factorial.run('5') == '120'
    assert ch_1_factorial.run('10') == '3628800'


def test_matrix_add():
    assert ch_1_matrix_add.run(
        '2', '2',  # m, n
        '1', '3', '2', '4', # Matrix 1
        '3', '1', '2', '1', # Matrix 2
    ).splitlines() == ['4 4 ',
                       '4 5']

    assert ch_1_matrix_add.run(
        '2', '2',  # m, n
        '10', '21', '34', '12', # Matrix 1
        '51', '14', '7', '11', # Matrix 2
    ).splitlines() == ['61 35 ',
                       '41 23']


def test_bubble_sort():
    assert ch_1_bubble_sort.run('3', '1', '3', '2') == '1 2 3'
    assert ch_1_bubble_sort.run('5', '4', '2', '7', '1', '3') == '1 2 3 4 7'
    assert ch_1_bubble_sort.run('7', '11', '31', '41', '62', '14', '6', '10') == '6 10 11 14 31 41 62'


def test_linear_search():
    assert ch_1_linear_search.run('3', '6', '4', '6', '5') == '1'
    assert ch_1_linear_search.run('5', '7', '4', '2', '7', '1', '3') == '2'


def test_max_element():
    assert ch_1_max_element.run('4', '4', '3', '2', '7') == '7'
    assert ch_1_max_element.run('5', '31', '11', '68', '13', '41') == '68'


def test_fibonnaci():
    assert ch_1_fibonacci.run('1') == '0'
    assert ch_1_fibonacci.run('3') == '1'
    assert ch_1_fibonacci.run('5') == '3'
    assert ch_1_fibonacci.run('10') == '34'


def test_hanoi_tower():
    assert ch_1_hanoi_tower.run('2') == ('Move disk 1 from A to B\n'+
                                         'Move disk 2 from A to C\n'+
                                         'Move disk 1 from B to C')

