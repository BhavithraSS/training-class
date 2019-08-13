def even_values_string(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

print(even_values_string('h1e2l3l4o5w6o7r8l9d'))
