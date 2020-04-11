

def __getstate__(self):
  state = {}
  state['min'] = self.min
  state['max'] = self.max
  return state


def list_comprehension():
  # comment
  if a:
    new_list = []
    for i in old_list:
      if filter(i):
        new_list.append(expressions(i))


def while_to_for():
  i = 0
  while i < 10:
    do_x()
    i += 1