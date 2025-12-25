from source.mainfest import lessons


if __name__ == '__main__':
    for script in lessons:
        try:
            script.compile()
            print(f'Compile Done: {script}')
        except Exception as e:
            print(f'Error while compiling {script}: {e}')
