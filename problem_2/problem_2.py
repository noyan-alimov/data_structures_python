import os


def find_files(suffix, path):
    paths = []

    if os.path.isfile(path):
        if path.endswith(suffix):
            paths.append(path)
    else:
        if os.path.isdir(path):
            sub_directories = os.listdir(path)
            for sub_directory in sub_directories:
                sub_paths = find_files(suffix, f'{path}/{sub_directory}')
                for sub_path in sub_paths:
                    paths.append(sub_path)
    
    return paths


def test_function_1(suffix, path):
    paths = find_files(suffix, path)
    if paths and type(paths) == list:
        print('Test Success')
    else:
        print('Test Failed')


def test_function_2(suffix, path):
    paths = find_files(suffix, path)
    if not paths:
        print('Test Success')
    else:
        print('Test Failed') 

test_function_1('.c', f'{os.path.abspath(os.getcwd())}/testdir')  # expect to return a non-empty list 
test_function_2('', '')  # expect to return an empty list
test_function_2('jfhdalksjdfh', 'sjdfhsakajfhk')  # expect to return an empty list
test_function_2(None, None)  # expect a Type Error because of invalid input parameters