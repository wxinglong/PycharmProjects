import collections
Vecs = collections.namedtuple('Vecs', ['x', 'y', 'z'])
def position_vec(position_list):
    return Vecs(position_list[0], position_list[1], position_list[2])
position_list = [1, 2, 3]
print(position_vec(position_list).x)
print(position_vec(position_list).y)