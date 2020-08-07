# this is a test script



pass


def function():
    if x is None:
        do_x()

    return None


def func2():
    pass



def move_assign(cond1, cond2):
    b_var = 20
    b_var = 20
    b_var = 20
    b_var = 20
    b_var = 20
    b_var = 20
    b_var = 20
    b_var = 20
    b_var = 20
    b_var = 20
    b_var = 20
    b_var = 20
    if cond1:
        c_var = 30
        a_var = 10
        if cond2:
          print(a_var)
        print(a_var)


def remove_escapes(text: str) -> str:
    res = ""
    is_escaped = False
    for item in text:
        if is_escaped:
            res += item
            is_escaped = False
        elif item == "\\":
            is_escaped = True
        else:
            res += item
    return res