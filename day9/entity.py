class Entity:
  def __init__(self, start_index, size):
    self.start_index = start_index
    self.end_index = start_index + size - 1
    self.size = size

class File(Entity):
  id = 0

  def __init__(self, start_index, size):
    super().__init__(start_index, size)
    self.id = File.id
    File.id += 1

  def move(self, new_start_index):
    self.start_index = new_start_index
    self.end_index = new_start_index + self.size - 1
    
  def get_checksum(self):
    checksum = 0
    for i in range(self.start_index, self.end_index + 1):
      checksum += i * self.id
    return checksum

  def __str__(self):
    return f"File {self.id} [{self.start_index}, {self.end_index}]"
  
  def __repr__(self):
    return self.__str__()
  
class Empty(Entity):
  def __init__(self, start_index, size):
    super().__init__(start_index, size)

  def add_to_empties(self, empties, skip_sort = False):
    if self.size in empties:
      empties[self.size].append(self)
      if not skip_sort:
        empties[self.size].sort(key=lambda x: x.start_index)
    else:
      empties[self.size] = [self]

  def remove_from_empties(self, empties):
    empties[self.size].remove(self)
    if len(empties[self.size]) == 0:
      empties.pop(self.size)

  def merge_file(self, file, empties):
    # normally we'd want to ensure we have enough space, but this is scrappy time
    new_empty = Empty(file.start_index, file.size)
    file.move(self.start_index)
    self.remove_from_empties(empties)

    # reduce this empty size if there is leftover space
    if self.size != file.size:
      new_size = self.size - file.size
      self.size = new_size
      self.start_index += file.size
      self.add_to_empties(empties)

    # check if we need to merge empties where the file moved from
    preceding_empty, following_empty = new_empty.find_neighbors(empties)
      
    if preceding_empty:
      new_empty.start_index = preceding_empty.start_index
      new_empty.size = preceding_empty.size + new_empty.size
      preceding_empty.remove_from_empties(empties)

    if following_empty:
      new_empty.end_index = following_empty.end_index
      new_empty.size = following_empty.size + new_empty.size
      following_empty.remove_from_empties(empties)

    new_empty.add_to_empties(empties)

  def find_neighbors(self, empties):
    preceding_empty = None
    following_empty = None
    for empty_set in empties.values():
      for empty in empty_set:
        if preceding_empty is None and empty.end_index + 1 == self.start_index:
          preceding_empty = empty
        elif following_empty is None and empty.start_index - 1 == self.end_index:
          following_empty = empty
        if preceding_empty is not None and following_empty is not None:
          return preceding_empty, following_empty
    return preceding_empty, following_empty

  def __str__(self):
    return f"Empty [{self.start_index}, {self.end_index}]"
  
  def __repr__(self):
    return self.__str__()