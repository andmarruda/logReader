from src.pgsqlAuthFailed import pgsqlAuthFailed

pg = pgsqlAuthFailed('../test/postgresql/postgresql-main.log')
print(pg.getFiltered())