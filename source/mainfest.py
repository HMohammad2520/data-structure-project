from .lesson_script import LessonScript

compile_dir_1 = 'build/chapter_1/'
compile_dir_2 = 'build/chapter_2/'
compile_dir_3 = 'build/chapter_3/'
compile_dir_4 = 'build/chapter_4/'


# Chapter 1
ch_1_factorial     = LessonScript(1, 'Factorial',          'source/chapter_1/01_factorial.cpp',     compile_dir_1)
ch_1_matrix_add    = LessonScript(2, 'Matrix Addition',    'source/chapter_1/02_matrix_add.cpp',    compile_dir_1)
ch_1_bubble_sort   = LessonScript(3, 'Bubble Sort',        'source/chapter_1/03_bubble_sort.cpp',   compile_dir_1)
ch_1_linear_search = LessonScript(4, 'Linear Search',      'source/chapter_1/04_linear_search.cpp', compile_dir_1)
ch_1_max_element   = LessonScript(5, 'Max Element',        'source/chapter_1/05_max_element.cpp',   compile_dir_1)
ch_1_fibonacci     = LessonScript(6, 'Fibonacci Sequence', 'source/chapter_1/06_fibonacci.cpp',     compile_dir_1)
ch_1_hanoi_tower   = LessonScript(7, 'Hanoi Tower',        'source/chapter_1/07_hanoi_tower.cpp',   compile_dir_1)


# Chapter 2
ch_2_array_simple     = LessonScript(1, 'Array Simple',        'source/chapter_2/01_array_simple.cpp',     compile_dir_2)
ch_2_array_addresses  = LessonScript(2, 'Array Addresses',     'source/chapter_2/02_array_addresses.cpp',  compile_dir_2)
ch_2_address_formula  = LessonScript(3, 'Address Formula',     'source/chapter_2/03_address_formula.cpp',  compile_dir_2)
ch_2_linear_search    = LessonScript(4, 'Linear Search',       'source/chapter_2/04_linear_search.cpp',    compile_dir_2)
ch_2_binary_search    = LessonScript(5, 'Binary Search',       'source/chapter_2/05_binary_search.cpp',    compile_dir_2)
ch_2_matrix_addresses = LessonScript(6, '2D Matrix Addresses', 'source/chapter_2/06_matrix_addresses.cpp', compile_dir_2)
ch_2_sparse_matrix    = LessonScript(7, 'Sparse Matrix',       'source/chapter_2/07_sparse_matrix.cpp',    compile_dir_2)


# Chapter 3
ch_3_stack_array           = LessonScript(1, 'Stack Array',           'source/chapter_3/01_stack_array.cpp',           compile_dir_3)
ch_3_stack_under_flow      = LessonScript(2, 'Stack Under Flow',      'source/chapter_3/02_stack_under_flow.cpp',      compile_dir_3)
ch_3_postfix_expression    = LessonScript(3, 'Postfix Expression',    'source/chapter_3/03_postfix_expression.cpp',    compile_dir_3)
ch_3_infix_to_postfix      = LessonScript(4, 'Infix To Postfix',      'source/chapter_3/04_infix_to_postfix.cpp',      compile_dir_3)
ch_3_recursive_subroutines = LessonScript(5, 'Recursive subroutines', 'source/chapter_3/05_recursive_subroutines.cpp', compile_dir_3)


# Chapter 4
ch_4_queue_fifo_lifo = LessonScript(1, 'Queue FIFO / LIFO',     'source/chapter_4/01_queue_fifo_lifo.cpp', compile_dir_4)
ch_4_queue_ops       = LessonScript(2, 'Queue Operations',      'source/chapter_4/02_queue_ops.cpp',       compile_dir_4)
ch_4_queue_display   = LessonScript(3, 'Queue Display',         'source/chapter_4/03_queue_display.cpp',   compile_dir_4)
ch_4_linked_list     = LessonScript(4, 'Linked List',           'source/chapter_4/04_linked_list.cpp',     compile_dir_4)
ch_4_loops           = LessonScript(5, 'Loops',                 'source/chapter_4/05_loops.cpp',           compile_dir_4)
ch_4_list_traversal  = LessonScript(6, 'Linked List Traversal', 'source/chapter_4/06_list_traversal.cpp',  compile_dir_4)


lessons = [
    # Chapter 1
    ch_1_factorial,
    ch_1_matrix_add,
    ch_1_bubble_sort,
    ch_1_linear_search,
    ch_1_max_element,
    ch_1_fibonacci,
    ch_1_hanoi_tower,

    # Chapter 2
    ch_2_array_simple,
    ch_2_array_addresses,
    ch_2_address_formula,
    ch_2_linear_search,
    ch_2_binary_search,
    ch_2_matrix_addresses,
    ch_2_sparse_matrix,

    # Chapter 3
    ch_3_stack_array,
    ch_3_stack_under_flow,
    ch_3_postfix_expression,
    ch_3_infix_to_postfix,
    ch_3_recursive_subroutines,

    # Chapter 4
    ch_4_queue_fifo_lifo,
    ch_4_queue_ops,
    ch_4_queue_display,
    ch_4_linked_list,
    ch_4_loops,
    ch_4_list_traversal,
]