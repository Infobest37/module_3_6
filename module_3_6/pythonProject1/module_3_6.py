
def calculate_structure_sum(data_structure):
  sum_1 = 0
  if isinstance(data_structure, (int, float)):
    sum_1 += data_structure
  elif isinstance(data_structure, (list,tuple, set)):
    for i in data_structure:
      sum_1 += calculate_structure_sum(i)
  elif isinstance(data_structure, dict):
    for value in data_structure:
      sum_1 += calculate_structure_sum(value)

  return sum_1
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)
