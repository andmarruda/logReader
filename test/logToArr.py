from src.reader import reader

list = reader('../test/postgresql/postgresql-main.log').toList()
print(list)