''' Module Providing ASCII Table Art '''
from prettytable import PrettyTable

# Creating a object from PrettyTable Class
table = PrettyTable()

# Before any data
print(table)

table.add_column("Pokemon",['Pikachu','Squirtle','Charmander'])
table.add_column("Type",['Electric','Water','Fire'])

# Changing from cetner align to left align
table.align="l"

# After adding the column with Pokemon and Type
print(table)
