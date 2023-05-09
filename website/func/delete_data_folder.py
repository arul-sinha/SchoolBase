from cs50 import *
db_users = SQL("sqlite:///../sql/users.db")
db_users.execute("DELETE FROM users")
