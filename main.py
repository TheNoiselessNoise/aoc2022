import os
import time
import importlib.util
from contextlib import suppress

def get_def(typ=None):
    if typ is int: return -1
    if typ is str: return ''
    if typ is list: return []
    if typ is dict: return {}
    if typ is set: return set()
    if typ is tuple: return ()
    if typ is bool: return False
    return None

def get_attr(module, what, typ=None):
    attr = get_def(typ)
    with suppress(AttributeError):
        attr = getattr(module, what)
    return attr

def get_str_time(t):
    t1 = round((time.time() - t) * 1000)
    return str(t1) + " ms"

def check_file(module_path, file_input_path):
    spec = importlib.util.spec_from_file_location(file.replace('.py', ''), module_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    # getting modules attributes
    todo = get_attr(mod, 'TODO', bool)
    skip = get_attr(mod, 'SKIP', bool)
    is_exit = get_attr(mod, 'EXIT', bool)
    time_it = get_attr(mod, 'TIME_IT', bool)
    test = get_attr(mod, 'TEST', bool)
    test_show_diff = get_attr(mod, 'TEST_SHOW_DIFF', bool)
    test_case = get_attr(mod, 'TEST_CASE', str)
    test_case_result = get_attr(mod, 'TEST_CASE_RESULT', int)

    # file names
    file_name = os.path.basename(module_path)
    file_input_name = os.path.basename(file_input_path)

    if is_exit:
        if todo:
            print("[!] Exiting {}, but has a TODO!".format(file_name))
        return

    # check if module has a needed function
    if not hasattr(mod, 'compute'):
        print("ERROR: {} doesn't have 'compute(input)' function!".format(file_name))
        return

    # printing
    if os.path.isfile(file_input):
        print("--> Executing with input: {} [{}]".format(file_name, file_input_name))
    else:
        print("--> Executing: {}".format(file_name))

    # executing
    if skip:
        print('Skipping...', "[TODO]" if todo else "")
    else:
        t0 = time.time()
        if test:
            a = mod.compute(test_case)
            b = test_case_result
            result = "OK" if a == b else "INVALID"
            str_time = "" if not time_it else "[" + get_str_time(t0) + "] "
            str_res = "{}Test result: {}".format(str_time, result)
            print(str_res)

            if not result and test_show_diff:
                print("Got:      {}\nExpected: {}".format(a, b))
        else:
            if os.path.isfile(file_input_path):
                with open(file_input_path, 'r') as f:
                    str_time = "" if not time_it else "[" + get_str_time(t0) + "] "
                    str_res = "{}Answer: {}".format(str_time, mod.compute(f.read()))
                    print(str_res)
            else:
                print('No input file found!')


if __name__ == '__main__':
    this_name = os.path.basename(__file__)
    this_path = os.path.dirname(os.path.realpath(__file__))

    files = []
    for file in os.listdir(this_path):
        filepath = os.path.join(this_path, file)
        if os.path.isfile(filepath) and file != this_name and file.endswith('.py') and file != "empty.py":
            files.append(filepath)

    if len(files) > 0:
        for file in files:
            file_path = os.path.join(this_path, file)
            file_input = os.path.join(this_path, file.replace('.py', '.txt'))
            check_file(file_path, file_input)
    else:
        print("No files found")
