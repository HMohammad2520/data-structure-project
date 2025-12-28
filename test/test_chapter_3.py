from source.mainfest import (
    ch_3_stack_array,
    ch_3_stack_under_flow,
    ch_3_postfix_expression,
    ch_3_infix_to_postfix,
    ch_3_recursive_subroutines,
)


def test_stack_array():
    assert ch_3_stack_array.run('10', '20', '30', 'pop', '40')


def test_stack_under_flow():
    assert ch_3_stack_under_flow.run() == 'STACK UNDERFLOW'


def test_postfix_expression():
    assert ch_3_postfix_expression.run('1', '1', '+') == '2'
    assert ch_3_postfix_expression.run('2', '1', '-') == '1'
    assert ch_3_postfix_expression.run('4', '2', 'x') == '8'
    assert ch_3_postfix_expression.run('8', '4', '/') == '2'


def test_infix_to_postfix():
    assert ch_3_infix_to_postfix.run('(A*C)') == 'AC*'
    assert ch_3_infix_to_postfix.run('(A+B)*C') == 'AB+C*'
    assert ch_3_infix_to_postfix.run('(A+B*C)') == 'ABC*+'
    assert ch_3_infix_to_postfix.run('A+B+(D*C)') == 'AB+DC*+'


def test_recursive_subroutines():
    assert ch_3_recursive_subroutines.run('2') == '2'
    assert ch_3_recursive_subroutines.run('4') == '24'
    assert ch_3_recursive_subroutines.run('5') == '120'
    assert ch_3_recursive_subroutines.run('6') == '720'
    assert ch_3_recursive_subroutines.run('12') == '479001600'
    assert ch_3_recursive_subroutines.run('16') == '2004189184'
