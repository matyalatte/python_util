import os,shutil


def mkdir(dir):
    os.makedirs(dir, exist_ok=True)

#if remove_line_break:
#   return ['a','b','c',...]
#else:
#   return ['a\n','b\n','c\n',...]
def read_txt(file, remove_line_break=True, ignore_extention=False):
    if file[-4:]!=".txt" and not ignore_extention:
        raise ValueError("'file' should be a text file.")

    with open(file) as f:
        if remove_line_break:
            lines = f.read().splitlines()
        else:
            lines = f.readlines()

    return lines

#let lines=['a','b','c',...]
#if insert_line_break:
#   write 'a/n'+'b/n'+'c/n'+...
#else:
#   write 'abc...'
def write_txt(file, lines, insert_line_break=True, ignore_extention=False):
    if file[-4:]!=".txt" and not ignore_extention:
        raise ValueError("'file' should be a text file.")

    with open(file, "w") as f:
        if insert_line_break:
            f.write("\n".join(lines)) 
        else:
            f.writelines(lines)
