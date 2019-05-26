import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if path[-2:] == suffix:
        print(path)
    else:
        if os.path.isdir(path):
            for file in os.listdir(path):
                find_files(suffix, os.path.join(path, file))

# Test Cases
find_files(".c", "./testdir")
print("--------------------")
find_files(".h", "./testdir")
print("--------------------")
find_files(".z", "./testdir")

# expected output:
# ./testdir/subdir3/subsubdir1/b.c
# ./testdir/t1.c
# ./testdir/subdir5/a.c
# ./testdir/subdir1/a.c
# --------------------
# ./testdir/subdir3/subsubdir1/b.h
# ./testdir/subdir5/a.h
# ./testdir/t1.h
# ./testdir/subdir1/a.h
# --------------------
