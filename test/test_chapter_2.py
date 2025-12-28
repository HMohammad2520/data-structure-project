from source.mainfest import (
    ch_2_array_simple,
    ch_2_array_addresses,
    ch_2_address_formula,
    ch_2_linear_search,
    ch_2_binary_search,
    ch_2_matrix_addresses,
    ch_2_sparse_matrix,
)


def test_array_simple():
    assert ch_2_array_simple.run('2', '99', '100') == '99 100'
    assert ch_2_array_simple.run('3', '1', '2', '3') == '1 2 3'
    assert ch_2_array_simple.run('4', '7', '8', '9', '10') == '7 8 9 10'
    assert ch_2_array_simple.run('5', '10', '20', '30', '40', '50') == '10 20 30 40 50'


def test_array_addresses():
    ## برای اینکه آدرس ها متغیر هستند وجود یک مقدار بررسی میشود
    assert ch_2_array_addresses.run('2', '99', '100')
    assert ch_2_array_addresses.run('3', '1', '2', '3')
    assert ch_2_array_addresses.run('4', '7', '8', '9', '10')
    assert ch_2_array_addresses.run('5', '10', '20', '30', '40', '50')


def test_address_formula():
    assert ch_2_address_formula.run('0', '10', '7') == '70'
    assert ch_2_address_formula.run('200', '8', '5') == '240'
    assert ch_2_address_formula.run('500', '2', '20') == '540'
    assert ch_2_address_formula.run('1000', '4', '3') == '1012'


def test_linear_search():
    assert ch_2_linear_search.run('3', '7', '8', '9', '7') == '0'
    assert ch_2_linear_search.run('3', '7', '8', '9', '10') == '-1'
    assert ch_2_linear_search.run('4', '1', '2', '3', '4', '4') == '3'
    assert ch_2_linear_search.run('5', '10', '20', '30', '40', '50', '30') == '2'

def test_binary_search():
    assert ch_2_binary_search.run('3', '10', '20', '30', '25') == '-1'
    assert ch_2_binary_search.run('4', '1', '3', '5', '7', '5') == '2'
    assert ch_2_binary_search.run('6', '1', '2', '3', '4', '5', '6', '4') == '3'
    assert ch_2_binary_search.run('5', '10', '20', '30', '40', '50', '30') == '2'


def test_matrix_addresses():
    ## برای اینکه آدرس ها متغیر هستند وجود یک مقدار بررسی میشود
    assert ch_2_matrix_addresses.run('2', '2', '1', '2', '3', '4')
    assert ch_2_matrix_addresses.run('1', '4', '10', '20', '30', '40')
    assert ch_2_matrix_addresses.run('3', '2', '1', '2', '3', '4', '5', '6')
    assert ch_2_matrix_addresses.run('2', '3', '7', '8', '9', '10', '11', '12')


def test_sparse_matrix():
    assert ch_2_sparse_matrix.run('2', '2', '1', '0', '0', '9') == '0:0=9'
    assert ch_2_sparse_matrix.run('2', '3', '2', '0', '1', '7', '1', '2', '8') == '0:1=7 1:2=8'
    assert ch_2_sparse_matrix.run('3', '3', '2', '0', '1', '5', '2', '2', '10') == '0:1=5 2:2=10'
    assert ch_2_sparse_matrix.run('3', '3', '3', '0', '0', '1', '1', '1', '2', '2', '2', '3') == '0:0=1 1:1=2 2:2=3'
    
