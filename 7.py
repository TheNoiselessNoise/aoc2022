TODO = False
SKIP = True
EXIT = True
TIME_IT = True
TEST = False
TEST_SHOW_DIFF = True
TEST_CASE_RESULT = 24933642
TEST_CASE = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

from pathlib import Path

def get_tree(cmds):
    d = Path("")
    tree = {}
    for cmd in cmds:
        e = cmd.split()
        if "$ cd" in cmd:
            d = d.parent if ".." in cmd else d / e[2]
            if d not in tree:
                tree[d] = []
        elif e[0] == "dir":
            tree[d].append(d / e[1])
        elif e[0].isdigit():
            tree[d].append((e[1], int(e[0])))
    return tree

def total_size(path, tree):
    return sum(x[1] if isinstance(x, tuple) else total_size(x, tree) for x in tree[path])

def compute(what): # part 2
    commands = [x for x in what.split('\n') if x]
    tree = get_tree(commands)
    sizes = {d: total_size(d, tree) for d in tree}

    used = sizes[Path("/")]
    need = 30000000 - (70000000 - used)
    return min([sizes[d] for d in sizes if sizes[d] >= need])

def compute_part1(what):
    commands = [x for x in what.split('\n') if x]
    tree = get_tree(commands)
    sizes = {d: total_size(d, tree) for d in tree}
    return sum(dir_size for dir_size in sizes.values() if dir_size < 100000)
