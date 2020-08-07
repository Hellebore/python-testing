# this is a test script



if True:
    pass


def function():
    if False:
        pass

    if x == None:
        do_x()

    return None
    do_x()


def func2():
    if False:
        pass



def move_assign(cond1, cond2):
  a_var = 10
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
    if cond2:
      print(a_var)
    print(a_var)


def remove_escapes(text: str) -> str:
    counter = 0
    res = ""
    is_escaped = False
    while counter < len(text):
        if is_escaped:
            res += text[counter]
            is_escaped = False
        elif text[counter] == "\\":
            is_escaped = True
        else:
            res += text[counter]
        counter += 1
    return res