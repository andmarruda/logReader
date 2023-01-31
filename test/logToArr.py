from src.reader import reader
from src.pgsqlAuthFailed import pgsqlAuthFailed
from src.filter import filter

f = pgsqlAuthFailed().getFilter()
reader = reader('../test/postgresql/postgresql-main.log')
reader.set_filter(f)
list = reader.filter_all()
print(list)