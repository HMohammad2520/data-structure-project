from .lesson_script import LessonScript

compile_dir_1 = 'build/chapter_1/'
compile_dir_2 = 'build/chapter_2/'
compile_dir_3 = 'build/chapter_3/'
compile_dir_4 = 'build/chapter_4/'


# Chapter 3
ch_3_stack_array = LessonScript(1, 'Stack Array', 'source/chapter_3/01_stack_array.cpp', compile_dir_3)
ch_3_stack_under_flow = LessonScript(2, 'Stack Under Flow', 'source/chapter_3/02_stack_under_flow.cpp', compile_dir_3)
ch_3_postfix_expression = LessonScript(3, 'Postfix Expression', 'source/chapter_3/03_postfix_expression.cpp', compile_dir_3)
ch_3_infix_to_postfix = LessonScript(4, 'Infix To Postfix', 'source/chapter_3/04_infix_to_postfix.cpp', compile_dir_3)
ch_3_recursive_subroutines = LessonScript(5, 'Recursive subroutines', 'source/chapter_3/05_recursive_subroutines.cpp', compile_dir_3)


# Chapter 3
ch_4_queue_fifo_lifo = LessonScript(1, 'Queue', 'source/chapter_4/01_queue_fifo_lifo.cpp', compile_dir_4)

lessons = [

    # Chapter 3
    ch_3_stack_array,
    ch_3_stack_under_flow,
    ch_3_postfix_expression,
    ch_3_infix_to_postfix,
    ch_3_recursive_subroutines,

    # Chapter 4
    ch_4_queue_fifo_lifo,
]